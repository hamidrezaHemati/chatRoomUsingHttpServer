from http.server import HTTPServer, BaseHTTPRequestHandler
import random
import string

members = dict()


def create_auth():
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(10))
    return result_str


class requestHandler(BaseHTTPRequestHandler):
    counter = 0

    def do_GET(self):
        if self.path == "/list":
            # print("user wants list")
            list = members.keys()
            self.send_response(200)
            self.send_header("content-type", 'text/plain')
            self.send_header("list", list)
            self.end_headers()

    def do_POST(self):
        if self.path == "/join":
            print(self.headers.get("name"), "has joined to the group")
            auth = create_auth()
            members[self.headers.get("name")] = auth
            self.send_response(200)
            self.send_header("content-type", 'text/plain')
            self.send_header("token", auth)
            self.end_headers()
        elif self.path == "/message":
            name = ''
            found_flag = 0
            for username, tokens in members.items():
                if tokens == self.headers.get("token"):
                    name = username
                    found_flag = 1
                    break
            if found_flag == 0:
                response = 403
            else:
                print(name, " : ", self.headers.get("text"))
                response = 200
            # print("server response is: ", response)
            self.send_response(response)
            self.send_header("content-type", 'text/plain')
            self.end_headers()
        elif self.path == "/leave":
            found_flag = 0
            for username, tokens in members.items():
                if tokens == self.headers.get("token"):
                    found_flag = 1
                    del members[username]
                    break
            if found_flag == 0:
                response = 403
            else:
                response = 200
            self.send_response(response)
            self.send_header("content-type", 'text/plain')
            self.end_headers()


def main():
    PORT = 9000
    server = HTTPServer(('', PORT), requestHandler)
    print("server running on port ", PORT)
    server.serve_forever()


main()