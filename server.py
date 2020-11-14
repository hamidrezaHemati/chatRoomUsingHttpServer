from http.server import HTTPServer, BaseHTTPRequestHandler
import random
import string

members = {}
def create_auth():
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(10))
    return result_str


class requestHandler(BaseHTTPRequestHandler):
    counter = 0
    def do_GET(self):
        if self.path == "/list":
            print("user wants list")
            self.send_response(200)
            self.send_header("content-type", 'text/plain')
            self.send_header("list", members)
            self.end_headers()

    def do_POST(self):
        if self.path == "/join":
            print(self.headers.get("name"), " has joined to the group")
            auth = create_auth()
            members[self.headers.get("name")] = auth
            print("token: ", auth)
            self.send_response(200)
            self.send_header("content-type", 'text/plain')
            self.send_header("token", auth)
            self.end_headers()
        elif self.path == "/message":
            print(self.headers.get("token"), " : ", self.headers.get("text"))


def main():
    PORT = 9000
    server = HTTPServer(('', PORT), requestHandler)
    print("server running on port ", PORT)
    server.serve_forever()



main()