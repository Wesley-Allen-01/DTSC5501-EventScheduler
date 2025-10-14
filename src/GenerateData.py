def generate_data(n):

    import random
    import string
    from datetime import datetime, timedelta
    
    # Assume Event class is already defined (as per your code)
    from Event import Event
    
    # Sample cities (expand as needed)
    cities = [
        "New York", "London", "Tokyo", "Paris", "Berlin", "Sydney", "Toronto", "Dubai",
        "Singapore", "Barcelona", "Rome", "Istanbul", "Bangkok", "Los Angeles", "Cape Town",
        "Seoul", "Moscow", "Mexico City", "Sao Paulo", "Mumbai"
    ]
    
    # Duration options with weight for bias
    durations = [15, 30, 60, 90, 120, 150]
    weights = [1, 5, 5, 2, 1, 1]  # Higher weight for 30 and 60 mins
    
    # Start and end date range
    start_date = datetime(2025, 8, 1)
    end_date = datetime(2027, 8, 1)
    
    # Helper to generate unique event titles like "Event A", "Event B", ..., "Event ZZ"
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
    
    # Helper to format time and date
    def format_time(dt):
        return dt.strftime("%H:%M")
    
    def format_date(dt):
        return dt.strftime("%Y-%m-%d")
    
    # Generate 10,000 unique events
    events = []
    for i in range(n):
        # Random date
        random_days = random.randint(0, (end_date - start_date).days)
        event_date = start_date + timedelta(days=random_days)
    
        # Duration
        duration = random.choices(durations, weights=weights, k=1)[0]
    
        # Start time: pick between 08:00 and 18:00 (to avoid ending too late)
        start_hour = random.randint(8, 18)
        start_minute = random.choice([0, 15, 30, 45])
        start_datetime = datetime.combine(event_date, datetime.min.time()) + timedelta(hours=start_hour, minutes=start_minute)
    
        # End time
        end_datetime = start_datetime + timedelta(minutes=duration)
        if end_datetime.hour >= 24:  # Avoid invalid time
            end_datetime = datetime.combine(event_date, datetime.min.time()) + timedelta(hours=23, minutes=59)
    
        # Title and location
        title = generate_event_title(i)
        location = random.choice(cities)
    
        # Create Event
        e = Event(
            id=i + 1,
            title=title,
            date=format_date(event_date),
            start_time=format_time(start_datetime),
            end_time=format_time(end_datetime),
            location=location
        )
    
        events.append(e)
    
    return events