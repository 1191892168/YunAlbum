import urllib3
import sys
import  urllib.request
import pip

import ssl

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=fEFvj23fUyK3Sq5PGslY9ufx&client_secret=IaBS3L4xGoHMqXllO40KWdFOyy1MMlgR'
request = urllib.request.Request(host)

request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib.request.urlopen(request)
content = response.read()
if (content):
    print(content)

