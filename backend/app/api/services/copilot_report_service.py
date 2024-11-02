from typing import List

from httpx import AsyncClient, HTTPError, HTTPStatusError
from pydantic import ValidationError

from app.core.config import settings
from app.models import CopilotMessage, CopilotMessageList, CopilotReport


class CopilotReportService:
    API_URL = settings.COPILOT_API_BASE_URL

    @classmethod
    async def fetch_messages(cls) -> List[CopilotMessage]:
        """
        Fetch the messages from the Copilot API
        """
        async with AsyncClient() as client:
            try:
                response = await client.get(f"{cls.API_URL}messages/current-period")
                response.raise_for_status()
                message_list = CopilotMessageList.model_validate_json(response.text)
                return message_list.messages

            except HTTPStatusError as exc:
                print(f"HTTP Status Exception for {exc.request.url} - {exc}")
                raise

            except ValidationError as exc:
                print(f"Validation error: {exc}")
                raise

            except HTTPError as exc:
                print(f"HTTP Exception for {exc.request.url} - {exc}")
                raise

            except Exception as exc:
                print(f"Exception: {exc}")
                raise

    @classmethod
    async def fetch_report(cls, id: int) -> CopilotReport:
        """
        Fetch a report from the API by id
        """
        async with AsyncClient() as client:
            try:
                response = await client.get(f"{cls.API_URL}reports/{id}")
                response.raise_for_status()
                return CopilotReport.model_validate_json(response.text)

            except HTTPStatusError as exc:
                print(f"HTTP Status Exception for {exc.request.url} - {exc}")
                raise

            except ValidationError as exc:
                print(f"Validation error: {exc}")
                raise

            except HTTPError as exc:
                print(f"HTTP Exception for {exc.request.url} - {exc}")
                raise

            except Exception as exc:
                print(f"Exception: {exc}")
                raise
