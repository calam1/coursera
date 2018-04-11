def how_many_stops(stations, mileage):
    '''return the indexes of the gas station stops'''
    gas_stops = []
    i = 0

    # iterate through the stations
    while i < len(stations):
        # if  i < length of gas stops and the distance between 2 stations are viable
        if i + 1 < len(stations) and stations[i + 1] - stations[i] <= mileage:
            print(
            'i is: {} station i is: {} station i+1 is: {} difference is: {}'.format(i, stations[i + 1], stations[i],
                                                                                    stations[i + 1] - stations[i]))
            # add the station
            gas_stops.append(i)
            # add the starting point
            last_mileage_tracker = stations[i]
            print('last_mileage_tracker {}'.format(last_mileage_tracker))  # these are the stations we go to

            # if the next station exists and if the next stations is within the mileage of the car (next right point - starting point)
            while i + 1 < len(stations) and stations[i + 1] - last_mileage_tracker <= mileage:
                gas_stops.pop()  # remove the old, we just want the stations we need to stop at
                gas_stops.append(i + 1)  # add current gas stations
                i += 1 # go to the next gas station
        else:
            # if the mileage between the 2 stations is above the capability of the car then error out
            if i < len(stations) - 1 and stations[i + 1] - stations[i] > mileage:
                print('Impossible')
                exit(1)
            else:
                #iterate through counter to finish outer while loop
                i += 1

    return gas_stops


MILEAGE = 400
GAS_STATIONS = [35, 150, 190, 390, 500, 650, 800, 1000]
#GAS_STATIONS = [35, 150, 390, 500, 650, 800, 1000]
#GAS_STATIONS = [0, 200, 375, 550, 750, 950]
#GAS_STATIONS=[0, 200, 650, 950] # BAD

print(how_many_stops(GAS_STATIONS, MILEAGE))
