"""
Accommodation-related Pydantic models for trip planning.

This module contains models for accommodation search results and individual accommodation options
that agents use to provide comprehensive lodging information and recommendations.
"""

from pydantic import BaseModel, Field
from typing import Optional


class AccommodationOption(BaseModel):
    """
    Detailed information for a single accommodation option.
    
    This model captures comprehensive accommodation information to help travelers make informed decisions
    based on their specific needs, budget, and preferences.
    """
    name: str = Field(description="Accommodation name and brand")
    type: str = Field(description="Type of accommodation (hotel, hostel, apartment, etc.)")
    location: str = Field(description="Address and neighborhood information")
    price_per_night: float = Field(description="Price per night in local currency")
    total_price: float = Field(description="Total price for the entire stay")
    rating: float = Field(description="Average rating out of 5 stars")
    amenities: list[str] = Field(description="Available amenities and services")
    room_types: list[str] = Field(description="Available room types and configurations")
    cancellation_policy: str = Field(description="Cancellation and refund policies")
    check_in_time: str = Field(description="Check-in and check-out times")
    distance_from_attractions: dict[str, str] = Field(description="Distance to major attractions")
    transportation_access: list[str] = Field(description="Nearby public transportation options")
    parking_availability: Optional[str] = Field(description="Parking options and costs")
    pet_policy: Optional[str] = Field(description="Pet-friendly policies if applicable")
    accessibility_features: list[str] = Field(description="Accessibility features for travelers with disabilities")


class AccommodationSearchResults(BaseModel):
    """
    Comprehensive accommodation search results.
    
    This model provides a complete overview of available accommodation options with pricing analysis,
    recommendations, and important considerations for travelers.
    """
    search_summary: dict[str, str] = Field(description="Summary of search results and criteria")
    accommodation_options: list[AccommodationOption] = Field(description="List of accommodation options")
    recommendations: dict[str, str] = Field(description="Specific recommendations by traveler type")
    neighborhood_guide: list[str] = Field(description="Information about different neighborhoods")
    booking_tips: list[str] = Field(description="Best practices for booking accommodation")
    seasonal_considerations: list[str] = Field(description="Seasonal price variations and availability")
