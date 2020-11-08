from http.server import HTTPServer, BaseHTTPRequestHandler

class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type", 'text/html')
        self.end_headers()
        self.wfile.write("hello hamidreza".encode())


def main():
    PORT = 8000
    server = HTTPServer(('', PORT), requestHandler)
    print("server running on port ", PORT)
    server.serve_forever()



main()