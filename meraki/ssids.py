class SSIDs:
    def __init__(self, session):
        self.session = session

    def get_ssids(self, networkid):
        url = f'/networks/{networkid}/ssids'
        return self.session.get(url)

    def get_ssid(self, networkid, number):
        url = f'/networks/{networkid}/ssids/{number}'
        return self.session.get(url)

    def get_ssid_for_ap(self, networkid, serial):
        url = f'/networks/{networkid}/devices/{serial}/wireless/status'
        return self.session.get(url)
