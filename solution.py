import csv
import json
import argparse
from datetime import datetime, timedelta
from xmlrpc.client import Boolean, boolean

class Flight:
    """
    A class used to represent a Flight

    ...

    Attributes
    ----------
    flight_no : str
        flight number
    origin : str
        origin airport
    destination : str
        destination airport
    departure : str
        departure time
    arrival : str
        arrival time
    base_price : float
        base price for the flight
    bag_price : float
        price for each bag carried by the passenger
    bags_allowed : int
        maximum allowed number of bags on the flight
    """

    def __init__(self, flight_no, origin, destination, departure, arrival, base_price, bag_price, bags_allowed):
        self.flight_no = flight_no
        self.origin = origin
        self.destination = destination
        self.departure = departure
        self.arrival = arrival
        self.base_price = base_price
        self.bag_price = bag_price
        self.bags_allowed = bags_allowed

def arg_parser():
    """Argument parser function"""
    parser = argparse.ArgumentParser(description='Kiwi task solution')
    parser.add_argument('csv_file', help='csv file path')
    parser.add_argument('origin', help='origin airport')
    parser.add_argument('destination', help='destination airport')
    parser.add_argument('-b', '--bags', help='number of bags', required=False, type=int, default=0)
    parser.add_argument('-r', '--return', help='return flight - not implemented', required=False, default=False)
    args = vars(parser.parse_args())
    return args

def main():
    """Main function. 
    
    Creates Flight class instances, then searches for all the possible routes
    depending on initial arguments, prints and returns json with flights
    sorted by total price.

    Maximum number of transfer flights is 1, meaning its possible to only find routes A -> B and A -> B -> C.
    """

    args = arg_parser()
    arg_csv_filename = args.get('csv_file')
    arg_origin = args.get('origin')
    arg_destination = args.get('destination')
    arg_bags = args.get('bags')
    print(args)

    with open(arg_csv_filename) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader) # skips headers

        flights = []
        flightsDest = []
        finalOutput =  []


        for row in reader:
            
            # create Flight instances and add to list
            flights.append(Flight(row[0], row[1], row[2], row[3], row[4], float(row[5]), float(row[6]), int(row[7])))

        # filter all flights with desired destination
        for flight in flights:
            if flight.destination == arg_destination:
                flightsDest.append(flight)

        # find all possible routes, which end in desired destination
        for flightDest in flightsDest:
            trip = {}

            # 1 flight: A -> B
            if flightDest.origin == arg_origin and flightDest.destination == arg_destination:
                trip["flights"] = flightDest.__dict__

                trip["bags_allowed"] = flightDest.bags_allowed
                trip["bags_count"] = arg_bags
                trip["destination"] = flightDest.destination
                trip["origin"] = flightDest.origin
                trip["total_price"] = flightDest.base_price + flightDest.bag_price * arg_bags
                trip["travel_time"] = str(datetime.strptime(flightDest.arrival, "%Y-%m-%dT%H:%M:%S") - datetime.strptime(flightDest.departure, "%Y-%m-%dT%H:%M:%S"))
                
                if trip["bags_allowed"] >= arg_bags:
                    finalOutput.append(trip)

                continue

            # 2 flights: A -> B -> C
            for flight in flights:
                if flight.destination == flightDest.origin:

                    # waiting time at the airport between flights
                    layoverTime = datetime.strptime(flightDest.departure, "%Y-%m-%dT%H:%M:%S") - datetime.strptime(flight.arrival, "%Y-%m-%dT%H:%M:%S")

                    if flight.origin == arg_origin and layoverTime > timedelta(hours = 1) and layoverTime < timedelta(hours = 6):
                        trip["flights"] = flight.__dict__, flightDest.__dict__

                        trip["bags_allowed"] = min(flightDest.bags_allowed, flight.bags_allowed)
                        trip["bags_count"] = arg_bags
                        trip["destination"] = flightDest.destination
                        trip["origin"] = flight.origin
                        trip["total_price"] = flightDest.base_price + flight.base_price + flightDest.bag_price * arg_bags + flight.bag_price * arg_bags
                        trip["travel_time"] = str(datetime.strptime(flightDest.arrival, "%Y-%m-%dT%H:%M:%S") - datetime.strptime(flight.departure, "%Y-%m-%dT%H:%M:%S"))

                        if trip["bags_allowed"] >= arg_bags:
                            finalOutput.append(trip)

                        break
        
        finalOutput.sort(key=lambda x: x["total_price"])
        print(json.dumps(finalOutput, indent=4, sort_keys=False))
        return json.dumps(finalOutput, indent=4, sort_keys=False)

if __name__ == "__main__":
    main()
