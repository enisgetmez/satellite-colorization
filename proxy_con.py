import requests
import urllib.parse
import time
proxies = {
    'http': 'proxyurl:port',
}
s = requests.Session()
s.proxies = proxies

def proxy_get_image(url,name):
	url = urllib.parse.unquote(url.replace("https","http"))
	r = s.get(url,stream=True)
	with open("static/origin/"+name,'wb') as f:
		f.write(r.content)
		print(r.content)