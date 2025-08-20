from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class ValidationMetric(BaseModel):
    name: str  # e.g., completeness, feasibility, satisfaction
    score: float  # e.g., 0-100
    notes: Optional[str] = None

class ItineraryIssue(BaseModel):
    description: str
    severity: str  # e.g., warning, critical
    recommendation: Optional[str] = None

class ItineraryValidationReport(BaseModel):
    overall_score: float  # e.g., 0-100
    validation_metrics: List[ValidationMetric]
    travel_style_match_percentage: Optional[float] = None
    issues_found: Optional[List[ItineraryIssue]] = None
    recommendations: Optional[List[str]] = None
    visual_validation_scores: Optional[Dict[str, float]] = None  # For charts/graphs
    quality_metrics: Optional[Dict[str, float]] = None
    notes: Optional[str] = None
