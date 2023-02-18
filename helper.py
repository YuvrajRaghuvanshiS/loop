from datetime import datetime
import pytz


class Helper:
    @classmethod
    def utc_to_local(
        cls, utc_time_str: str, timezone_str: str = "America/Chicago"
    ) -> tuple[int, str]:
        # Parse the UTC time string into a datetime object
        utc_time = datetime.strptime(utc_time_str, "%Y-%m-%d %H:%M:%S.%f UTC")

        # Create a timezone object for the specified timezone
        local_tz = pytz.timezone(timezone_str)

        # Convert the UTC time to the local time
        local_time = utc_time.replace(tzinfo=pytz.utc).astimezone(local_tz)

        # Get the day of the week as an integer (where Monday = 0, Tuesday = 1, and so on)
        day_of_week = local_time.weekday()

        # Format the local time as a string in the format HH:MM:SS
        local_time_str = local_time.strftime("%H:%M:%S")

        return day_of_week, local_time_str
