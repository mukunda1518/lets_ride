import factory
from lets_ride_auth.models.user import User

class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = factory.Sequence(lambda n: "username %d" % n)
    phone_number = factory.Sequence(lambda n: 9234567111 + n)
