"""
Pydantic models for trip planning application.

This module contains all the structured output models used by the CrewAI agents
to ensure consistent and validated data structures across the application.
"""

from .destination import DestinationInvestigation
from .flight import FlightOption, FlightSearchResults
from .accommodation import AccommodationOption, AccommodationSearchResults
from .common import (
    TravelerType, 
    BudgetRange, 
    Location, 
    PriceInfo, 
    ContactInfo, 
    Review
)

__all__ = [
    # Destination models
    "DestinationInvestigation",
    
    # Flight models
    "FlightOption", 
    "FlightSearchResults",
    
    # Accommodation models
    "AccommodationOption",
    "AccommodationSearchResults",
    
    # Common models
    "TravelerType",
    "BudgetRange", 
    "Location", 
    "PriceInfo", 
    "ContactInfo", 
    "Review"
]
