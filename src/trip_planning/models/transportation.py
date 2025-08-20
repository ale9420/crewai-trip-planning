"""
Transportation-related Pydantic models for trip planning.

This module contains models for transportation search results and individual transportation options
that agents use to provide comprehensive local transportation information and recommendations.
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from .common import PriceInfo, ContactInfo, Review


class PublicTransportOption(BaseModel):
    """
    Detailed information for public transportation options including metro, buses, and regional transport.
    
    This model captures comprehensive public transit information to help travelers understand
    local transportation networks and make informed decisions about getting around.
    """
    transport_type: Optional[str] = Field(
        default=None,
        description="Type of public transportation (metro, bus, tram, light rail, regional train, etc.)"
    )
    network_name: Optional[str] = Field(
        default=None,
        description="Name of the transportation network or system"
    )
    coverage_area: Optional[str] = Field(
        default=None,
        description="Geographic coverage area and key destinations served"
    )
    operating_hours: Optional[str] = Field(
        default=None,
        description="Operating hours including peak and off-peak service times"
    )
    frequency: Optional[str] = Field(
        default=None,
        description="Service frequency during peak and off-peak hours"
    )
    fare_structure: Optional[Dict[str, Any]] = Field(
        default_factory=dict,
        description="Fare information including single fares, day passes, weekly/monthly passes"
    )
    payment_methods: List[str] = Field(
        default_factory=list,
        description="Accepted payment methods (cash, card, mobile app, contactless, etc.)"
    )
    accessibility_features: List[str] = Field(
        default_factory=list,
        description="Accessibility features including wheelchair access, audio announcements, etc."
    )
    key_stations: List[str] = Field(
        default_factory=list,
        description="Major stations and transfer points"
    )
    tourist_friendly_features: List[str] = Field(
        default_factory=list,
        description="Features helpful for tourists (English signage, tourist passes, etc.)"
    )
    safety_rating: Optional[float] = Field(
        default=None,
        description="Safety rating out of 5 stars based on crime statistics and user reviews"
    )
    reliability_score: Optional[float] = Field(
        default=None,
        description="Reliability score based on on-time performance and service consistency"
    )
    peak_hours: Optional[str] = Field(
        default=None,
        description="Peak hours to avoid and off-peak recommendations"
    )
    night_service: Optional[str] = Field(
        default=None,
        description="Night bus or late-night service availability and schedules"
    )
    contact_info: Optional[ContactInfo] = Field(
        default=None,
        description="Contact information for the transportation service"
    )


class CarRentalOption(BaseModel):
    """
    Detailed information for car rental services including pricing, requirements, and policies.
    
    This model captures comprehensive car rental information to help travelers understand
    driving options, costs, and requirements for their destination.
    """
    company_name: Optional[str] = Field(
        default=None,
        description="Car rental company name and any local partnerships"
    )
    vehicle_types: List[str] = Field(
        default_factory=list,
        description="Available vehicle types (economy, compact, SUV, luxury, etc.)"
    )
    daily_rates: Optional[Dict[str, float]] = Field(
        default_factory=dict,
        description="Daily rental rates by vehicle type"
    )
    insurance_options: List[str] = Field(
        default_factory=list,
        description="Available insurance options and coverage details"
    )
    insurance_costs: Optional[Dict[str, float]] = Field(
        default_factory=dict,
        description="Daily insurance costs by coverage type"
    )
    fuel_policy: Optional[str] = Field(
        default=None,
        description="Fuel policy (full-to-full, pre-paid, etc.) and fuel costs"
    )
    mileage_limits: Optional[str] = Field(
        default=None,
        description="Daily mileage limits and additional mileage costs"
    )
    driving_requirements: List[str] = Field(
        default_factory=list,
        description="Driving license requirements, age restrictions, and experience needed"
    )
    pickup_locations: List[str] = Field(
        default_factory=list,
        description="Pickup and drop-off locations including airports and city centers"
    )
    additional_fees: List[str] = Field(
        default_factory=list,
        description="Additional fees (airport surcharges, one-way fees, etc.)"
    )
    cancellation_policy: Optional[str] = Field(
        default=None,
        description="Cancellation and modification policies"
    )
    gps_availability: Optional[bool] = Field(
        default=None,
        description="GPS availability and rental costs"
    )
    child_seat_availability: Optional[bool] = Field(
        default=None,
        description="Child seat availability and rental costs"
    )
    parking_information: Optional[str] = Field(
        default=None,
        description="Parking availability, costs, and restrictions at destination"
    )
    contact_info: Optional[ContactInfo] = Field(
        default=None,
        description="Contact information for the car rental company"
    )


class RideSharingOption(BaseModel):
    """
    Detailed information for ride-sharing services including availability, pricing, and features.
    
    This model captures comprehensive ride-sharing information to help travelers understand
    local transportation options and costs.
    """
    service_name: Optional[str] = Field(
        default=None,
        description="Ride-sharing service name (Uber, Lyft, local equivalents)"
    )
    availability_areas: Optional[str] = Field(
        default=None,
        description="Service coverage areas and availability zones"
    )
    vehicle_types: List[str] = Field(
        default_factory=list,
        description="Available vehicle types (standard, premium, XL, etc.)"
    )
    base_fares: Optional[Dict[str, float]] = Field(
        default_factory=dict,
        description="Base fares by vehicle type"
    )
    per_km_rates: Optional[Dict[str, float]] = Field(
        default_factory=dict,
        description="Per kilometer rates by vehicle type"
    )
    per_minute_rates: Optional[Dict[str, float]] = Field(
        default_factory=dict,
        description="Per minute rates by vehicle type"
    )
    surge_pricing_info: Optional[str] = Field(
        default=None,
        description="Surge pricing patterns and peak hours"
    )
    payment_methods: List[str] = Field(
        default_factory=list,
        description="Accepted payment methods"
    )
    tipping_culture: Optional[str] = Field(
        default=None,
        description="Local tipping expectations and customs"
    )
    safety_features: List[str] = Field(
        default_factory=list,
        description="Safety features including driver verification, ride tracking, etc."
    )
    accessibility_features: List[str] = Field(
        default_factory=list,
        description="Accessibility features for travelers with disabilities"
    )
    language_support: List[str] = Field(
        default_factory=list,
        description="Language support and communication options"
    )
    airport_service: Optional[bool] = Field(
        default=None,
        description="Airport pickup and drop-off service availability"
    )
    contact_info: Optional[ContactInfo] = Field(
        default=None,
        description="Contact information for the ride-sharing service"
    )


class TaxiServiceOption(BaseModel):
    """
    Detailed information for taxi services including companies, pricing, and reliability.
    
    This model captures comprehensive taxi service information to help travelers understand
    traditional transportation options.
    """
    company_name: Optional[str] = Field(
        default=None,
        description="Taxi company name or service provider"
    )
    service_type: Optional[str] = Field(
        default=None,
        description="Service type (metered, fixed rate, airport transfer, etc.)"
    )
    pricing_structure: Optional[str] = Field(
        default=None,
        description="Pricing structure including base fare, per km rates, and surcharges"
    )
    airport_transfer_rates: Optional[Dict[str, float]] = Field(
        default_factory=dict,
        description="Airport transfer rates to different zones or destinations"
    )
    booking_methods: List[str] = Field(
        default_factory=list,
        description="Booking methods (phone, app, street hail, hotel concierge)"
    )
    availability_hours: Optional[str] = Field(
        default=None,
        description="Service availability hours and 24/7 service information"
    )
    vehicle_types: List[str] = Field(
        default_factory=list,
        description="Available vehicle types (standard, luxury, van, etc.)"
    )
    safety_rating: Optional[float] = Field(
        default=None,
        description="Safety rating based on driver verification and service quality"
    )
    reliability_score: Optional[float] = Field(
        default=None,
        description="Reliability score based on on-time performance and availability"
    )
    tipping_expectations: Optional[str] = Field(
        default=None,
        description="Local tipping customs and expectations"
    )
    accessibility_features: List[str] = Field(
        default_factory=list,
        description="Accessibility features for travelers with disabilities"
    )
    contact_info: Optional[ContactInfo] = Field(
        default=None,
        description="Contact information for the taxi service"
    )


class AlternativeTransportOption(BaseModel):
    """
    Detailed information for alternative transportation options including walking, cycling, and unique transport.
    
    This model captures comprehensive alternative transportation information for travelers
    who prefer non-motorized or unique transportation methods.
    """
    transport_type: Optional[str] = Field(
        default=None,
        description="Type of alternative transportation (walking, cycling, scooter, water taxi, etc.)"
    )
    service_name: Optional[str] = Field(
        default=None,
        description="Service or company name if applicable"
    )
    coverage_area: Optional[str] = Field(
        default=None,
        description="Coverage area and route information"
    )
    rental_costs: Optional[Dict[str, float]] = Field(
        default_factory=dict,
        description="Rental costs by duration (hourly, daily, weekly)"
    )
    safety_considerations: List[str] = Field(
        default_factory=list,
        description="Safety considerations and recommended precautions"
    )
    weather_impact: Optional[str] = Field(
        default=None,
        description="Weather impact on availability and safety"
    )
    accessibility_features: List[str] = Field(
        default_factory=list,
        description="Accessibility features and limitations"
    )
    recommended_routes: List[str] = Field(
        default_factory=list,
        description="Recommended routes and scenic paths"
    )
    equipment_requirements: List[str] = Field(
        default_factory=list,
        description="Required equipment or gear"
    )
    contact_info: Optional[ContactInfo] = Field(
        default=None,
        description="Contact information for the service"
    )


class TouristTransportOption(BaseModel):
    """
    Detailed information for tourist-specific transportation options including passes and guided transport.
    
    This model captures comprehensive tourist transportation information including
    specialized services and passes designed for visitors.
    """
    service_name: Optional[str] = Field(
        default=None,
        description="Tourist transportation service or pass name"
    )
    service_type: Optional[str] = Field(
        default=None,
        description="Service type (hop-on-hop-off, tourist pass, guided tour, etc.)"
    )
    coverage_inclusions: List[str] = Field(
        default_factory=list,
        description="What's included in the service or pass"
    )
    duration_options: List[str] = Field(
        default_factory=list,
        description="Available duration options (1-day, 3-day, weekly, etc.)"
    )
    pricing: Optional[Dict[str, float]] = Field(
        default_factory=dict,
        description="Pricing by duration and passenger type"
    )
    route_information: Optional[str] = Field(
        default=None,
        description="Route information and key stops"
    )
    operating_hours: Optional[str] = Field(
        default=None,
        description="Operating hours and frequency"
    )
    booking_requirements: Optional[str] = Field(
        default=None,
        description="Booking requirements and advance purchase recommendations"
    )
    value_assessment: Optional[str] = Field(
        default=None,
        description="Value assessment and cost-benefit analysis"
    )
    contact_info: Optional[ContactInfo] = Field(
        default=None,
        description="Contact information for the tourist service"
    )


class TransportationSearchResults(BaseModel):
    """
    Comprehensive transportation search results containing all local transportation options.
    
    This model provides a complete overview of available transportation options with detailed
    analysis, recommendations, and important considerations for travelers. All information should be
    tailored to the specific travel requirements and preferences provided in the task context.
    """
    search_summary: Optional[Dict[str, Any]] = Field(
        default_factory=dict,
        description="Summary statistics including primary transportation hubs, cost ranges, "
                   "and best value highlights. Include currency and search criteria used."
    )
    public_transportation: Optional[PublicTransportOption] = Field(
        default=None,
        description="Public transportation options including metro, buses, and regional transport"
    )
    car_rental_options: List[CarRentalOption] = Field(
        default_factory=list,
        description="Car rental options from major and local companies"
    )
    ride_sharing_services: List[RideSharingOption] = Field(
        default_factory=list,
        description="Ride-sharing services available in the destination"
    )
    taxi_services: List[TaxiServiceOption] = Field(
        default_factory=list,
        description="Taxi services and companies available"
    )
    alternative_transportation: List[AlternativeTransportOption] = Field(
        default_factory=list,
        description="Alternative transportation options including walking, cycling, and unique transport"
    )
    tourist_transportation: List[TouristTransportOption] = Field(
        default_factory=list,
        description="Tourist-specific transportation options and passes"
    )
    recommendations: Optional[Dict[str, Any]] = Field(
        default_factory=dict,
        description="Specific recommendations including best options for different traveler types, "
                   "budget considerations, and accessibility needs. Include reasoning for each recommendation."
    )
    cost_comparison: Optional[Dict[str, Any]] = Field(
        default_factory=dict,
        description="Cost comparison analysis between different transportation options"
    )
    safety_assessment: Optional[Dict[str, Any]] = Field(
        default_factory=dict,
        description="Safety assessment including safe areas, areas to avoid, and safety tips"
    )
    accessibility_information: Optional[Dict[str, Any]] = Field(
        default_factory=dict,
        description="Accessibility information for travelers with special needs"
    )
    seasonal_considerations: List[str] = Field(
        default_factory=list,
        description="Seasonal transportation changes and weather impacts"
    )
    practical_tips: List[str] = Field(
        default_factory=list,
        description="Practical tips for using local transportation"
    )
    emergency_information: List[str] = Field(
        default_factory=list,
        description="Emergency contact information and procedures"
    )
    language_barriers: List[str] = Field(
        default_factory=list,
        description="Language barrier considerations and communication tips"
    )
    mobile_app_recommendations: List[str] = Field(
        default_factory=list,
        description="Recommended mobile apps for navigation and transportation"
    )
    payment_method_preferences: List[str] = Field(
        default_factory=list,
        description="Payment method preferences and requirements"
    )
