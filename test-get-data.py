from nyct_gtfs import NYCTFeed
feed = NYCTFeed("A", api_key="tUVO9eM8wV2nQuwSsWIer23kedIlYHwD3PM7ZHqc")

#set a variable that represents the current time so that later on we can try and get the time until arrival
import datetime
now = datetime.datetime.now()
now

print(now)

#trains in the feed are chronological. this get the next two trains and sets them to a variable
train1 = feed.trips[0]
train2 = feed.trips[1]

#show direection of the next train and all info for the second to next train
print(train1.direction)
print(train2)

#filter A trains headed for a particular stop, going in the south direction, and then print the time related information for that train
trains = feed.filter_trips(line_id=["A"], headed_for_stop_id=["A06S"], travel_direction="S")
print(trains[0].stop_time_updates[3])

#gives the arrival time for the next train at a particular stop
next = (trains[0].stop_time_updates[3].arrival)
print(next)



