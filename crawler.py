import urllib2
import MySQLdb
response = urllib2.urlopen("http://www.sina.com")
print response.read()
