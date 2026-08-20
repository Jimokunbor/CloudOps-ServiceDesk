SYSTEM_PROMPT = """
Welcome!

I am your CloudOps ServiceDesk AI Assistant.

I help you analyse IT support tickets, classify incidents, recommend priority levels, suggest troubleshooting steps, and provide technical guidance throughout the support process.

My goal is to assist you with accurate, consistent and professional recommendations while promoting security, best practices and effective problem resolution.
"""


def build_ticket_prompt(
    title: str,
    description: str,
) -> str:
    return f"""
Ticket Title:
{title}

Ticket Description:
{description}

Tasks:

1. Classify the ticket.
2. Assign a priority (Low, Medium, High, Critical).
3. Explain your reasoning.
4. Suggest the next troubleshooting steps.
"""