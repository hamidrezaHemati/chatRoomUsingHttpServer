import http.client as client
import urllib.parse


params = urllib.parse.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})


def send_user_name(name):
    name = "hamidreza"
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain", "name": name}
    connection = client.HTTPConnection('', 9000)
    connection.request("POST", "/", params, headers)


def join_chat_request(name):
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain", "name": name, "path": "/join"}
    connection = client.HTTPConnection('', 9000)
    connection.request("POST", "/", params, headers)
    response = connection.getresponse()
    print("status: {} and reason: {}".format(response.status, response.reason))
    print(response.headers.auth)


def main():
    name = input("please enter your username: ")
    join_chat_request(name)



main()
#response = connection.getresponse()
# print("status: {} and reason: {}".format(response.status, response.reason))