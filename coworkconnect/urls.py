from django.conf import settings
from django.http import Http404, HttpResponse
from django.urls import include, path, re_path
from django.views.static import serve


def home(_request):
    return HttpResponse("CoWorkConnect API is running")


def serve_ui(request, path="index.html"):
    target = path or "index.html"
    try:
        return serve(request, target, document_root=settings.BASE_DIR / "ui")
    except Http404:
        raise


urlpatterns = [
    path("api/", include("api.urls")),
    path("uploads/<path:path>", serve, {"document_root": settings.MEDIA_ROOT}),
    path("", serve_ui),
    re_path(r"^(?P<path>.*)$", serve_ui),
]
