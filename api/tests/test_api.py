import json
import sys
import unittest
from io import BytesIO
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from app import ApiHandler


class MockRequestHandler(ApiHandler):
    def __init__(self, path):
        self.path = path
        self.rfile = BytesIO()
        self.wfile = BytesIO()
        self.headers = {}
        self.command = "GET"
        self.request_version = "HTTP/1.1"
        self.server_version = "TestServer"
        self.sys_version = ""
        self.responses = []

    def send_response(self, code, message=None):
        self.status_code = code

    def send_header(self, keyword, value):
        pass

    def end_headers(self):
        pass


def call_get(path):
    handler = MockRequestHandler(path)
    handler.do_GET()
    body = handler.wfile.getvalue().decode("utf-8")
    return handler.status_code, json.loads(body)


class ApiTests(unittest.TestCase):
    def test_get_chamados_retorna_200(self):
        status_code, payload = call_get("/chamados")
        self.assertEqual(status_code, 200)
        self.assertTrue(payload["success"])
        self.assertGreaterEqual(len(payload["data"]), 10)

    def test_json_possui_campos_obrigatorios(self):
        status_code, payload = call_get("/chamados/1")
        chamado = payload["data"]
        self.assertEqual(status_code, 200)
        for field in ["id", "titulo", "servico", "prioridade", "status"]:
            self.assertIn(field, chamado)

    def test_chamado_inexistente_retorna_404(self):
        status_code, payload = call_get("/chamados/999")
        self.assertEqual(status_code, 404)
        self.assertFalse(payload["success"])
        self.assertEqual(payload["error"], "Chamado não encontrado.")

    def test_status_da_api_retorna_nome_versao_e_status(self):
        status_code, payload = call_get("/status")
        self.assertEqual(status_code, 200)
        self.assertEqual(payload["data"]["status"], "online")
        self.assertIn("nome", payload["data"])
        self.assertIn("versao", payload["data"])


if __name__ == "__main__":
    unittest.main()
