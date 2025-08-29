from pydantic import BaseModel, Field

class SendEmailInput(BaseModel):
    recipient: str = Field(..., description="Email address of the recipient.")
    subject: str = Field(..., description="Subject line of the email.")
    body: str = Field(..., description="Content or body of the email.")