from dataclasses import dataclass

@dataclass
class Article():
    """A class holding article data"""

    type_of: str
    id: str
    title: str
    description: str
    readable_publish_date: str
    url: str
    published_timestamp: int
    created_at: str
    published_at: str
    reading_time_minutes: int

