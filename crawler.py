import urllib2
response = urllib2.urlopen("http://www.sina.com")
print response.read()
