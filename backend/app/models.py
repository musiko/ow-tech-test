from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class CopilotMessage(BaseModel):
    id: int
    report_id: Optional[int] = None
    text: str
    timestamp: datetime


class CopilotMessageList(BaseModel):
    messages: List[CopilotMessage]


class CopilotReport(BaseModel):
    id: int
    name: str
    credit_cost: float
