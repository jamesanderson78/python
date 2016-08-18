# Example from Lynda.com

import urllib2
import json

def printResults(data):
    # use the json module to load the string data into a dictionary
    theJSON = json.loads(data)
    # access contents through the json library
    if "title" in theJSON["metadata"]:
        print theJSON["metadata"]["title"]

def main():
    # define a JSON source - USGS geological data 
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    webUrl = urllib2.urlopen(urlData)
    print webUrl.getcode()
    if (webUrl.getcode() == 200):
        data = webUrl.read()
        # print out the results
        printResults(data)
    else:
        print "Error: cannot retrieve results " + str(webUrl.getcode())



# Start program    
if __name__ == "__main__":
    main()