"""
Accommodation-related Pydantic models for trip planning.

This module contains models for accommodation search results and individual accommodation options
that agents use to provide comprehensive lodging information and recommendations.
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from .common import PriceInfo, Location, Review, ContactInfo


class AccommodationAmenities(BaseModel):
    """Detailed amenities information for accommodation."""
    essential: List[str] = Field(description="Essential amenities (WiFi, AC, private bathroom, etc.)")
    comfort: List[str] = Field(description="Comfort amenities (pool, gym, spa, restaurant, etc.)")
    convenience: List[str] = Field(description="Convenience amenities (airport shuttle, parking, laundry, etc.)")
    safety: List[str] = Field(description="Safety features (24/7 front desk, security cameras, etc.)")
    accessibility: List[str] = Field(description="Accessibility features for travelers with disabilities")
    family: List[str] = Field(description="Family-friendly amenities (cribs, kids' activities, etc.)")
    business: List[str] = Field(description="Business amenities (work desk, meeting rooms, etc.)")


class RoomConfiguration(BaseModel):
    """Room type and configuration details."""
    room_type: str = Field(description="Type of room (standard, deluxe, suite, etc.)")
    bed_configuration: str = Field(description="Bed sizes and arrangement")
    max_occupancy: int = Field(description="Maximum number of guests")
    bathroom_type: str = Field(description="Private or shared bathroom")
    special_features: List[str] = Field(description="Special features (balcony, view, kitchen, etc.)")
    square_meters: Optional[float] = Field(description="Room size in square meters")


class LocationDetails(BaseModel):
    """Detailed location and neighborhood information."""
    address: str = Field(description="Full address")
    neighborhood: str = Field(description="Neighborhood name and description")
    safety_rating: float = Field(description="Safety rating out of 5")
    walkability_score: float = Field(description="Walkability score out of 5")
    distance_to_attractions: Dict[str, str] = Field(description="Distance to major attractions")
    distance_to_transport: Dict[str, str] = Field(description="Distance to transportation hubs")
    nearby_amenities: List[str] = Field(description="Nearby restaurants, shops, and services")
    noise_level: str = Field(description="Expected noise levels (quiet, moderate, busy)")


class BookingInformation(BaseModel):
    """Booking and payment details."""
    total_price: PriceInfo = Field(description="Total price for the entire stay")
    price_breakdown: Dict[str, PriceInfo] = Field(description="Breakdown of costs (base rate, taxes, fees)")
    cancellation_policy: str = Field(description="Cancellation and refund policies")
    payment_methods: List[str] = Field(description="Accepted payment methods")
    deposit_required: Optional[PriceInfo] = Field(description="Required deposit amount")
    check_in_time: str = Field(description="Check-in time")
    check_out_time: str = Field(description="Check-out time")
    booking_channels: List[str] = Field(description="Recommended booking channels")
    best_booking_timing: str = Field(description="Optimal timing for booking")


class AccommodationOption(BaseModel):
    """
    Detailed information for a single accommodation option.
    
    This model captures comprehensive accommodation information to help travelers make informed decisions
    based on their specific needs, budget, and preferences.
    """
    # Basic Information
    name: str = Field(description="Accommodation name and brand")
    type: str = Field(description="Type of accommodation (hotel, resort, vacation rental, hostel)")
    star_rating: Optional[int] = Field(description="Official star rating (1-5)")
    guest_score: float = Field(description="Guest rating out of 5")
    
    # Location and Neighborhood
    location: LocationDetails = Field(description="Detailed location information")
    
    # Pricing and Booking
    booking_info: BookingInformation = Field(description="Booking and payment details")
    
    # Room and Amenities
    room_configurations: List[RoomConfiguration] = Field(description="Available room types and configurations")
    amenities: AccommodationAmenities = Field(description="Comprehensive amenities information")
    
    # Property Features
    property_features: List[str] = Field(description="On-site facilities and services")
    environmental_initiatives: List[str] = Field(description="Environmental sustainability practices")
    
    # Guest Experience
    reviews: Review = Field(description="Guest reviews and ratings")
    staff_quality: str = Field(description="Staff friendliness and service quality")
    cleanliness_rating: float = Field(description="Cleanliness rating out of 5")
    maintenance_quality: str = Field(description="Property maintenance standards")
    atmosphere: str = Field(description="Overall atmosphere and vibe")
    cultural_authenticity: str = Field(description="Cultural authenticity and local experience")
    
    # Practical Information
    contact_info: ContactInfo = Field(description="Contact information")
    airport_transfer: Optional[str] = Field(description="Airport transfer options and costs")
    parking_info: Optional[str] = Field(description="Parking availability and fees")
    pet_policy: Optional[str] = Field(description="Pet-friendly policies if applicable")
    covid_protocols: List[str] = Field(description="COVID-19 protocols and cleaning standards")
    
    # Special Considerations
    loyalty_program: Optional[str] = Field(description="Loyalty program benefits if applicable")
    special_packages: List[str] = Field(description="Special packages or promotions")
    seasonal_variations: Optional[str] = Field(description="Seasonal price variations")


class AccommodationRecommendations(BaseModel):
    """Specific recommendations by traveler type and preferences."""
    best_value_options: List[str] = Field(default_factory=list, description="Top 3 value-for-money options")
    best_for_families: Optional[str] = Field(default=None, description="Best option for families with children")
    best_for_business: Optional[str] = Field(default=None, description="Best option for business travelers")
    best_for_budget: Optional[str] = Field(default=None, description="Best option for budget-conscious travelers")
    best_for_luxury: Optional[str] = Field(default=None, description="Best option for luxury seekers")
    best_for_cultural_immersion: Optional[str] = Field(default=None, description="Best option for cultural immersion")
    alternative_neighborhoods: List[str] = Field(default_factory=list, description="Alternative neighborhoods to consider")


class LocationInsights(BaseModel):
    """Comprehensive location and neighborhood insights."""
    neighborhood_safety: Dict[str, float] = Field(default_factory=dict, description="Safety ratings by neighborhood")
    proximity_analysis: Dict[str, List[str]] = Field(default_factory=dict, description="Proximity to attractions and transport")
    dining_options: Dict[str, List[str]] = Field(default_factory=dict, description="Local dining options by area")
    shopping_districts: List[str] = Field(default_factory=list, description="Shopping districts and areas")
    cultural_districts: List[str] = Field(default_factory=list, description="Cultural and entertainment districts")
    transportation_hubs: List[str] = Field(default_factory=list, description="Major transportation hubs and accessibility")


class AccommodationSearchResults(BaseModel):
    """
    Comprehensive accommodation search results.
    
    This model provides a complete overview of available accommodation options with pricing analysis,
    recommendations, and important considerations for travelers.
    """
    # Search Summary
    search_summary: Optional[Dict[str, str]] = Field(default_factory=dict, description="Summary of search results and criteria")
    total_options_found: int = Field(default=0, description="Total number of accommodation options found")
    price_range: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Price range (lowest to highest)")
    location_highlights: List[str] = Field(default_factory=list, description="Key areas and neighborhoods")
    
    # Detailed Options
    accommodation_options: List[AccommodationOption] = Field(default_factory=list, description="List of detailed accommodation options")
    
    # Recommendations
    recommendations: Optional[AccommodationRecommendations] = Field(default=None, description="Specific recommendations by traveler type")
    
    # Location Insights
    location_insights: Optional[LocationInsights] = Field(default=None, description="Comprehensive location and neighborhood insights")
    
    # Additional Information
    booking_tips: List[str] = Field(default_factory=list, description="Best practices for booking accommodation")
    seasonal_considerations: List[str] = Field(default_factory=list, description="Seasonal price variations and availability")
    important_notes: List[str] = Field(default_factory=list, description="Important warnings, advisories, or restrictions")
    upcoming_events: List[str] = Field(default_factory=list, description="Upcoming events that may affect availability")
    loyalty_program_benefits: List[str] = Field(default_factory=list, description="Loyalty program benefits and recommendations")
    special_promotions: List[str] = Field(default_factory=list, description="Special packages or promotions available")
