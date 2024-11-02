from typing import List

import httpx
import pytest
from pytest_mock import MockerFixture

from app.api.services.copilot_report_service import CopilotReportService
from app.models import CopilotMessage, CopilotReport


@pytest.fixture
def mock_messages() -> str:
    return """{
        "messages": [
            {
                "id": 1004,
                "text": "What is the security deposit amount?",
                "timestamp": "2024-04-29T11:54:18.493Z"
            },
            {
                "id": 1005,
                "text": "Please generate a comprehensive Tenant Obligations Report.",
                "timestamp": "2024-04-29T12:31:00.539Z",
                "report_id": 5392
            },
            {
                "id": 1006,
                "text": "What are the restrictions on operating hours and any related provisions for commercial tenants?",
                "timestamp": "2024-04-29T12:57:04.853Z"
            }
        ]
    }"""


@pytest.fixture
def mock_report() -> str:
    return """{
        "id": 5447,
        "name": "Landlord Responsibilities Report",
        "credit_cost": 44
    }"""


@pytest.fixture
def cr_service():
    return CopilotReportService()


@pytest.mark.asyncio
async def test_fetch_messages(
    mocker: MockerFixture, cr_service: CopilotReportService, mock_messages: str
):
    mock_get = mocker.patch(
        "httpx.AsyncClient.get",
        return_value=httpx.Response(
            200,
            request=httpx.Request("GET", "http://localhost/messages/current-period"),
            text=mock_messages,
        ),
    )

    result = await cr_service.fetch_messages()
    assert isinstance(result, List)
    assert len(result) == 3
    assert isinstance(result[0], CopilotMessage)
    assert result[0].id == 1004
    assert result[0].text == "What is the security deposit amount?"
    assert result[1].report_id == 5392
    assert mock_get.call_count == 1


@pytest.mark.asyncio
async def test_fetch_valid_report(
    mocker: MockerFixture, cr_service: CopilotReportService, mock_report: str
):
    mock_get = mocker.patch(
        "httpx.AsyncClient.get",
        return_value=httpx.Response(
            200,
            request=httpx.Request("GET", "http://localhost/reports/5447"),
            text=mock_report,
        ),
    )

    report_id = 5447
    result = await cr_service.fetch_report(report_id)
    assert isinstance(result, CopilotReport)
    assert result.id == report_id
    assert result.name == "Landlord Responsibilities Report"
    assert result.credit_cost == 44
    assert mock_get.call_count == 1


@pytest.mark.asyncio
async def test_fetch_invalid_report(
    mocker: MockerFixture, cr_service: CopilotReportService
):
    http_status_error = httpx.HTTPStatusError(
        "Not Found",
        request=httpx.Request("GET", "http://localhost/reports/999999"),
        response=httpx.Response(404),
    )
    mock_get = mocker.patch(
        "httpx.AsyncClient.get",
        side_effect=http_status_error,
    )

    with pytest.raises(httpx.HTTPStatusError) as exc:
        await cr_service.fetch_report(999999)

    assert exc.type is httpx.HTTPStatusError
    assert mock_get.call_count == 1


@pytest.mark.asyncio
async def test_usage_api(mocker: MockerFixture, cr_service: CopilotReportService):
    # TODO: Implement this for /usage API with mock data of messages and report
    assert True
