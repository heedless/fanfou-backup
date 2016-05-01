# -*- coding:utf-8 -*-

import fanfou_api_key
consumer_key,consumer_secret = fanfou_api_key.get()

import get_token
oauth_token,oauth_token_secret = get_token.oauth2()

import urlparse,sys,urllib,re
import oauth2 as oauth
from urllib2 import Request,urlopen

def request_to_header(request, realm=''):
    """Serialize as a header for an HTTPAuth request."""
    auth_header = 'OAuth realm="%s"' % realm
    for k, v in request.iteritems():
        if k.startswith('oauth_') or k.startswith('x_auth_'):
            auth_header += ', %s="%s"' % (k, oauth.escape(str(v)))
    return {'Authorization': auth_header}

def get(page, url):
    params={}
    params['page']=page
    consumer = oauth.Consumer(consumer_key, consumer_secret)
    token = oauth.Token(oauth_token,oauth_token_secret)
    request = oauth.Request.from_consumer_and_token(consumer,
                                                token,                      
                                                http_url=url, 
                                                http_method='GET',     
                                                parameters=params    
                                                )
    signature_method = oauth.SignatureMethod_HMAC_SHA1()
    request.sign_request(signature_method, consumer, token)
    headers=request_to_header(request)
    data = {'page':page}
    data = urllib.urlencode(data)
    url = url + '?' + data
    resp = urlopen(Request(url=url, headers=headers))
    resp = resp.read()

    return resp
