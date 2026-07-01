import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import urlparse


APP_NAME = "API de Chamados de Suporte em Nuvem"
APP_VERSION = "1.0.0"
DATA_PATH = Path(__file__).parent / "data" / "chamados.json"


def load_chamados():
    with DATA_PATH.open(encoding="utf-8") as data_file:
        return json.load(data_file)


def response_payload(success, data=None, error=None):
    return {
        "success": success,
        "data": data,
        "error": error,
    }


class ApiHandler(BaseHTTPRequestHandler):
    def _send_json(self, status_code, payload):
        encoded = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def do_GET(self):
        try:
            path = urlparse(self.path).path.strip("/")

            if path == "status":
                self._send_json(
                    200,
                    response_payload(
                        True,
                        {
                            "nome": APP_NAME,
                            "versao": APP_VERSION,
                            "status": "online",
                        },
                    ),
                )
                return

            if path == "chamados":
                self._send_json(200, response_payload(True, load_chamados()))
                return

            if path.startswith("chamados/"):
                chamado_id = path.split("/", 1)[1]
                chamado = next(
                    (item for item in load_chamados() if str(item["id"]) == chamado_id),
                    None,
                )
                if chamado is None:
                    self._send_json(
                        404,
                        response_payload(False, error="Chamado não encontrado."),
                    )
                    return
                self._send_json(200, response_payload(True, chamado))
                return

            self._send_json(404, response_payload(False, error="Rota não encontrada."))
        except Exception as exc:
            self._send_json(500, response_payload(False, error=str(exc)))

    def log_message(self, format, *args):
        return


def create_server(host="0.0.0.0", port=8000):
    return HTTPServer((host, port), ApiHandler)


if __name__ == "__main__":
    server = create_server()
    print(f"{APP_NAME} rodando em http://localhost:8000")
    server.serve_forever()
