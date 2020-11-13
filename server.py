from http.server import HTTPServer, BaseHTTPRequestHandler
import random
import string


def create_auth():
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(10))
    return result_str


class requestHandler(BaseHTTPRequestHandler):
    counter = 0

    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type", 'text/plain')
        self.end_headers()

    def do_POST(self):
        if self.headers.get("path") == "/join":
            print("fuck off")
            print(self.headers.get("name"))
            self.send_response(200)
            auth = create_auth()
            print("token: ", auth)
            self.send_header("content-type", 'text/plain')
            self.send_header("token", auth)
            self.end_headers()
        elif self.headers.get("path") == "/message":
            print("shut the fuck up")
            print(self.headers.get("name"))


def main():
    PORT = 9000
    server = HTTPServer(('', PORT), requestHandler)
    print("server running on port ", PORT)
    server.serve_forever()



main()