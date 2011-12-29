
import simplejason, urllib2, base64

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
        print(results)


if __name__ == '__main__':
    t = Toggl()
    t.send()
