import http.client as client

connection = client.HTTPConnection('', 9000)
connection.request("GET", "/")
response = connection.getresponse()
print("status: {} and reason: {}".format(response.status, response.reason))