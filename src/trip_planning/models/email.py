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
    css_styles: str = Field(..., description="CSS styles for the email template")
    translations: Dict[EmailLanguage, str] = Field(..., description="Translated content in different languages")

class TravelEmailResponse(BaseModel):
    status: EmailStatus = Field(..., description="Status of the email sending operation")
    message: str = Field(..., description="Detailed message about the email sending result")
    template: EmailTemplate = Field(..., description="The formatted email template with translations")
    selected_language: EmailLanguage = Field(..., description="The language used for the sent email")
    subject: Dict[EmailLanguage, str] = Field(..., description="Email subject in different languages")

class SendEmailInput(BaseModel):
    recipient: str = Field(..., description="Email address of the recipient")
    subject: str = Field(..., description="Subject line of the email")
    body: str = Field(..., description="Content or body of the email")
    preferred_language: Optional[EmailLanguage] = Field(default=EmailLanguage.ENGLISH, 
                                                      description="Preferred language for the email content")