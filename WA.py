import urllib.request, urllib.parse, urllib.error
import json
import ssl

def url_service(url):
	# Ignore SSL certificate errors
	ctx = ssl.create_default_context()
	ctx.check_hostname = False
	ctx.verify_mode = ssl.CERT_NONE
	# URL handle and open
	url_handle = urllib.request.urlopen(url, context=ctx)
	data = url_handle.read().decode()
	jdata = json.loads(data)

