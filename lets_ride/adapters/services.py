class Services:

    @property
    def auth_service(self):
        from lets_ride.adapters.auth_service import AuthService
        return AuthService()


def get_service():
    return Services()
