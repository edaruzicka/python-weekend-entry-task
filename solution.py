import csv
import json
import argparse

def arg_parser():
    parser = argparse.ArgumentParser(description='Kiwi task solution')
    parser.add_argument('csv_file', help='csv file path')
    parser.add_argument('origin', help='origin')
    parser.add_argument('destination', help='destination')
    parser.add_argument('-b', '--bags', help='bags', required=False, type=int)
    parser.add_argument('-r', '--return', help='return', required=False)
    args = vars(parser.parse_args())
    return args

def main():
    args = arg_parser()
    arg_csv_filename = args.get('csv_file')
    arg_origin = args.get('origin')
    arg_destination = args.get('destination')
    arg_bags = args.get('bags')
    print(args)

    with open(arg_csv_filename) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader) # skip headers

        for row in reader:
            flight_no, origin, destination, departure, arrival, base_price, bag_price, bags_allowed = row[0], row[1], row[2], row[3], row[4], float(row[5]), float(row[6]), int(row[7])
            if origin == arg_origin and destination == arg_destination:
                #print(row)

                fligts = [{'flights':
                            [{
                            'flight_no': flight_no,
                            'origin': origin,
                            'destination': destination,
                            'departure': departure,
                            'arrival': arrival,
                            'base_price': base_price,
                            'bag_price': bag_price,
                            'bags_allowed': bags_allowed
                            }],
                        "bags_allowed": bags_allowed,
                        "bags_count": arg_bags,
                        "destination": destination,
                        "origin": origin,
                        "total_price": base_price + bag_price * arg_bags,
                        "travel_time": "TBD"
                        }]

                output = json.dumps(fligts, indent=4)
                print(output)

if __name__ == "__main__":
    main()
