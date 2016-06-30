
import webapp2
import json


class ParkInfo(webapp2.RequestHandler):
    def get(self):
    	jObject = json.loads('{"one" : "1", "two" : "2", "three" : "3"}')
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(jObject)

app = webapp2.WSGIApplication([
    ('/parkinfo', ParkInfo),
], debug=True)
