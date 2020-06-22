import factory



class UserFactory(factory.Factory):
    class Meta:
        model = base.User

    firstname = "John"

