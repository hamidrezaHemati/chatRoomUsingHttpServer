import http.client as client
import urllib.parse


params = urllib.parse.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})


def leave_chat(auth):
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain", "token": auth}
    connection = client.HTTPConnection('', 9000)
    connection.request("POST", "/leave", params, headers)
    response = connection.getresponse()
    # print("leave response: ", response.status)


def get_list_of_users():
    connection = client.HTTPConnection('', 9000)
    connection.request("GET", "/list")
    response = connection.getresponse()
    # print("status: {} and reason: {}".format(response.status, response.reason))
    return response.headers.get("list")


def send_message(message, auth):
    # print("send message method")
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain", "token": auth,
               "text": message}
    connection = client.HTTPConnection('', 9000)
    connection.request("POST", "/message", params, headers)
    response = connection.getresponse()
    # print("response status send message is: ", response.status)
    if response.status == 403:
        print("currently you are not part of this group chat")


def join_chat_request(name):
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain", "name": name}
    connection = client.HTTPConnection('', 9000)
    connection.request("POST", "/join", params, headers)
    response = connection.getresponse()
    auth = response.headers.get("token")
    # print("geted token is: ", auth)
    # print(response.status)
    if response.status == 200:
        print("you have successfully added to the group")
    else:
        print("cant access to the group")
        return "false"
    return auth


def main():
    name = input("please enter your username: ")
    auth = join_chat_request(name)
    if auth == "false":
        return
    print("enter '/info' when ever you want to see active users ")
    print("enter '/exit' when ever you want leave group ")
    while 1:
        message = input()
        if message == "/info":
            members = get_list_of_users()
            print("active members are: ")
            print(members)
        elif message == "/exit":
            leave_chat(auth)
            break
        else:
            send_message(message, auth)

    print("you have leaved this chat")
    return


main()


#long polling
