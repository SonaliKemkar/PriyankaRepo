import requests

def testStart(test_id):
	return requests.post('https://a.blazemeter.com/api/v4/tests/7389741/start'.format(test_id), auth=('846d7b462618937db5b75','83b720f2e2c405866b1769bb4582635542a684e548331a948308e2f89ccf7ec0807c28db'))

res = testStart(7389741)
print res.json()
