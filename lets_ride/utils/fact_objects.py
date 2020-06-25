import datetime
import factory
import random

from . import objects


class AccountFactory(factory.Factory):
    class Meta:
        model = objects.Account

    username = factory.Sequence(lambda n: 'john%s' % n)
    email = factory.LazyAttribute(lambda o: '%s@example.org' % o.username)
    date_joined = factory.LazyFunction(datetime.datetime.now)


class ProfileFactory(factory.Factory):
    class Meta:
        model = objects.Profile

    account = factory.SubFactory(AccountFactory)
    gender = factory.Iterator([objects.Profile.GENDER_MALE, objects.Profile.GENDER_FEMALE])
    firstname = u'John'
    lastname = u'Doe'


class FemaleProfileFactory(ProfileFactory):
    gender = objects.Profile.GENDER_FEMALE
    firstname = u'Jane'
    account__username = factory.Sequence(lambda n: 'jane%s' % n)
