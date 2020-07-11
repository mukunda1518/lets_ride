import factory
from lets_ride_auth.models.user import User
from lets_ride_auth.interactors.storages.dtos import UserDTO

class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = factory.Sequence(lambda n: "username%d" % n)
    phone_number = factory.Sequence(lambda n: 9234567111 + n)


# class UserDtoFactory(factory.factory):
#     class Meta:
#         model = UserDTO

#     user_id = factory.Sequence(lambda n: n)
#     username = factory.Sequence(lambda n: "username%d" % n)
#     phone_number = factory.Sequence(lambda n: 9234567111 + n)
#     profile_pic = factory.Sequence(lambda n : "http://userprofile%d" % n)

