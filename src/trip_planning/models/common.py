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
    original_amount: Optional[float] = Field(None, description="Original price before discounts")
    discount_percentage: Optional[float] = Field(None, description="Discount percentage if applicable")
    
    def __init__(self, **data):
        super().__init__(**data)
        # If original_amount is not provided, set it equal to amount
        if self.original_amount is None:
            self.original_amount = self.amount
        # If there's a difference between original and current amount, calculate discount
        if self.discount_percentage is None and self.original_amount != self.amount:
            self.discount_percentage = ((self.original_amount - self.amount) / self.original_amount) * 100


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
