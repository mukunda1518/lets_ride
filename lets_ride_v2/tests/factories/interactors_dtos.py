import factory

from lets_ride_v2.interactors.dtos import RideRequestDTO



class RideRequestDTOFactory(factory.factory):

    class Meta:
        model = RideRequestDTO

    from_place = factory.Sequence(lambda n: "source%d" %n)
    to_place = factory.Sequence(lambda n: "destination%d" %n)
    no_of_seats = 4

    @factory.lazy_attribute
    def travel_date_time(self):
        from datetime import datetime, timedelta
        return datetime.now() + timedelta(10)
