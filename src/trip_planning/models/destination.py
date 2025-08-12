"""
Destination-related Pydantic models for trip planning.

This module contains models for destination investigation and research data
that agents use to provide comprehensive travel information.
"""

from pydantic import BaseModel, Field


class DestinationInvestigation(BaseModel):
    """
    Comprehensive destination intelligence report containing essential travel information.
    
    This model captures all critical information needed for trip planning including
    weather conditions, entry requirements, safety considerations, cultural insights,
    and practical travel tips. All information should be tailored to the specific
    travel dates and user preferences provided in the task context.
    """
    overview: str = Field(
        description="A comprehensive overview of the destination including key highlights, "
                   "general atmosphere, and what makes it unique. Should include major "
                   "attractions, cultural significance, and overall travel appeal."
    )
    weather: list[str] = Field(
        description="Detailed weather information for the specific travel dates including "
                   "temperature ranges, precipitation patterns, humidity levels, and seasonal "
                   "considerations. Include packing recommendations and weather-related travel tips."
    )
    events: list[str] = Field(
        description="Major events, festivals, holidays, or special occasions during the travel period. "
                   "Include impact on crowds, prices, availability, and whether these events "
                   "enhance or complicate the travel experience."
    )
    entry_requirements: list[str] = Field(
        description="Complete entry and visa requirements including passport validity, visa types, "
                   "application processes, fees, and processing times. Include health requirements, "
                   "COVID-19 protocols, and travel insurance mandates."
    )
    safety_tips: list[str] = Field(
        description="Comprehensive safety information including crime rates, common scams, "
                   "areas to avoid, emergency contacts, and health/medical care availability. "
                   "Include political stability and any current travel advisories."
    )
    cultural_norms: list[str] = Field(
        description="Essential cultural etiquette, customs, dress codes, and social norms. "
                   "Include tipping practices, language basics, local dos and don'ts, "
                   "and cultural sensitivities to respect."
    )
    best_times_to_visit: list[str] = Field(
        description="Optimal timing for visiting major attractions including opening hours, "
                   "peak vs. off-peak times, crowd management tips, and recommendations "
                   "for maximizing the visitor experience."
    )
    local_transportation: list[str] = Field(
        description="Complete transportation overview including public transit systems, "
                   "ride-sharing options, taxi services, walking safety, and accessibility "
                   "features for travelers with special needs."
    )
    money_and_connectivity: list[str] = Field(
        description="Financial and communication information including local currency, "
                   "payment methods, ATM availability, internet access, SIM card options, "
                   "mobile coverage, and connectivity costs."
    )
    insider_tips: list[str] = Field(
        description="Local secrets, hidden gems, off-the-beaten-path suggestions, and "
                   "common tourist mistakes to avoid. Include authentic local experiences "
                   "and insider knowledge for a more genuine travel experience."
    )
    recent_developments: list[str] = Field(
        description="Recent news, travel advisories, infrastructure changes, or disruptions "
                   "relevant to the travel period. Include any updates that could impact "
                   "the travel experience or require special planning."
    )
