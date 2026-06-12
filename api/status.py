from http.server import BaseHTTPRequestHandler
import json
from pymongo import MongoClient
from datetime import datetime
import os

# MongoDB connection (coloque sua string aqui)
MONGO_URI = os.environ.get("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["pcp_dashboard"]
collection = db["status"]

class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            data = json.loads(body.decode("utf-8"))

            # adiciona timestamp
            data["updated_at"] = datetime.now().isoformat()

            # salva (sempre substitui o último registro)
            collection.delete_many({})
            collection.insert_one(data)

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'{"status":"ok"}')

        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode())
