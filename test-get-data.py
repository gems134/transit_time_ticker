from nyct_gtfs import NYCTFeed
feed = NYCTFeed("A", api_key="tUVO9eM8wV2nQuwSsWIer23kedIlYHwD3PM7ZHqc")

import datetime
now = datetime.datetime.now()
now

print(now)


# Read all trip (train) information published to the BDFM feed 
train1 = feed.trips[0]
train2 = feed.trips[1]

print(train1.direction)
print(train2)

trains = feed.filter_trips(line_id=["A"], headed_for_stop_id=["A06S"], travel_direction="S")
print(trains[0].stop_time_updates[3])

next = (trains[0].stop_time_updates[3].arrival)
print(next)



