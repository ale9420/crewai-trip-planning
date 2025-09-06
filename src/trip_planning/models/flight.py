"""
Flight-related Pydantic models for trip planning.

This module contains models for flight search results and individual flight options
that agents use to provide comprehensive flight information and recommendations.
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any


class FlightOption(BaseModel):
    """
    Detailed information for a single flight option including all pricing, timing, and service details.
    
    This model captures comprehensive flight information to help travelers make informed decisions
    based on their specific needs, budget, and preferences.
    """
    airline: str = Field(
        description="The airline name and any codeshare partners. Include major carrier, "
                   "budget airline, or regional carrier designation."
    )
    flight_numbers: List[str] = Field(
        default_factory=list,
        description="All flight numbers for the journey including connecting flights. "
                   "Format as airline code + number (e.g., 'AA123', 'BA456')."
    )
    departure_time: str = Field(
        description="Departure time in local timezone with date. Include timezone information "
                   "if different from origin timezone."
    )
    arrival_time: str = Field(
        description="Arrival time in local timezone with date. Include timezone information "
                   "if different from destination timezone."
    )
    total_travel_time: str = Field(
        description="Total journey time including layovers. Format as hours and minutes "
                   "(e.g., '8h 30m' or '2h 15m' for direct flights)."
    )
    stops: int = Field(
        description="Number of stops (0 for direct flights, 1 for one connection, etc.). "
                   "Include layover duration and airport codes."
    )
    layover_details: Optional[List[str]] = Field(
        default_factory=list,
        description="Detailed layover information including airport codes, duration, "
                   "and any terminal changes. Include visa requirements for layover countries."
    )
    aircraft_type: Optional[str] = Field(
        default=None,
        description="Aircraft model and configuration. Include seat layout and capacity "
                   "information if available."
    )
    total_price_per_person: Optional[float] = Field(
        default=None,
        description="Total price per person including all taxes and fees. "
                   "Specify currency and whether price is for one-way or round-trip."
    )
    price_breakdown: Optional[Dict[str, Any]] = Field(
        default_factory=dict,
        description="Detailed price breakdown including base fare, taxes, fuel surcharges, "
                   "and any additional fees. Include currency for each component."
    )
    baggage_allowance: Optional[str] = Field(
        default=None,
        description="Checked and carry-on baggage allowance. Include weight limits, "
                   "dimension restrictions, and any additional baggage fees."
    )
    seat_selection_cost: Optional[float] = Field(
        default=None,
        description="Cost for seat selection including any advance seat reservation fees. "
                   "Specify if seat selection is included in base fare."
    )
    cancellation_fees: Optional[str] = Field(
        default=None,
        description="Cancellation and change fees including refund policies. "
                   "Include time restrictions and any non-refundable components."
    )
    cabin_class: Optional[str] = Field(
        default=None,
        description="Cabin class (Economy, Premium Economy, Business, First). "
                   "Include seat configuration and legroom information."
    )
    in_flight_amenities: List[str] = Field(
        default_factory=list,
        description="Available in-flight amenities including WiFi, entertainment systems, "
                   "meal service, power outlets, and lounge access."
    )
    on_time_performance: Optional[float] = Field(
        default=None,
        description="Airline's on-time performance percentage for this route. "
                   "Include historical data if available."
    )
    customer_rating: Optional[float] = Field(
        default=None,
        description="Customer satisfaction rating out of 5 stars. "
                   "Include number of reviews and recent feedback trends."
    )
    airport_transfer_info: Optional[str] = Field(
        default=None,
        description="Information about airport transfers including transfer times, "
                   "costs, and transportation options between terminals."
    )
    visa_requirements: List[str] = Field(
        default_factory=list,
        description="Visa requirements for any layover countries. "
                   "Include transit visa needs and application processes."
    )
    covid_requirements: Optional[List[str]] = Field(
        default_factory=list,
        description="COVID-19 related requirements including testing, vaccination, "
                   "and quarantine rules for all countries in the journey."
    )
    booking_class: Optional[str] = Field(
        default=None,
        description="Fare class and booking code. Include fare rules and restrictions "
                   "for changes, cancellations, and upgrades."
    )
    loyalty_program: Optional[str] = Field(
        default=None,
        description="Loyalty program earning potential including miles/points per dollar "
                   "and any elite status benefits that apply."
    )




class FlightSearchResults(BaseModel):
    """
    Comprehensive flight search results containing summary statistics and detailed flight options.
    
    This model provides a complete overview of available flight options with pricing analysis,
    recommendations, and important considerations for travelers. All information should be
    tailored to the specific travel requirements and preferences provided in the task context.
    """
    search_summary: Optional[Dict[str, Any]] = Field(
        default_factory=dict,
        description="Summary statistics including total options found, price range, "
                   "and best value highlights. Include currency and search criteria used."
    )
    flight_options: List[FlightOption] = Field(
        default_factory=list,
        description="Detailed flight options (maximum 10) ranked by relevance and value. "
                   "Include a mix of direct flights, connections, and different price points."
    )
    recommendations: Optional[List[str]] = Field(
        default_factory=list,
        description="Specific recommendations including top 3 value-for-money options, "
                   "best options for families, business travelers, and budget-conscious travelers. "
                   "Include reasoning for each recommendation."
    )
    alternative_airports: List[str] = Field(
        default_factory=list,
        description="Nearby airports that could offer better pricing or convenience. "
                   "Include distance from primary airports and transportation options."
    )
    seasonal_considerations: Optional[List[str]] = Field(
        default_factory=list,
        description="Seasonal price variations, peak travel periods, and weather impacts "
                   "on flight availability and pricing."
    )

