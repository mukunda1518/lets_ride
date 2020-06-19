
class DomainDoesNotExist(Exception):

    def __init__(self, domain_id: int):
        self.domain_id = domain_id

class UserNotMemberOfDomain(Exception):

    def __init__(self, domain_id: int, user_id: int):
        self.domain_id = domain_id
        self.user_id = user_id

class InvalidPostIds(Exception):

    def __init__(self, invalid_post_ids: int):
        self.invalid_post_ids = invalid_post_ids


