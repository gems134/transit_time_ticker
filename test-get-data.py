from nyct_gtfs import NYCTFeed
feed = NYCTFeed("A", api_key="tUVO9eM8wV2nQuwSsWIer23kedIlYHwD3PM7ZHqc")

# Read all trip (train) information published to the BDFM feed 
trains = feed.trips

len(trains)
print(len(trains))