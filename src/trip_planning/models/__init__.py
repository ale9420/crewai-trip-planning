"""
Pydantic models for trip planning application.

This module contains all the structured output models used by the CrewAI agents
to ensure consistent and validated data structures across the application.
"""

from .destination import DestinationInvestigation
from .flight import FlightOption, FlightSearchResults
from .accommodation import AccommodationOption, AccommodationSearchResults
from .transportation import (
    PublicTransportOption,
    CarRentalOption,
    RideSharingOption,
    TaxiServiceOption,
    AlternativeTransportOption,
    TouristTransportOption,
    TransportationSearchResults
)
from .attraction import (
    CulturalHistoricalAttraction,
    NaturalOutdoorAttraction,
    EntertainmentRecreationAttraction,
    LocalExperienceTour,
    SeasonalSpecialEvent,
    AttractionSearchResults
)
from .common import (
    TravelerType, 
    BudgetRange, 
    Location, 
    PriceInfo, 
    ContactInfo, 
    Review
)
from .dining import DiningOption, DiningSearchResults
from .itinerary import ItineraryActivity, ItineraryDay, StructuredItinerary
from .budget import CostBreakdownItem, VariableCostItem, FinalBudgetSummary
from .itinerary_validation import ValidationMetric, ItineraryIssue, ItineraryValidationReport
from .travel_document import TravelDocumentSection, EmergencyContact, ComprehensiveTravelDocument

__all__ = [
    # Destination models
    "DestinationInvestigation",
    
    # Flight models
    "FlightOption", 
    "FlightSearchResults",
    
    # Accommodation models
    "AccommodationOption",
    "AccommodationSearchResults",
    
    # Transportation models
    "PublicTransportOption",
    "CarRentalOption",
    "RideSharingOption",
    "TaxiServiceOption",
    "AlternativeTransportOption",
    "TouristTransportOption",
    "TransportationSearchResults",
    
    # Attraction models
    "CulturalHistoricalAttraction",
    "NaturalOutdoorAttraction",
    "EntertainmentRecreationAttraction",
    "LocalExperienceTour",
    "SeasonalSpecialEvent",
    "AttractionSearchResults",
    
    # Common models
    "TravelerType",
    "BudgetRange", 
    "Location", 
    "PriceInfo", 
    "ContactInfo", 
    "Review",
    
    # Dining models
    "DiningOption",
    "DiningSearchResults",
    
    # Itinerary models
    "ItineraryActivity",
    "ItineraryDay",
    "StructuredItinerary",
    
    # Budget models
    "CostBreakdownItem",
    "VariableCostItem",
    "FinalBudgetSummary",
    
    # Itinerary validation models
    "ValidationMetric",
    "ItineraryIssue",
    "ItineraryValidationReport",
    
    # Travel document models
    "TravelDocumentSection",
    "EmergencyContact",
    "ComprehensiveTravelDocument",
]
