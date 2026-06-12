from http.server import BaseHTTPRequestHandler
import json

# memória temporária (simples)
DATA_STORE = {}

class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        global DATA_STORE

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)

        try:
            DATA_STORE = json.loads(body.decode("utf-8"))

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            self.wfile.write(json.dumps({"status": "ok"}).encode())

        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode())


    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        self.wfile.write(json.dumps(DATA_STORE).encode())
