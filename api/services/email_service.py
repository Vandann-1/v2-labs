from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_templated_email(
    *,
    subject: str,
    to_emails: list[str],
    template_name: str,
    context: dict,
    reply_to: list[str] | None = None,
    from_email: str | None = None,
    text_template_name: str | None = None,
) -> None:
    html_body = render_to_string(template_name, context)
    text_body = (
        render_to_string(text_template_name, context)
        if text_template_name
        else strip_tags(html_body)
    )

    message = EmailMultiAlternatives(
        subject=subject,
        body=text_body,
        from_email=from_email or settings.DEFAULT_FROM_EMAIL,
        to=to_emails,
        reply_to=reply_to or [],
    )
    message.attach_alternative(html_body, "text/html")
    message.send(fail_silently=False)
