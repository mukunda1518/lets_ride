import factory
from .user import User

class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = "John"