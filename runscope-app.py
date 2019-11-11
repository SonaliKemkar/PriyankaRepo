import requests

def testStart(test_id):
	return requests.post('https://a.blazemeter.com/api/v4/tests/7389741/start'.format(test_id), auth=('id','secret'))

res = testStart(7389741)
print res.json()
