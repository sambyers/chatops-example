![Test and Deploy ChatOps Example to Lambda](https://github.com/sambyers/chatops-example/workflows/Test%20and%20Deploy%20ChatOps%20Example%20to%20Lambda/badge.svg?branch=master)

# ChatOps Example
An example exercise to create a bot that displays network infrastruture information in a Webex Teams space. Anyone granted access can trigger the bot with a slash command (/command) in a direct message or by mentioning the bot (@ChatOpsExample).

## Commands supported:
### /ssid
Searches all SSIDs the bot is privileged to access and replies with a list of enabled SSIDs.

### /networks
Searches all networks the bot is privileged to access and replies with a list.

### /orgs
Searches all orgs the bot is privileged to access and replies with a list.

### /help
Displays help text describing how to use the bot.

## Deployment
The bot code is tested and deployed to a AWS lambda function by a GitHub workflow.