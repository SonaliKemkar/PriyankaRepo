import requests
import sys
import time
import os


def main():   
    results = {}   
    result = _get_result()
   
print "All test runs passed."

def _get_result(): 
   url = "https://a.blazemeter.com/api/v4/tests/7389741/start"

headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic OGNhYzQ2ZDdiNDYyNjE4OTM3ZGI1Yjc1OjgzYjcyMGYyZTJjNDA1ODY2YjE3NjliYjQ1ODI2MzU1NDJhNjg0ZTU0ODMzMWE5NDgzMDhlMmY4OWNjZjdlYzA4MDdjMjhkYg==",
    'User-Agent': "PostmanRuntime/7.19.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "9e58d93d-8a03-4ead-972b-559b8775d6b1,e195269a-94ba-419b-9eed-65611dbbca3d",
    'Host': "a.blazemeter.com",
    'Accept-Encoding': "gzip, deflate",
    'Cookie': "bzm_sess=a49850b5873308c85fa9d8c702cd60ea",
    'Content-Length': "0",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

result_resp = requests.request("POST", url, headers=headers)
   

   if result_resp.ok:
        return result_resp.json()

    return None


if __name__ == '__main__':
    main()
