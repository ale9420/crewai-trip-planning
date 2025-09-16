import yagmail
from pydantic import BaseModel, Field
from crewai.tools import BaseTool
from typing import Type
import os

# Define the input schema for the tool (so the LLM knows what arguments to provide)
class SendEmailInput(BaseModel):
    recipient: str = Field(..., description="Email address of the recipient.")
    subject: str = Field(..., description="Subject line of the email.")
    body: str = Field(..., description="Content or body of the email.")

class EmailTool(BaseTool):
    name: str = "Email Tool"
    description: str = (
        "Send emails using the provided recipient email address, subject, and HTML body content. "
        "Use this tool to send the travel itinerary email to the user's specified email address."
    )
    args_schema: Type[BaseModel] = SendEmailInput

    def _run(self, recipient: str, subject: str, body: str) -> str:
        try:
            yag = setup_yagmail_client()
            yag.send(to=recipient, subject=subject, contents=body)
            return f"Email successfully sent to {recipient} with subject: '{subject}'."
        except Exception as e:
            return f"Failed to send email. Error: {str(e)}"

def setup_yagmail_client():
    """Helper function to set up the yagmail client.
    Reads credentials from environment variables for security.
    """
    email_address = os.getenv("GMAIL_ADDRESS")  # e.g., your.email@gmail.com
    email_password = os.getenv("GMAIL_APP_PASSWORD") # NOT your regular password!
    return yagmail.SMTP(email_address, email_password)

# Note: For Gmail, you need to generate an "App Password":
# 1. Enable 2FA on your Google account.
# 2. Go to Google Account settings > Security > 2FA > App passwords.
# 3. Generate a password for your CrewAI application.
# 4. Set the GMAIL_ADDRESS and GMAIL_APP_PASSWORD environment variables.