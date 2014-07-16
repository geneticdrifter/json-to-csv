import json
import urllib2
import csv
import MimeWriter
import os, sys
import password

print 'fetching data...'

data = "groupondata.csv"
page = json.load(urllib2.urlopen("http://partner-api.groupon.com/v1/orders.json?clientId=%s&startDate=01-04-2014&endDate=30-04-2014" % (password.key)))
report = page["data"]["records"]

#print 'data received'
#print 'building csv...'

with open(data, 'w') as csvfile:
	writer = csv.writer(csvfile, delimiter=",")
	writer.writerow(['date', 'order value', 'commission', 'sid', 'orders', 'orderID'])
	for record in report:
		writer.writerow([record['date'],record['grossMinorUnits'],record['commissionMinorUnits'],record['sid'],record['orders'],record['orderId']])

#print 'opening file...'
#os.open('groupondata.csv', os.O_RDWR)

print 'Go get your commission data!'
