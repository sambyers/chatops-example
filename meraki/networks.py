class Networks:
    def __init__(self, session):
        self.session = session

    def get_networks(self, organizationid):
        url = f'/organizations/{organizationid}/networks'
        return self.session.get(url)

    def get_network(self, networkid):
        url = f'/networks/{networkid}'
        return self.session.get(url)
