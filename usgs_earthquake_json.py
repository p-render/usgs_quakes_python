# Earthquake!
# Python data feeds, parsing and processing JSON from USGS
# info at http://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php

import urllib2
import json

def printResults(data):
  # json module loads the string data into a dictionary
  quakes = json.loads(data)
  
  # access the contents of the JSON like any other Python object
  if "title" in quakes["metadata"]:
    print quakes["metadata"]["title"]
  
  # output the number of events, plus the magnitude and each event name  
  count = quakes["metadata"]["count"];
  print str(count) + " events recorded"
  print " "
  
  # for each event, print the place where it occurred
  for i in quakes["features"]:
    print i["properties"]["place"]
    
  print "--"

  # for each event in Alaska, print the place where it occurred
  """for i in quakes["features"]:
    if quakes["properties"]["place"].__contains__("Alaska") == true:
      print "%2.1f" % i["properties"]["mag"], i["properties"]["place"]
    
  print "--" """ #Not finding a good way weed out only Alaska earthquakes (.find or __contains__)

  # print the events that only have a magnitude greater than 4
  print "4.0+ Earthquakes"
  print " "
  for i in quakes["features"]:
    if i["properties"]["mag"] >= 4.0:
      print "%2.1f" % i["properties"]["mag"], i["properties"]["place"]
  print "--"

  # print only the events where at least 1 person reported feeling something, 
  # DYFI? Citizen Science - http://earthquake.usgs.gov/research/dyfi/
  print "Events that were felt:"
  print " "
  for i in quakes["features"]:
    feltReports = i["properties"]["felt"]
    if (feltReports != None) & (feltReports > 0):
        print "%2.1f" % i["properties"]["mag"], i["properties"]["place"], " reported " + str(feltReports) + " times"
  print "--"
  
def main():
  # variable to hold the source URL
  # free data feed from the USGS lists all earthquakes for the last day larger than Mag 2.5
  urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_week.geojson"
  
  # Opens the URL and read the data
  webUrl = urllib2.urlopen(urlData)
  print (webUrl.getcode())
  if (webUrl.getcode() == 200):
    data = webUrl.read()
    # print out results
    printResults(data)
  else:
    print "Received an error from server, cannot retrieve results " + str(webUrl.getcode())

if __name__ == "__main__":
  main()

  #Next... refer to in a html file, or in combo with a KML map  (adjusted from Lynda.com Python course)