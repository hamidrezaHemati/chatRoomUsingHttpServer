from http.server import HTTPServer, BaseHTTPRequestHandler


class requestHandler(BaseHTTPRequestHandler):
    counter = 0
    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type", 'text/html')
        self.end_headers()


def main():
    PORT = 9000
    server = HTTPServer(('', PORT), requestHandler)
    print("server running on port ", PORT)
    server.serve_forever()



main()