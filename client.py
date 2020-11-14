import http.client as client
import urllib.parse


params = urllib.parse.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
auth = ''


def get_list_of_users():
    connection = client.HTTPConnection('', 9000)
    print("fuck1")
    connection.request("GET", "/list")
    response = connection.getresponse()
    print("status: {} and reason: {}".format(response.status, response.reason))
    print("members are: ")
    print(response.headers.get("list"))


def send_message(auth):
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain", "token": auth,
               "text": "kiramo bokhor"}
    connection = client.HTTPConnection('', 9000)
    print("fuck1")
    connection.request("POST", "/message", params, headers)


def join_chat_request(name):
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain", "name": name}
    connection = client.HTTPConnection('', 9000)
    connection.request("POST", "/join", params, headers)
    response = connection.getresponse()
    auth = response.headers.get("token")
    print(auth)
    print(response.status)
    if response.status == 200:
        send_message(auth)
    else:
        print("status: {} and reason: {}".format(response.status, response.reason))
    return


def main():
    while 1:
        code = input("enter code: 1 for joining the chat, 2 for getting the list of active members in group, "
                     "3 fo sending message and 4 for leave the chat: ")
        code = int(code)
        if code == 1:
            name = input("please enter your username: ")
            join_chat_request(name)
        elif code == 2:
            get_list_of_users()
        elif code == 3:
            send_message()
        elif code == 4:
            break
        else:
            print("wrong code...try again")

    print("you have kicked out of the group chat")


main()


#long polling
