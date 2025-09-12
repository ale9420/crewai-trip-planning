from pydantic import BaseModel
from typing import List, Optional


class ComprehensiveTravelDocument(BaseModel):
    trip_title: str
    content: str
    resources: Optional[List[str]] = None  # URLs, files, etc.
    