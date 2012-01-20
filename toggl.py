#!/usr/bin/env python
#
# toggl.py
# Nick Loadholtes <nick@ironboundsoftware.com>
#
# This class is a thin wrapper around the toggl.com api
# and is useful for pulling JSON formatted data from
# toggl.

import simplejson, urllib2, base64, sys, logging

class Toggl:
    URL = 'https://www.toggl.com/api/'
    API_VERSION = 'v6'

    def __init__(self, api_token, api_version='v6'):
        API_VERSION = api_version
        self.api_token = api_token

    def send(self, req):
        """
        Sends requests to toggl
        """
        url = self.URL + self.API_VERSION + '/' + req
        request = urllib2.Request(url, None)
        request.add_header('Content-type', 'application/json')
        authstr = base64.encodestring('%s:%s' % (self.api_token, 'api_token')).replace('\n', '')
        request.add_header('Authorization', authstr)

        res = urllib2.urlopen(request)
        result = simplejson.load(res)
        return result


if __name__ == '__main__':
    """
    This main method serves as a test/example usage of this lib.
    """
    args = sys.argv
    if len(args) == 1:
        logging.error("\n\nYou need to pass in a toggl.com api key! \n\n")
    else:
        t = Toggl(args[1])
        print(t.send('me.json'))
