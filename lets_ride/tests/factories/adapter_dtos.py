import factory

from lets_ride.adapters.dtos import UserDetailsDTO

class UserDetailsDTOFactory(factory.factory):

    class Meta:
        model = UserDetailsDTO

    user_id = factory.Sequence(lambda n: n)
    username = factory.Sequence(lambda n: "username%d" %n)
    phone_number = factory.Sequence(lambda n: "956718211%d" %n)
