from typing import List

import pytest
import pytest_asyncio
from httpx import HTTPStatusError

from app.api.services.copilot_report_service import CopilotReportService
from app.models import CopilotMessage, CopilotReport


@pytest_asyncio.fixture
async def cr_service():
    return CopilotReportService()


@pytest.mark.asyncio
async def test_fetch_messages(cr_service):
    result = await cr_service.fetch_messages()
    assert isinstance(result, List)
    assert len(result) > 0
    assert isinstance(result[0], CopilotMessage)


@pytest.mark.asyncio
async def test_fetch_valid_report(cr_service):
    result = await cr_service.fetch_report(5447)
    assert isinstance(result, CopilotReport)


@pytest.mark.asyncio
async def test_fetch_invalid_report(cr_service):
    try:
        result = await cr_service.fetch_report(999999)
    except HTTPStatusError as exc:
        assert exc.response.status_code == 404
