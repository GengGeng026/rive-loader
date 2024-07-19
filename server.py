import http.server
import socketserver

PORT = 8000

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        if self.path.endswith(".riv"):
            self.send_header('Content-Type', 'application/json')
        super().end_headers()

Handler = CustomHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
