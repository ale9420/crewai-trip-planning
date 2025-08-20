"""
Attraction-related Pydantic models for trip planning.

This module contains models for attraction search results and individual attraction options
that agents use to provide comprehensive local attraction and activity information and recommendations.
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from .common import PriceInfo, ContactInfo, Review


class CulturalHistoricalAttraction(BaseModel):
    """
    Detailed information for cultural and historical attractions including museums, landmarks, and heritage sites.
    
    This model captures comprehensive cultural and historical attraction information to help travelers
    understand local heritage and cultural significance.
    """
    attraction_name: Optional[str] = Field(
        default=None,
        description="Name of the cultural or historical attraction"
    )
    attraction_type: Optional[str] = Field(
        default=None,
        description="Type of attraction (museum, gallery, monument, archaeological site, etc.)"
    )
    cultural_significance: Optional[str] = Field(
        default=None,
        description="Cultural and historical significance of the attraction"
    )
    historical_background: Optional[str] = Field(
        default=None,
        description="Historical background and context of the attraction"
    )
    unesco_status: Optional[str] = Field(
        default=None,
        description="UNESCO World Heritage status or other special designations"
    )
    address: Optional[str] = Field(
        default=None,
        description="Full address and location description"
    )
    visitor_rating: Optional[float] = Field(
        default=None,
        description="Visitor rating out of 5 stars"
    )
    review_count: Optional[int] = Field(
        default=None,
        description="Number of reviews"
    )
    opening_hours: Optional[str] = Field(
        default=None,
        description="Opening hours and days of operation"
    )
    seasonal_availability: Optional[str] = Field(
        default=None,
        description="Seasonal availability and any closures"
    )
    admission_fees: Optional[Dict[str, Any]] = Field(
        default_factory=dict,
        description="Admission fees and pricing structure by visitor type"
    )
    advance_booking: Optional[str] = Field(
        default=None,
        description="Advance booking requirements and time slots"
    )
    visit_duration: Optional[str] = Field(
        default=None,
        description="Typical duration of visit"
    )
    peak_times: Optional[str] = Field(
        default=None,
        description="Peak visiting times and crowd management"
    )
    guided_tours: Optional[List[str]] = Field(
        default_factory=list,
        description="Available guided tour options and costs"
    )
    interactive_elements: List[str] = Field(
        default_factory=list,
        description="Interactive elements and hands-on activities"
    )
    photography_policy: Optional[str] = Field(
        default=None,
        description="Photography policies and restrictions"
    )
    accessibility_features: List[str] = Field(
        default_factory=list,
        description="Accessibility features including wheelchair access, audio guides, etc."
    )
    family_friendly_features: List[str] = Field(
        default_factory=list,
        description="Family-friendly features and child-appropriate activities"
    )
    amenities: List[str] = Field(
        default_factory=list,
        description="Available amenities (restrooms, dining, gift shops, etc.)"
    )
    contact_info: Optional[ContactInfo] = Field(
        default=None,
        description="Contact information for the attraction"
    )


class NaturalOutdoorAttraction(BaseModel):
    """
    Detailed information for natural and outdoor attractions including parks, beaches, and nature reserves.
    
    This model captures comprehensive natural and outdoor attraction information for travelers
    who enjoy nature and outdoor activities.
    """
    attraction_name: Optional[str] = Field(
        default=None,
        description="Name of the natural or outdoor attraction"
    )
    attraction_type: Optional[str] = Field(
        default=None,
        description="Type of attraction (national park, beach, mountain, botanical garden, etc.)"
    )
    natural_features: List[str] = Field(
        default_factory=list,
        description="Key natural features and highlights"
    )
    scenic_highlights: List[str] = Field(
        default_factory=list,
        description="Scenic viewpoints and photo opportunities"
    )
    address: Optional[str] = Field(
        default=None,
        description="Location and access information"
    )
    visitor_rating: Optional[float] = Field(
        default=None,
        description="Visitor rating out of 5 stars"
    )
    review_count: Optional[int] = Field(
        default=None,
        description="Number of reviews"
    )
    operating_hours: Optional[str] = Field(
        default=None,
        description="Operating hours and seasonal availability"
    )
    weather_considerations: Optional[str] = Field(
        default=None,
        description="Weather impact and best times to visit"
    )
    admission_fees: Optional[Dict[str, Any]] = Field(
        default_factory=dict,
        description="Admission fees and pricing structure"
    )
    hiking_trails: List[str] = Field(
        default_factory=list,
        description="Available hiking trails and difficulty levels"
    )
    outdoor_activities: List[str] = Field(
        default_factory=list,
        description="Available outdoor activities and sports"
    )
    wildlife_information: Optional[str] = Field(
        default=None,
        description="Wildlife viewing opportunities and safety information"
    )
    photography_opportunities: List[str] = Field(
        default_factory=list,
        description="Best photography spots and optimal times"
    )
    accessibility_features: List[str] = Field(
        default_factory=list,
        description="Accessibility features and limitations"
    )
    family_friendly_features: List[str] = Field(
        default_factory=list,
        description="Family-friendly features and activities"
    )
    safety_information: List[str] = Field(
        default_factory=list,
        description="Safety considerations and precautions"
    )
    amenities: List[str] = Field(
        default_factory=list,
        description="Available amenities (restrooms, picnic areas, etc.)"
    )
    contact_info: Optional[ContactInfo] = Field(
        default=None,
        description="Contact information for the attraction"
    )


class EntertainmentRecreationAttraction(BaseModel):
    """
    Detailed information for entertainment and recreation attractions including theme parks, sports venues, and shopping.
    
    This model captures comprehensive entertainment and recreation information for travelers
    seeking fun and engaging activities.
    """
    attraction_name: Optional[str] = Field(
        default=None,
        description="Name of the entertainment or recreation attraction"
    )
    attraction_type: Optional[str] = Field(
        default=None,
        description="Type of attraction (theme park, sports venue, shopping district, etc.)"
    )
    entertainment_highlights: List[str] = Field(
        default_factory=list,
        description="Key entertainment features and attractions"
    )
    address: Optional[str] = Field(
        default=None,
        description="Location and access information"
    )
    visitor_rating: Optional[float] = Field(
        default=None,
        description="Visitor rating out of 5 stars"
    )
    review_count: Optional[int] = Field(
        default=None,
        description="Number of reviews"
    )
    operating_hours: Optional[str] = Field(
        default=None,
        description="Operating hours and seasonal availability"
    )
    admission_fees: Optional[Dict[str, Any]] = Field(
        default_factory=dict,
        description="Admission fees and pricing structure"
    )
    age_restrictions: Optional[str] = Field(
        default=None,
        description="Age restrictions and suitability"
    )
    thrill_level: Optional[str] = Field(
        default=None,
        description="Thrill level and intensity of activities"
    )
    family_friendly_features: List[str] = Field(
        default_factory=list,
        description="Family-friendly features and child-appropriate activities"
    )
    accessibility_features: List[str] = Field(
        default_factory=list,
        description="Accessibility features and accommodations"
    )
    food_beverage_options: List[str] = Field(
        default_factory=list,
        description="Food and beverage options available"
    )
    shopping_options: List[str] = Field(
        default_factory=list,
        description="Shopping options and retail experiences"
    )
    special_events: List[str] = Field(
        default_factory=list,
        description="Special events and seasonal programming"
    )
    peak_times: Optional[str] = Field(
        default=None,
        description="Peak visiting times and crowd management"
    )
    contact_info: Optional[ContactInfo] = Field(
        default=None,
        description="Contact information for the attraction"
    )


class LocalExperienceTour(BaseModel):
    """
    Detailed information for local experiences and tours including guided tours, workshops, and cultural experiences.
    
    This model captures comprehensive local experience information for travelers
    seeking authentic and immersive cultural experiences.
    """
    experience_name: Optional[str] = Field(
        default=None,
        description="Name of the local experience or tour"
    )
    experience_type: Optional[str] = Field(
        default=None,
        description="Type of experience (guided tour, workshop, cultural experience, etc.)"
    )
    experience_description: Optional[str] = Field(
        default=None,
        description="Detailed description of the experience"
    )
    cultural_focus: Optional[str] = Field(
        default=None,
        description="Cultural focus and authenticity of the experience"
    )
    meeting_point: Optional[str] = Field(
        default=None,
        description="Meeting point and location information"
    )
    duration: Optional[str] = Field(
        default=None,
        description="Duration of the experience"
    )
    group_size: Optional[str] = Field(
        default=None,
        description="Group size and capacity"
    )
    pricing: Optional[Dict[str, Any]] = Field(
        default_factory=dict,
        description="Pricing structure and what's included"
    )
    booking_requirements: Optional[str] = Field(
        default=None,
        description="Booking requirements and advance notice needed"
    )
    language_options: List[str] = Field(
        default_factory=list,
        description="Available language options for tours"
    )
    guide_qualifications: Optional[str] = Field(
        default=None,
        description="Guide qualifications and expertise"
    )
    interactive_elements: List[str] = Field(
        default_factory=list,
        description="Interactive elements and hands-on activities"
    )
    accessibility_features: List[str] = Field(
        default_factory=list,
        description="Accessibility features and accommodations"
    )
    family_friendly_features: List[str] = Field(
        default_factory=list,
        description="Family-friendly features and age suitability"
    )
    what_to_bring: List[str] = Field(
        default_factory=list,
        description="What to bring and preparation needed"
    )
    cancellation_policy: Optional[str] = Field(
        default=None,
        description="Cancellation policy and refund information"
    )
    contact_info: Optional[ContactInfo] = Field(
        default=None,
        description="Contact information for the experience provider"
    )


class SeasonalSpecialEvent(BaseModel):
    """
    Detailed information for seasonal attractions and special events including festivals and limited-time experiences.
    
    This model captures comprehensive seasonal and special event information for travelers
    seeking unique and time-sensitive experiences.
    """
    event_name: Optional[str] = Field(
        default=None,
        description="Name of the seasonal attraction or special event"
    )
    event_type: Optional[str] = Field(
        default=None,
        description="Type of event (festival, exhibition, seasonal activity, etc.)"
    )
    event_description: Optional[str] = Field(
        default=None,
        description="Detailed description of the event"
    )
    dates: Optional[str] = Field(
        default=None,
        description="Event dates and duration"
    )
    location: Optional[str] = Field(
        default=None,
        description="Event location and venue information"
    )
    cultural_significance: Optional[str] = Field(
        default=None,
        description="Cultural significance and historical background"
    )
    visitor_rating: Optional[float] = Field(
        default=None,
        description="Visitor rating out of 5 stars"
    )
    review_count: Optional[int] = Field(
        default=None,
        description="Number of reviews"
    )
    admission_fees: Optional[Dict[str, Any]] = Field(
        default_factory=dict,
        description="Admission fees and pricing structure"
    )
    booking_requirements: Optional[str] = Field(
        default=None,
        description="Booking requirements and advance purchase recommendations"
    )
    highlights: List[str] = Field(
        default_factory=list,
        description="Key highlights and must-see elements"
    )
    activities: List[str] = Field(
        default_factory=list,
        description="Available activities and experiences"
    )
    family_friendly_features: List[str] = Field(
        default_factory=list,
        description="Family-friendly features and activities"
    )
    accessibility_features: List[str] = Field(
        default_factory=list,
        description="Accessibility features and accommodations"
    )
    weather_considerations: Optional[str] = Field(
        default=None,
        description="Weather considerations and backup plans"
    )
    crowd_management: Optional[str] = Field(
        default=None,
        description="Crowd management and peak times"
    )
    contact_info: Optional[ContactInfo] = Field(
        default=None,
        description="Contact information for the event organizers"
    )


class AttractionSearchResults(BaseModel):
    """
    Comprehensive attraction search results containing all local attraction and activity options.
    
    This model provides a complete overview of available attractions and activities with detailed
    analysis, recommendations, and important considerations for travelers. All information should be
    tailored to the specific travel requirements and preferences provided in the task context.
    """
    search_summary: Optional[Dict[str, Any]] = Field(
        default_factory=dict,
        description="Summary statistics including total attractions found, price ranges, "
                   "and top-rated highlights. Include currency and search criteria used."
    )
    cultural_historical_attractions: List[CulturalHistoricalAttraction] = Field(
        default_factory=list,
        description="Cultural and historical attractions including museums, landmarks, and heritage sites"
    )
    natural_outdoor_attractions: List[NaturalOutdoorAttraction] = Field(
        default_factory=list,
        description="Natural and outdoor attractions including parks, beaches, and nature reserves"
    )
    entertainment_recreation_attractions: List[EntertainmentRecreationAttraction] = Field(
        default_factory=list,
        description="Entertainment and recreation attractions including theme parks and sports venues"
    )
    local_experience_tours: List[LocalExperienceTour] = Field(
        default_factory=list,
        description="Local experiences and tours including guided tours and cultural workshops"
    )
    seasonal_special_events: List[SeasonalSpecialEvent] = Field(
        default_factory=list,
        description="Seasonal attractions and special events during travel dates"
    )
    recommendations: Optional[Dict[str, Any]] = Field(
        default_factory=dict,
        description="Specific recommendations including best attractions for different traveler types, "
                   "budget considerations, and accessibility needs. Include reasoning for each recommendation."
    )
    budget_friendly_options: List[str] = Field(
        default_factory=list,
        description="Free and low-cost attractions and activities"
    )
    premium_experiences: List[str] = Field(
        default_factory=list,
        description="Premium and luxury experiences worth considering"
    )
    accessibility_highlights: List[str] = Field(
        default_factory=list,
        description="Fully accessible attractions and special needs accommodations"
    )
    family_friendly_highlights: List[str] = Field(
        default_factory=list,
        description="Best attractions for families with children"
    )
    must_see_attractions: List[str] = Field(
        default_factory=list,
        description="Must-see attractions and cultural highlights"
    )
    hidden_gems: List[str] = Field(
        default_factory=list,
        description="Hidden gems and off-the-beaten-path attractions"
    )
    combination_opportunities: List[str] = Field(
        default_factory=list,
        description="Attractions that can be combined for efficient visiting"
    )
    seasonal_considerations: List[str] = Field(
        default_factory=list,
        description="Seasonal considerations and weather-dependent activities"
    )
    practical_tips: List[str] = Field(
        default_factory=list,
        description="Practical tips for visiting attractions"
    )
    booking_advice: List[str] = Field(
        default_factory=list,
        description="Booking advice and advance purchase recommendations"
    )
    photography_tips: List[str] = Field(
        default_factory=list,
        description="Photography tips and best viewpoints"
    )
    local_customs: List[str] = Field(
        default_factory=list,
        description="Local customs and respectful behavior guidelines"
    )
    emergency_information: List[str] = Field(
        default_factory=list,
        description="Emergency contact information and procedures"
    )
