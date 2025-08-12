"""
Flight-related Pydantic models for trip planning.

This module contains models for flight search results and individual flight options
that agents use to provide comprehensive flight information and recommendations.
"""

from pydantic import BaseModel, Field


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
    flight_numbers: list[str] = Field(
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
    layover_details: list[str] = Field(
        description="Detailed layover information including airport codes, duration, "
                   "and any terminal changes. Include visa requirements for layover countries."
    )
    aircraft_type: str = Field(
        description="Aircraft model and configuration. Include seat layout and capacity "
                   "information if available."
    )
    total_price_per_person: float = Field(
        description="Total price per person including all taxes and fees. "
                   "Specify currency and whether price is for one-way or round-trip."
    )
    price_breakdown: dict[str, float] = Field(
        description="Detailed price breakdown including base fare, taxes, fuel surcharges, "
                   "and any additional fees. Include currency for each component."
    )
    baggage_allowance: str = Field(
        description="Checked and carry-on baggage allowance. Include weight limits, "
                   "dimension restrictions, and any additional baggage fees."
    )
    seat_selection_cost: float = Field(
        description="Cost for seat selection including any advance seat reservation fees. "
                   "Specify if seat selection is included in base fare."
    )
    cancellation_fees: str = Field(
        description="Cancellation and change fees including refund policies. "
                   "Include time restrictions and any non-refundable components."
    )
    cabin_class: str = Field(
        description="Cabin class (Economy, Premium Economy, Business, First). "
                   "Include seat configuration and legroom information."
    )
    in_flight_amenities: list[str] = Field(
        description="Available in-flight amenities including WiFi, entertainment systems, "
                   "meal service, power outlets, and lounge access."
    )
    on_time_performance: float = Field(
        description="Airline's on-time performance percentage for this route. "
                   "Include historical data if available."
    )
    customer_rating: float = Field(
        description="Customer satisfaction rating out of 5 stars. "
                   "Include number of reviews and recent feedback trends."
    )
    airport_transfer_info: str = Field(
        description="Information about airport transfers including transfer times, "
                   "costs, and transportation options between terminals."
    )
    visa_requirements: list[str] = Field(
        description="Visa requirements for any layover countries. "
                   "Include transit visa needs and application processes."
    )
    covid_requirements: list[str] = Field(
        description="COVID-19 related requirements including testing, vaccination, "
                   "and quarantine rules for all countries in the journey."
    )
    booking_class: str = Field(
        description="Fare class and booking code. Include fare rules and restrictions "
                   "for changes, cancellations, and upgrades."
    )
    loyalty_program: str = Field(
        description="Loyalty program earning potential including miles/points per dollar "
                   "and any elite status benefits that apply."
    )
    recommended_booking_channel: str = Field(
        description="Best booking channel recommendation (direct airline, OTA, travel agent). "
                   "Include reasoning and any exclusive deals available."
    )
    booking_timing: str = Field(
        description="Optimal booking timing recommendations. Include advance booking "
                   "requirements and last-minute deal possibilities."
    )


class FlightSearchResults(BaseModel):
    """
    Comprehensive flight search results containing summary statistics and detailed flight options.
    
    This model provides a complete overview of available flight options with pricing analysis,
    recommendations, and important considerations for travelers. All information should be
    tailored to the specific travel requirements and preferences provided in the task context.
    """
    search_summary: dict[str, str] = Field(
        description="Summary statistics including total options found, price range, "
                   "and best value highlights. Include currency and search criteria used."
    )
    flight_options: list[FlightOption] = Field(
        description="Detailed flight options (maximum 10) ranked by relevance and value. "
                   "Include a mix of direct flights, connections, and different price points."
    )
    recommendations: dict[str, str] = Field(
        description="Specific recommendations including top 3 value-for-money options, "
                   "best options for families, business travelers, and budget-conscious travelers. "
                   "Include reasoning for each recommendation."
    )
    alternative_airports: list[str] = Field(
        description="Nearby airports that could offer better pricing or convenience. "
                   "Include distance from primary airports and transportation options."
    )
    flexible_date_recommendations: list[str] = Field(
        description="Recommendations for flexible date travel including potential savings "
                   "and optimal travel dates within the user's flexibility range."
    )
    seasonal_considerations: list[str] = Field(
        description="Seasonal price variations, peak travel periods, and weather impacts "
                   "on flight availability and pricing."
    )
    promotions_and_deals: list[str] = Field(
        description="Current promotions, fare sales, and special deals that could "
                   "provide additional savings or benefits."
    )
    travel_advisories: list[str] = Field(
        description="Any travel advisories, restrictions, or warnings relevant to "
                   "the flight routes or destinations."
    )
    booking_tips: list[str] = Field(
        description="Best practices for booking including timing, payment methods, "
                   "and strategies for securing the best deals."
    )
    insurance_recommendations: list[str] = Field(
        description="Travel insurance recommendations including coverage options, "
                   "costs, and specific policies that would benefit this trip."
    )
