from django.http import HttpResponse


#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

import urllib.request
import urllib.parse
import json

from django.http import HttpResponse
# make a GET request and parse the returned JSON
# note, no timeouts, error handling or all the other things needed to do this f or real

def index(request):

        req = urllib.request.Request('http://172.17.0.3:8000/') #is this a long term solution? hard coding the IP
        #req = urllib.request.Request('https://api.github.com/users/mralexgray/repos')
        
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)
        return(HttpResponse(resp))
        #return(HttpResponse("hi"))
                    
