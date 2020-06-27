import factory

from lets_ride.models.user import User

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    phone_number = factory.Sequence(lambda n: 9234567111+n)
    username = factory.Sequence(lambda n: "username%d" % n)

