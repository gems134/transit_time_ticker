from nyct_gtfs import NYCTFeed
#181st street stop ID - A06N

feed = NYCTFeed("A", api_key="tUVO9eM8wV2nQuwSsWIer23kedIlYHwD3PM7ZHqc")
#print(type(feed.trips[0]))
#train = feed.trips[0]


for i in range(20):
    if feed.trips[i].direction == "N":
        train = feed.trips[i]
        for j in range(len(train.stop_time_updates)):
            print(train.stop_time_updates[j].stop_name)
            print(train.stop_time_updates[j].stop_id)
            

# this looks at the twenty trips, tries to find a northbound trip, and prints all remaining stops and their identifiers

