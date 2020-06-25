import factory

from datetime import datetime, date, timedelta

from factory import fuzzy

from lets_ride.models.user import User
from lets_ride.models import log
from lets_ride.models import rental
from lets_ride.models import order


# class UserFactory(factory.Factory):
#     class Meta:
#         model = User

#     username = "john"
#     phone_number = "1234567890"


# class EnglishUserFactory(factory.Factory):
#     class Meta:
#         model = User

#     username = "john"


# class FrenchUserFactory(factory.Factory):
#     class Meta:
#         model = User

#     username = "john"


# class UserFactory(factory.Factory):
#     class Meta:
#         model = User

#     username = factory.Sequence(lambda n: 'user%d' % n)

# class UserFactory(factory.DjangoModelFactory):
#     class Meta:
#         model = User

#     phone_number = "111111111111"

#     @factory.sequence
#     def username(n):
#         return 'user%d' % n


class LogFactory(factory.Factory):
    class Meta:
        model = User
        model = log.Log

    # username = "john"
    # timestamp = factory.LazyFunction(datetime.now)


# class UserFactory(factory.Factory):
#     class Meta:
#         model = User

#     username = factory.Sequence(lambda n: 'user%d' % n)
#     email = factory.LazyAttribute(lambda obj: '%s@example.com' % obj.username)

class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'user%d' % n)

    @factory.lazy_attribute
    def email(self):
        return '%s@example.com' % self.username


class RentalFactory(factory.Factory):
    class Meta:
        model = rental.Rental

    begin = factory.fuzzy.FuzzyDate(start_date=date(2000, 1, 1))
    end = factory.LazyAttribute(lambda o: o.begin + timedelta(o.duration))

    class Params:
        duration = 12


class OrderFactory(factory.Factory):
    status = 'pending'
    shipped_by = None
    shipped_on = None

    class Meta:
        model = order.Order

    class Params:
        shipped = factory.Trait(
            status='shipped',
            shipped_by=factory.SubFactory(UserFactory),
            shipped_on=factory.LazyFunction(date.today),
        )