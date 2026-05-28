from django.conf import settings
from django.utils import timezone

from .email_service import send_templated_email


ENTERPRISE_SERVICES = {
    "custom_erp",
    "enterprise_web",
    "crm_dev",
    "saas_dev",
    "cloud_devops",
}
HIGH_BUDGET_MARKERS = {"2,00,000", "200000", "enterprise", "custom quote", "custom"}


def get_priority_details(lead) -> dict:
    normalized_budget = (lead.budget or "").lower().replace(" ", "")
    is_high_budget = any(marker in normalized_budget for marker in HIGH_BUDGET_MARKERS)
    is_enterprise_service = lead.service in ENTERPRISE_SERVICES

    if is_high_budget or is_enterprise_service:
        return {
            "label": "High Priority",
            "tone": "priority",
            "reason": "High-value lead based on service scope or stated budget.",
        }

    return {
        "label": "Standard Priority",
        "tone": "standard",
        "reason": "New inbound lead ready for qualification and response.",
    }


def send_lead_notification(*, lead) -> None:
    priority = get_priority_details(lead)
    submitted_at = timezone.localtime(lead.created_at)
    context = {
        "company_name": settings.V2_LABS_COMPANY_NAME,
        "lead": lead,
        "submitted_at": submitted_at,
        "submitted_timezone": settings.TIME_ZONE,
        "priority": priority,
        "reply_email": f"mailto:{lead.email}",
        "call_link": f"tel:{lead.phone}" if lead.phone else "",
        "source_page": lead.source_page or settings.V2_LABS_FRONTEND_URL,
    }

    subject = (
        f"New Lead Received | {lead.get_service_display()} | "
        f"{lead.name}"
    )

    send_templated_email(
        subject=subject,
        to_emails=settings.LEAD_NOTIFICATION_RECIPIENTS,
        template_name="emails/lead_notification.html",
        text_template_name="emails/lead_notification.txt",
        context=context,
        reply_to=[lead.email],
    )
