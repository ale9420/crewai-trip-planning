from pydantic import BaseModel, Field
from typing import List, Optional

class ItineraryActivity(BaseModel):
    name: str
    type: Optional[str] = None  # e.g., sightseeing, dining, transport
    start_time: Optional[str] = None  # e.g., '09:00'
    end_time: Optional[str] = None  # e.g., '11:00'
    location: Optional[str] = None
    cost: Optional[float] = None
    currency: Optional[str] = None
    instructions: Optional[str] = None
    notes: Optional[str] = None

class ItineraryDay(BaseModel):
    date: str  # e.g., '2025-08-19'
    activities: List[ItineraryActivity]
    total_cost: Optional[float] = None
    currency: Optional[str] = None
    special_instructions: Optional[str] = None

class StructuredItinerary(BaseModel):
    trip_title: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    days: List[ItineraryDay] = []
    overall_cost: Optional[float] = None
    currency: Optional[str] = None
    general_notes: Optional[str] = None
