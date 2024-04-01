from math import radians, cos, sin, asin, sqrt


# formula borrowed from: https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
def haversine(
    start_lng: float, start_lat: float, end_lng: float, end_lat: float
) -> float | None:
    """
    Calculate the great circle distance in kilometers between two points
    on the earth (specified in decimal degrees)
    """
    if start_lng and start_lat and end_lng and end_lat:
        # convert decimal degrees to radians
        start_lng, start_lat, end_lng, end_lat = map(
            radians, [start_lng, start_lat, end_lng, end_lat]
        )

        # haversine formula
        dlon = end_lng - start_lng
        dlat = end_lat - start_lat
        a = sin(dlat / 2) ** 2 + cos(start_lat) * cos(end_lat) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 6371  # Radius of earth in kilometers.
        return c * r
    else:
        return None


def get_distance_bucket(distance: float) -> float:
    """
    based on a given distance, return the corresponding bucket given in the assignment
    """
    if distance is None:
        return "n/a"
    elif distance < 1:
        return "[0, 1)"
    elif distance >= 1 and distance < 4:
        return "[1, 4)"
    elif distance >= 4 and distance < 10:
        return "[4, 10)"
    else:
        return "[10, inf)"
