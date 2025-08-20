from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class CostBreakdownItem(BaseModel):
    category: str  # e.g., flights, accommodation, dining, activities
    amount: float
    currency: str
    notes: Optional[str] = None

class VariableCostItem(BaseModel):
    description: str
    estimated_amount: float
    currency: str
    adjustable: bool = True
    notes: Optional[str] = None

class FinalBudgetSummary(BaseModel):
    total_trip_cost: float
    budget_limit: float
    currency: str
    within_budget: bool
    fixed_costs: List[CostBreakdownItem]
    variable_costs: List[VariableCostItem]
    cost_comparison_table: Optional[List[Dict[str, str]]] = None  # For tabular data
    budget_chart_data: Optional[Dict[str, float]] = None  # For visualizations
    important_notes: Optional[List[str]] = None
