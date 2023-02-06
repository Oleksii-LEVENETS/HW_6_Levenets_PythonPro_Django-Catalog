import time

from .models import Logger


class LogMiddleware:
    """Request Logging Middleware."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        path = request.get_full_path()
        method = request.method
        request_data = request.POST

        response = self.get_response(request)

        if "/admin/" in path:
            return response
        run_time = time.time() - start_time
        Logger(
            path=path,
            method=method,
            request_data=request_data,
            run_time=run_time
        ).save()

        return response
