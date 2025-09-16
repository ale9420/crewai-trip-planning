from pydantic import BaseModel, Field
from enum import Enum
from typing import Dict, Optional

class EmailStatus(str, Enum):
    SENT = "sent"
    FAILED = "failed"
    PENDING = "pending"

class EmailLanguage(str, Enum):
    ENGLISH = "en"
    SPANISH = "es"

class EmailTemplate(BaseModel):
    html_content: str = Field(..., description="HTML formatted content of the email")
    css_styles: Optional[str] = Field(default="", description="CSS styles for the email template")

class TravelEmailResponse(BaseModel):
    status: EmailStatus = Field(default=EmailStatus.PENDING, description="Status of the email sending operation")
    message: str = Field(default="Email template prepared", description="Detailed message about the email sending result")
    template: Optional[EmailTemplate] = Field(default=None, description="The formatted email template with translations")
    selected_language: EmailLanguage = Field(default=EmailLanguage.ENGLISH, description="The language used for the sent email")
    subject: Optional[Dict[EmailLanguage, str]] = Field(
        default=None,
        description="Email subject in different languages. Must use lowercase language codes: 'en' for English, 'es' for Spanish",
        json_schema_extra={
            "example": {
                EmailLanguage.ENGLISH: "Your Travel Itinerary",
                EmailLanguage.SPANISH: "Su Itinerario de Viaje"
            }
        }
    )

class SendEmailInput(BaseModel):
    recipient: str = Field(..., description="Email address of the recipient")
    subject: str = Field(..., description="Subject line of the email")
    body: str = Field(..., description="Content or body of the email")
    preferred_language: Optional[EmailLanguage] = Field(default=EmailLanguage.ENGLISH, 
                                                      description="Preferred language for the email content")