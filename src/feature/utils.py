from datetime import datetime

def is_holiday(date):
    """ Determine if a given date is a holiday, Sunday, or Poya day """
    # List of fixed holidays (ensure the format is YYYY-MM-DD)
    holidays = {
        '2021-11-04',  # Deepavali
        '2021-12-25',  # Christmas Day
        '2022-01-01',  # New Year’s Day
        '2022-01-14',  # Tamil Thai Pongal Day
        '2021-11-19',  # November Poya (usually full moon)
        '2021-12-19',  # December Poya
        '2022-01-17',  # January Poya
        '2022-02-16',  # February Poya
        # Add more Poya days if needed
    }
    
    # Convert the date to string format
    date_str = date.strftime('%Y-%m-%d')
    
    # Check if the date is a holiday
    return date_str in holidays


