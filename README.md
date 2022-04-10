# Python weekend entry task - solution by Eduard Ruzicka - edaruzicka@seznam.cz

**A python script, that for a given flight data in a form of `csv` file, prints out a json of all flight combinations for a selected route between airports A -> B, sorted by the final price for the trip.**

### Description
CSV file structure:
- `flight_no`: Flight number.
- `origin`, `destination`: Airport codes.
- `departure`, `arrival`: Dates and times of the departures/arrivals.
- `base_price`, `bag_price`: Prices of the ticket and one piece of baggage.
- `bags_allowed`: Number of allowed pieces of baggage for the flight.

Required arguments:

| Argument name | type    | Description              | Notes                        |
|---------------|---------|--------------------------|------------------------------|
| `origin`      | string  | Origin airport code      |                              |
| `destination` | string  | Destination airport code |                              |

### Search restrictions - all are implemented
- By default you're performing search on ALL available combinations, according to search parameters.
- In case of a combination of A -> B -> C, the layover time in B should **not be less than 1 hour and more than 6 hours**.
- No repeating airports in the same trip!
    - A -> B -> A -> C is not a valid combination for search A -> C.
- Output is sorted by the final price of the trip.

#### Optional arguments

| Argument name | type    | Description              | Notes                        |
|---------------|---------|--------------------------|------------------------------|
| `bags`        | integer | Number of requested bags | Optional (defaults to 0)     |

##### Performing return trip search
Example input, `solution.py` is the main module:
```
python -m solution example/example0.csv RFZ WIW --bags=1
```
will perform a search RFZ -> WIW for flights which allow at least 1 piece of baggage.

#### Output
The output is a json-compatible structured list of trips sorted by price. The trip has the following schema:
| Field          | Description                                                   |
|----------------|---------------------------------------------------------------|
| `flights`      | A list of flights in the trip according to the input dataset. |
| `origin`       | Origin airport of the trip.                                   |
| `destination`  | The final destination of the trip.                            |
| `bags_allowed` | The number of allowed bags for the trip.                      |
| `bags_count`   | The searched number of bags.                                  |
| `total_price`  | The total price for the trip.                                 |
| `travel_time`  | The total travel time.                                        |

## Example behaviour

I wrote the solution into one file, `solution.py` and the example datatsets are in folder `examples`.
We want to test the script by performing a flight search on route NRX -> DHE (we know the airports are present in the dataset) with two bags. We run the thing:

```bash
python -m solution example/example1.csv NRX DHE --bags=2
```
and get the following result:

```json
[
    {
        "flights": {
            "flight_no": "IM218",
            "origin": "SML",
            "destination": "NIZ",
            "departure": "2021-09-02T04:35:00",
            "arrival": "2021-09-02T08:40:00",
            "base_price": 120.0,
            "bag_price": 9.0,
            "bags_allowed": 2
        },
        "bags_allowed": 2,
        "bags_count": 2,
        "destination": "NIZ",
        "origin": "SML",
        "total_price": 138.0,
        "travel_time": "4:05:00"
    },
    {
        "flights": {
            "flight_no": "IM218",
            "origin": "SML",
            "destination": "NIZ",
            "departure": "2021-09-04T04:35:00",
            "arrival": "2021-09-04T08:40:00",
            "base_price": 120.0,
            "bag_price": 9.0,
            "bags_allowed": 2
        },
        "bags_allowed": 2,
        "bags_count": 2,
        "destination": "NIZ",
        "origin": "SML",
        "total_price": 138.0,
        "travel_time": "4:05:00"
    },
    {
        "flights": {
            "flight_no": "IM218",
            "origin": "SML",
            "destination": "NIZ",
            "departure": "2021-09-08T04:35:00",
            "arrival": "2021-09-08T08:40:00",
            "base_price": 120.0,
            "bag_price": 9.0,
            "bags_allowed": 2
        },
        "bags_allowed": 2,
        "bags_count": 2,
        "destination": "NIZ",
        "origin": "SML",
        "total_price": 138.0,
        "travel_time": "4:05:00"
    },
    {
        "flights": {
            "flight_no": "IM218",
            "origin": "SML",
            "destination": "NIZ",
            "departure": "2021-09-13T04:35:00",
            "arrival": "2021-09-13T08:40:00",
            "base_price": 120.0,
            "bag_price": 9.0,
            "bags_allowed": 2
        },
        "bags_allowed": 2,
        "bags_count": 2,
        "destination": "NIZ",
        "origin": "SML",
        "total_price": 138.0,
        "travel_time": "4:05:00"
    },
    {
        "flights": {
            "flight_no": "WM094",
            "origin": "SML",
            "destination": "NIZ",
            "departure": "2021-09-02T06:30:00",
            "arrival": "2021-09-02T10:35:00",
            "base_price": 122.0,
            "bag_price": 12.0,
            "bags_allowed": 2
        },
        "bags_allowed": 2,
        "bags_count": 2,
        "destination": "NIZ",
        "origin": "SML",
        "total_price": 146.0,
        "travel_time": "4:05:00"
    },
    {
        "flights": {
            "flight_no": "WM094",
            "origin": "SML",
            "destination": "NIZ",
            "departure": "2021-09-03T06:30:00",
            "arrival": "2021-09-03T10:35:00",
            "base_price": 122.0,
            "bag_price": 12.0,
            "bags_allowed": 2
        },
        "bags_allowed": 2,
        "bags_count": 2,
        "destination": "NIZ",
        "origin": "SML",
        "total_price": 146.0,
        "travel_time": "4:05:00"
    },
    {
        "flights": {
            "flight_no": "WM094",
            "origin": "SML",
            "destination": "NIZ",
            "departure": "2021-09-07T06:30:00",
            "arrival": "2021-09-07T10:35:00",
            "base_price": 122.0,
            "bag_price": 12.0,
            "bags_allowed": 2
        },
        "bags_allowed": 2,
        "bags_count": 2,
        "destination": "NIZ",
        "origin": "SML",
        "total_price": 146.0,
        "travel_time": "4:05:00"
    },
    {
        "flights": {
            "flight_no": "WM094",
            "origin": "SML",
            "destination": "NIZ",
            "departure": "2021-09-12T06:30:00",
            "arrival": "2021-09-12T10:35:00",
            "base_price": 122.0,
            "bag_price": 12.0,
            "bags_allowed": 2
        },
        "bags_allowed": 2,
        "bags_count": 2,
        "destination": "NIZ",
        "origin": "SML",
        "total_price": 146.0,
        "travel_time": "4:05:00"
    },
    {
        "flights": [
            {
                "flight_no": "WM608",
                "origin": "SML",
                "destination": "DHE",
                "departure": "2021-09-02T02:15:00",
                "arrival": "2021-09-02T03:45:00",
                "base_price": 46.0,
                "bag_price": 12.0,
                "bags_allowed": 2
            },
            {
                "flight_no": "IM405",
                "origin": "DHE",
                "destination": "NIZ",
                "departure": "2021-09-02T08:20:00",
                "arrival": "2021-09-02T13:30:00",
                "base_price": 219.0,
                "bag_price": 9.0,
                "bags_allowed": 2
            }
        ],
        "bags_allowed": 2,
        "bags_count": 2,
        "destination": "NIZ",
        "origin": "SML",
        "total_price": 307.0,
        "travel_time": "11:15:00"
    }
]
```
