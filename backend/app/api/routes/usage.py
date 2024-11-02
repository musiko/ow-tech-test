from typing import List

from app.api.services.copilot_report_service import CopilotReportService
from app.api.services.credit_calculator_service import calculate_message_credits
from app.models import CopilotUsage
from fastapi import APIRouter, HTTPException
from httpx import HTTPStatusError

router = APIRouter()


@router.get("/", response_model=List[CopilotUsage], response_model_exclude_none=True)
async def get_usage():
    """
    Get the usage of the Copilot service
    """
    cr_service = CopilotReportService()
    usages = []
    try:
        messages = await cr_service.fetch_messages()
        for message in messages:
            usage = CopilotUsage(
                message_id=message.id,
                timestamp=message.timestamp,
                credits_used=0.0,
            )
            # If the message has a report_id, fetch the report to get the credit cost and report name
            if hasattr(message, "report_id") and message.report_id is not None:
                try:
                    report = await cr_service.fetch_report(message.report_id)
                    usage.report_name = report.name
                    usage.credits_used = report.credit_cost
                except HTTPStatusError as exc:
                    # If the report is not found, calculate the credits used from the message
                    if exc.response.status_code == 404:
                        usage.credits_used = float(
                            calculate_message_credits(message.text)
                        )
                    else:
                        # REVIEW: retry?
                        raise HTTPException(
                            status_code=500, detail="Internal Server Error"
                        )
                except Exception:
                    raise HTTPException(status_code=500, detail="Internal Server Error")
            else:
                usage.credits_used = float(calculate_message_credits(message.text))
            usages.append(usage)
        return usages

    except HTTPStatusError as exc:
        raise HTTPException(
            status_code=exc.response.status_code, detail=exc.response.reason_phrase
        )

    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")
