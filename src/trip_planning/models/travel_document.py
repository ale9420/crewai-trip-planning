from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class TravelDocumentSection(BaseModel):
    title: str
    content: str
    resources: Optional[List[str]] = None  # URLs, files, etc.

class EmergencyContact(BaseModel):
    name: str
    phone: str
    relation: Optional[str] = None
    notes: Optional[str] = None

class ComprehensiveTravelDocument(BaseModel):
    trip_title: str
    summary: Optional[str] = None
    recommendations: Optional[List[str]] = None
    practical_information: Optional[List[TravelDocumentSection]] = None
    emergency_contacts: Optional[List[EmergencyContact]] = None
    resources: Optional[List[str]] = None  # URLs, files, etc.
    notes: Optional[str] = None
