from nyct_gtfs import NYCTFeed
from datetime import datetime
#181st street stop ID - A06S

feed = NYCTFeed("A", api_key="tUVO9eM8wV2nQuwSsWIer23kedIlYHwD3PM7ZHqc")

#Filters feed for trains that are A trains, going south, and headed for my stop.  Includes trains which haven't departed yet
a_trains = feed.filter_trips(line_id="A", travel_direction="S", headed_for_stop_id="A06S")

#Iterates through first 2 trains to find their arrival times for my stop, then calculates the time to arrival at my stop
### Intermittently pulling train arrival times which are much sooner than expected
for i in range(2):
    for j in range(4):
        if a_trains[i].stop_time_updates[j].stop_id == "A06S":
            print(a_trains[i].stop_time_updates[j].stop_id)

            print(a_trains[i].stop_time_updates[j].arrival)
            print(datetime.today())
            print(a_trains[i].stop_time_updates[j].arrival - datetime.today())
