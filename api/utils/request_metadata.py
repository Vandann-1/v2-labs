def get_client_ip(request) -> str:
    forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR", "")
    if forwarded_for:
        return forwarded_for.split(",")[0].strip()
    return request.META.get("REMOTE_ADDR", "")


def extract_lead_request_metadata(request) -> dict:
    source_page = (
        request.data.get("source_page")
        or request.headers.get("Referer")
        or request.headers.get("Origin")
        or ""
    )

    return {
        "ip_address": get_client_ip(request) or None,
        "user_agent": request.headers.get("User-Agent", "") or None,
        "source_page": source_page or None,
    }
