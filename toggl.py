#!/usr/bin/env python

import simplejason, urllib2, base64

class Toggl:
    URL = 'https://www.toggl.com/api/'
    API_VERSION = 'v6'

    def __init__(self, version='v6'):
        API_VERSION = version

    def send(self, req):
        """
        Sends requests to toggl
        """
        url = URL + API_VERSION + '/' + req
        request = urllib2.Request(url, None)
        request.add_header("Content-type", "application/json")

        res = urllib2.urlopen(request)
        result = simplejson.load(res)


if __name__ == "__main__":
    t = Toggl()
    t.send()
