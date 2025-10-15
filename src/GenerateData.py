def create_event_dataset(n: int, type: str):
    import random
    import string
    from datetime import datetime, timedelta
    from Event import Event
    from ArrayList import ArrayList
    from LinkedList import LinkedList
    
    # arbitrary locations to choose from
    cities = [
        "New York","London", "Tokyo", "Paris", "Berlin", "Sydney","Toronto", "Dubai",
        "Singapore", "Barcelona", "Rome","Istanbul", "Bangkok", "Los Angeles", "Cape Town",
        "Seoul","Moscow", "Mexico City", "Sao Paulo", "Mumbai", 'Kyoto', 'Osaka', 'New Orleans',
        "Amsterdam", 'Copenhagen', "Kiev"
    ]

    # event duration, weighted to favor 30- and 60-minutes
    durations = [15, 30, 60, 90, 120, 150, 180]
    weights = [1, 5, 5, 2, 1, 2, 1]

    # possible data range
    start_date = datetime(2025, 8, 1)
    end_date = datetime(2029, 8, 1)

    # name events like excel columns
    def generate_event_title(index):
        letters = string.ascii_uppercase
        title = ""
        while True:
            index, rem = divmod(index, 26)
            title = letters[rem] + title
            if index == 0:
                break
            index -= 1
        return f"Event {title}"

    def format_time(dt):
        return dt.strftime("%H:%M")

    def format_date(dt):
        return dt.strftime("%Y-%m-%d")

    # pick Array or LinkedList
    if type not in ["array", "ll"]:
        raise ValueError("Invalid type. Must be 'array' or 'll'")

    container = ArrayList() if type == "array" else LinkedList()

    # make events
    for i in range(n):
        # Random date
        days_offset = random.randint(0, (end_date - start_date).days)
        event_date = start_date + timedelta(days=days_offset)

        # Duration
        duration = random.choices(durations, weights=weights, k=1)[0]

        # Start time between 08:00 and 19:00
        start_hour = random.randint(8, 19)
        start_minute = random.choice([0, 15, 30, 45])
        start_dt = datetime.combine(event_date, datetime.min.time()) + timedelta(
            hours=start_hour, minutes=start_minute)

        # End time (max 23:59)
        end_dt = start_dt + timedelta(minutes=duration)
        if end_dt.hour >= 24:
            end_dt = datetime.combine(event_date, datetime.min.time()) + timedelta(hours=23, minutes=59)

        # Create Event
        event = Event(
            id=i + 1,
            title=generate_event_title(i),
            date=format_date(event_date),
            start_time=format_time(start_dt),
            end_time=format_time(end_dt),
            location=random.choice(cities),
        )

        container.insert(event)

    return container
