class Organizations:
    def __init__(self, session):
        self.session = session

    def get_organizations(self):
        url = '/organizations'
        return self.session.get(url)

    def get_organization(self, organizationid):
        url = f'/organizations/{organizationid}'
        return self.session.get(url)
