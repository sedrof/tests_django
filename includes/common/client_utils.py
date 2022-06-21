from rest_framework.request import Request


def get_client_ip(request: Request) -> str:
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip_address = x_forwarded_for.split(",")[-1].strip()
    elif request.META.get("HTTP_X_REAL_IP"):
        ip_address = request.META.get("HTTP_X_REAL_IP")
    else:
        ip_address = request.META.get("REMOTE_ADDR")
    return ip_address
