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

        #Assigns (train [i] stop [j]) to variable this_train for easier reference in following checks
        this_train = a_trains[i].stop_time_updates[j]

        if this_train.stop_id == "A06S":
            print(this_train.stop_id)
            print(str(this_train))
            print(this_train.arrival)
            print(datetime.today())
            print(this_train.arrival - datetime.today())
