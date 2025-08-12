"""
Common Pydantic models shared across the trip planning application.

This module contains base models, enums, and utility models that are used
across multiple parts of the application.
"""

from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum


class TravelerType(str, Enum):
    """Types of travelers for personalized recommendations."""
    SOLO = "solo"
    COUPLE = "couple"
    FAMILY = "family"
    BUSINESS = "business"
    BACKPACKER = "backpacker"
    LUXURY = "luxury"
    BUDGET = "budget"


class BudgetRange(str, Enum):
    """Budget ranges for filtering options."""
    BUDGET = "budget"
    MODERATE = "moderate"
    LUXURY = "luxury"
    PREMIUM = "premium"


class Location(BaseModel):
    """Geographic location information."""
    city: str = Field(description="City name")
    country: str = Field(description="Country name")
    latitude: Optional[float] = Field(description="Latitude coordinate")
    longitude: Optional[float] = Field(description="Longitude coordinate")
    timezone: Optional[str] = Field(description="Timezone information")


class PriceInfo(BaseModel):
    """Standardized price information."""
    amount: float = Field(description="Price amount")
    currency: str = Field(description="Currency code (e.g., USD, EUR)")
    original_amount: Optional[float] = Field(description="Original price before discounts")
    discount_percentage: Optional[float] = Field(description="Discount percentage if applicable")


class ContactInfo(BaseModel):
    """Contact information for services and accommodations."""
    phone: Optional[str] = Field(description="Phone number")
    email: Optional[str] = Field(description="Email address")
    website: Optional[str] = Field(description="Website URL")
    address: Optional[str] = Field(description="Physical address")


class Review(BaseModel):
    """Standardized review information."""
    rating: float = Field(description="Rating out of 5 stars")
    review_count: int = Field(description="Number of reviews")
    recent_rating: Optional[float] = Field(description="Recent average rating")
    review_highlights: List[str] = Field(description="Key points from recent reviews")
