from pydantic import BaseModel, Field
from typing import List, Optional

class DiningOption(BaseModel):
    name: str
    type: str  # e.g., restaurant, cafe, street food
    cuisine: Optional[str] = None
    price_range: Optional[str] = None  # e.g., $-$$$
    rating: Optional[float] = None
    address: Optional[str] = None
    distance_to_attractions: Optional[str] = None
    menu_highlights: Optional[List[str]] = None
    reservation_required: Optional[bool] = None
    photos: Optional[List[str]] = None  # URLs or file paths
    reviews: Optional[List[str]] = None
    covid_protocols: Optional[str] = None
    special_features: Optional[List[str]] = None  # e.g., vegan, gluten-free, live music

class DiningSearchResults(BaseModel):
    summary: str
    total_options_found: int
    price_range: Optional[str] = None
    best_value_options: Optional[List[str]] = None  # Names or IDs
    location_highlights: Optional[List[str]] = None
    dining_options: List[DiningOption]
    recommendations: Optional[List[str]] = None  # e.g., best for families, business, budget
    location_insights: Optional[List[str]] = None  # e.g., safety, proximity, local districts
    important_notes: Optional[List[str]] = None
    photos: Optional[List[str]] = None  # URLs or file paths
    menu_highlights: Optional[List[str]] = None
