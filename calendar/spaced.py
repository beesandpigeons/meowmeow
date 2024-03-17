from datetime import datetime, timedelta

def calculate_next_review_date(last_review_date, difficulty_level):
    # Define intervals for spaced repetition, up to 410 days
    intervals = [1, 2, 4, 7, 15, 30, 60, 120, 240, 410]

    # Make sure the difficulty level is within the valid range
    difficulty_level = min(difficulty_level, len(intervals) - 1)

    # Calculate the next review interval based on the difficulty level
    next_interval = intervals[difficulty_level]

    # Calculate the next review date
    next_review_date = last_review_date + timedelta(days=next_interval)

    return next_review_date

# Example usage
last_review_date = datetime.now()
difficulty_level = 8  # Assuming difficulty level is between 0 and 9
next_review_date = calculate_next_review_date(last_review_date, difficulty_level)

print(f"Last review date: {last_review_date}")
print(f"Next review date: {next_review_date}")