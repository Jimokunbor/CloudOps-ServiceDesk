from fastapi import APIRouter

from app.ai.prompts import build_ticket_prompt
from app.ai.service import AIService

router = APIRouter(
    prefix="/ai",
    tags=["Artificial Intelligence"],
)

ai_service = AIService()


@router.post("/classify")
def classify_ticket(
    title: str,
    description: str,
):
    prompt = build_ticket_prompt(
        title=title,
        description=description,
    )

    result = ai_service.generate(prompt)

    return result


@router.post("/summarize")
def summarize_ticket(
    title: str,
    description: str,
):
    prompt = f"""
Summarize the following IT support ticket.

Title:
{title}

Description:
{description}
"""

    result = ai_service.generate(prompt)

    return result


@router.post("/priority")
def recommend_priority(
    title: str,
    description: str,
):
    prompt = f"""
Determine the priority of this IT support ticket.

Title:
{title}

Description:
{description}

Respond with:

Priority:
Reason:
"""

    result = ai_service.generate(prompt)

    return result