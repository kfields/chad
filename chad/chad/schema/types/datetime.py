from ariadne import ScalarType
from datetime import datetime

# Serialize a datetime object to a string
def serialize_datetime(value):
    return value.isoformat()

# Parse a string to a datetime object
def parse_datetime(value):
    return datetime.fromisoformat(value)

datetime_scalar = ScalarType("DateTime", serializer=serialize_datetime, value_parser=parse_datetime)
