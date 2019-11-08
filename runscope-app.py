import requests
import json	
import urllib2

def JTLsWget(session_id):
	return requests.get('https://a.blazemeter.com/api/v4/sessions/r-v4-5dc512c104030/reports/logs/'.format(session_id), auth=('8cac46d7b462618937db5b75','83b720f2e2c405866b1769bb4582635542a684e548331a948308e2f89ccf7ec0807c28db')) 

res = JTLsWget("r-v4-5dc512c104030")
print res.json()

Json_String = res.json()
url = [entry for entry in Json_String['result']['data'] if entry['filename'] == 'jtls_and_more.zip'][0]['dataUrl']
print url
open('jtls_and_more.zip', 'wb').write(urllib2.urlopen(url).read())