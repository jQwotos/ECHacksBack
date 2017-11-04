from datetime import datetime

def convert_string_to_date(string):
    return datetime.strptime(
        string,
        '%b %d, %Y')
