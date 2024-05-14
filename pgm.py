def calculate_actual_time(initial_time, seconds_gained_per_interval, minutes_early):
    # Convert the initial time to seconds
    initial_time_seconds = sum(int(t) * 60 ** i for i, t in enumerate(reversed(initial_time.split(':'))))

    # Calculate the total seconds gained
    total_seconds_gained = (seconds_gained_per_interval / 5) * (60 * 5)

    # Calculate the actual time X reached the venue in seconds
    actual_time_seconds = initial_time_seconds + total_seconds_gained - (minutes_early * 60)

    # Convert the actual time back to 24-hour format HH:MM:SS
    actual_hours = (actual_time_seconds // 3600) % 24
    actual_time = "{:02}:{:02}:{:02}".format(
        int(actual_hours),
        (actual_time_seconds % 3600) // 60,
        actual_time_seconds % 60
    )

    return actual_time

# Example usage:
initial_time = "08:00:00"
seconds_gained_per_interval = 2
minutes_early = 5

result = calculate_actual_time(initial_time, seconds_gained_per_interval, minutes_early)
print("Actual time X reached the interview venue:", result)

