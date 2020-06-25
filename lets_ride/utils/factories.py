import factory
from lets_ride.models import  fact
from factory import fuzzy


class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = fact.Group

    name = factory.Sequence(lambda n: "Group #%s" % n)



class User1Factory(factory.django.DjangoModelFactory):
    class Meta:
        model = fact.User1

    first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    group = factory.SubFactory(GroupFactory)


# class User1Factory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = fact.User1

#     first_name = factory.Sequence(lambda n: "Agent %03d" % n)
#     group = factory.Iterator(fact.Group.objects.all())


class UserLogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = fact.UserLog

    action = factory.Sequence(lambda n: "Action %03d" % n)

class User2Factory(factory.django.DjangoModelFactory):
    class Meta:
        model = fact.User2

    name = factory.Sequence(lambda n: "User %d" % n)
    userlog = factory.RelatedFactory(UserLogFactory, 'user')







class Group1Factory(factory.django.DjangoModelFactory):
    class Meta:
        model = fact.Group1

    name = factory.Sequence(lambda n: "Group #%s" % n)


class User3Factory(factory.django.DjangoModelFactory):
    class Meta:
        model = fact.User3

    name = "John Doe"

    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        print("-----create------ ", create)
        if not create:
            # Simple build, do nothing.
            return

        print("-------extracted------ ",extracted)
        print("------kwargs------- ",kwargs)
        if extracted:
            # A list of groups were passed in, use them
            for group in extracted:
                self.groups.add(group)



class User4Factory(factory.django.DjangoModelFactory):
    class Meta:
        model = fact.User4

    name = "John Doe"

class Group4Factory(factory.django.DjangoModelFactory):
    class Meta:
        model = fact.Group4

    name = "Admins"

class GroupLevelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = fact.GroupLevel

    user = factory.SubFactory(User4Factory)
    group = factory.SubFactory(Group4Factory)
    rank = 1


class UserWithGroupFactory(User4Factory):
    membership = factory.RelatedFactory(GroupLevelFactory, 'user')

class UserWith2GroupsFactory(User4Factory):
    membership1 = factory.RelatedFactory(GroupLevelFactory, 'user', group__name='Group1')
    membership2 = factory.RelatedFactory(GroupLevelFactory, 'user', group__name='Group2')





class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = fact.Country

    name = factory.Iterator(["France", "Italy", "Spain"])
    lang = factory.Iterator(['fr', 'it', 'es'])



class User5Factory(factory.django.DjangoModelFactory):
    class Meta:
        model = fact.User5

    lang = factory.SelfAttribute('country.lang')
    country = factory.SubFactory(CountryFactory)
    name = "john"



class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = fact.Company

    name = "ACME, Inc."
    country = factory.SubFactory(CountryFactory)
    owner = factory.SubFactory(
        User5Factory,
        country=factory.LazyAttribute(lambda o: o.factory_parent.country)
    )


# class OrganizationFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         models = fact.Organization

#     name = "IB hubs"
#     country = factory.SubFactory(CountryFactory, name="India")

# class User6Factory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = fact.User6

class User6Factory(factory.django.DjangoModelFactory):
    class Meta:
        model = fact.User6

    first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    last_name = factory.fuzzy.FuzzyChoice(
        [("user", "user1"), ("user1", "user2")],
        getter=lambda c: c[0]
    )
