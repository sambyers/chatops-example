'''
Main module for chatops exercise
'''
from meraki import Meraki
from webexteamssdk import WebexTeamsAPI, Webhook
import json
import os


def get_all_enabled_ssids():
    '''Return all SSIDs across all orgs and nets that are enabled.'''
    api = Meraki()
    orgs_nets = get_all_networks()
    for org in orgs_nets:
        for net in org['networks']:
            if 'wireless' in net['productTypes']:
                net['ssids'] = []
                for ssid in api.ssids.get_ssids(net['id']):
                    if ssid['enabled']:
                        ssid['psk'] = 'XXXXXXXXXX'  # Anonymize the SSID PSK
                        net['ssids'].append(ssid)
    return orgs_nets


def get_all_networks():
    api = Meraki()
    orgs_nets = get_all_organizations()
    for org in orgs_nets:
        org['networks'] = []
        for net in api.networks.get_networks(org['id']):
            org['networks'].append(net)
    return orgs_nets


def get_all_organizations():
    api = Meraki()
    orgs = [org for org in api.organizations.get_organizations()]
    return orgs


def to_msg(d):
    return json.dumps(d, indent=4)


def help_msg():
    return "Hi! Supported commands: /ssids, /networks, /orgs, /help"


def not_implemented_msg():
    return "Sorry. I don't understand your request."


def lambda_handler(event, context):
    webhook_obj = Webhook(event['body'])
    if webhook_obj.id == os.environ.get('WEBEX_TEAMS_WEBHOOK_ID'):
        wbxapi = WebexTeamsAPI()
        room = wbxapi.rooms.get(webhook_obj.data.roomId)
        message = wbxapi.messages.get(webhook_obj.data.id)
        me = wbxapi.people.me()
        if not message.personId == me.id:
            message_list = message.text.split(' ')
            if "/help" in message_list:
                wbxapi.messages.create(room.id, text=help_msg())
            elif "/ssids" in message_list:
                wbxapi.messages.create(room.id, text=to_msg(get_all_enabled_ssids()))
            elif "/networks" in message_list:
                wbxapi.messages.create(room.id, text=to_msg(get_all_networks()))
            elif "/orgs" in message_list:
                wbxapi.messages.create(room.id, text=to_msg(get_all_organizations()))
            else:
                wbxapi.messages.create(room.id, text=to_msg(not_implemented_msg()))
