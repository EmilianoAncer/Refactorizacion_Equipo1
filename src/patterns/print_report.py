from patterns.csv_utils import Ride


def create_content(rides):
    builder = [_create_headers("Taxi Report"), _create_table_headers()]
    for ride in rides:
        builder.append(_add_ride(ride))

    return "".join(builder)


def create_file(content: str):
    with open("financial-report.txt", "w") as file:
        file.write(content)


def _create_headers(title: str):
    return f"{title}\n"


def _create_table_headers():
    return 'TaxiID\t\tPickup time\t\t\t\tDropoff time\t\t\tPassenger count\tTrip distance\tTotal amount\n'


def _add_ride(ride):
    if(len(ride.taxi_id) <= 3):
        return "".join([
        f"{ride.taxi_id}\t\t\t",
        f"{ride.pick_up_time.isoformat()}\t\t",
        f"{ride.drop_of_time.isoformat()}\t\t",
        f"{ride.passenger_count}\t\t\t\t",
        f"{ride.trip_distance}\t\t\t",
        f"{_format_amount(ride.tolls_amount, len(str(ride.trip_distance)))}",
        "\n"])
    else:
        return "".join([
            f"{ride.taxi_id}\t\t",
            f"{ride.pick_up_time.isoformat()}\t\t",
            f"{ride.drop_of_time.isoformat()}\t\t",
            f"{ride.passenger_count}\t\t\t\t",
            f"{ride.trip_distance}\t\t\t",
            f"{_format_amount(ride.tolls_amount, len(str(ride.trip_distance)))}",
            "\n"])
    


def _format_amount(amount, trip_distance_len):
    if(trip_distance_len <= 3):
        if amount < 0:
            return f"\t({amount})"
        return "\t" + str(amount)
    else:
        if amount < 0:
            return f"({amount})"
        return str(amount)
