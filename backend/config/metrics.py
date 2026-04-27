from __future__ import annotations

import os
import time

from django.http import HttpRequest, HttpResponse

_PROCESS_START_TIME_SECONDS = time.time()


def metrics(_request: HttpRequest) -> HttpResponse:
    """
    Endpoint Prometheus minimal (format texte).
    On évite volontairement des dépendances externes pour rester léger côté projet.
    """

    app = os.getenv("APP_NAME", "meteo_api")
    lines = [
        "# HELP meteo_api_up 1 si l'API répond.",
        "# TYPE meteo_api_up gauge",
        "meteo_api_up 1",
        "# HELP meteo_api_process_start_time_seconds Démarrage du process.",
        "# TYPE meteo_api_process_start_time_seconds gauge",
        f"meteo_api_process_start_time_seconds {_PROCESS_START_TIME_SECONDS}",
        "# HELP meteo_api_build_info Informations build (constante).",
        "# TYPE meteo_api_build_info gauge",
        f'meteo_api_build_info{{app="{app}"}} 1',
        "",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain; version=0.0.4")

