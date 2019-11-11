import http.client

conn = http.client.HTTPConnection("a,blazemeter,com")

headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic OGNhYzQ2ZDdiNDYyNjE4OTM3ZGI1Yjc1OjgzYjcyMGYyZTJjNDA1ODY2YjE3NjliYjQ1ODI2MzU1NDJhNjg0ZTU0ODMzMWE5NDgzMDhlMmY4OWNjZjdlYzA4MDdjMjhkYg==",
    'User-Agent': "PostmanRuntime/7.19.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "9e58d93d-8a03-4ead-972b-559b8775d6b1,d3444990-a6d3-42cb-91f8-7233f3833cb8",
    'Host': "a.blazemeter.com",
    'Accept-Encoding': "gzip, deflate",
    'Cookie': "bzm_sess=a49850b5873308c85fa9d8c702cd60ea",
    'Content-Length': "0",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

conn.request("POST", "api,v4,tests,7389741,start", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
