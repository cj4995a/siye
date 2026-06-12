from http.server import BaseHTTPRequestHandler
from pymongo import MongoClient
import json
import os

MONGO_URI = os.environ.get("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["pcp_dashboard"]
collection = db["status"]

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            data = collection.find_one({}, {"_id": 0})

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            self.wfile.write(json.dumps(data or {}).encode())

        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode())
