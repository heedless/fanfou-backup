# -*- coding:utf-8 -*-
def oauth2():
    import os
    if os.path.exists('oauth2.db')== False:
        get_token()

    import sqlite3
    conn = sqlite3.connect('oauth2.db')
    c = conn.cursor()
    c.execute('''select * from token''')
    oauth_token,oauth_token_secret = c.fetchone()
    conn.close()

    return oauth_token,oauth_token_secret



import urlparse
import oauth2 as oauth
import sys,urllib,re
from urllib2 import Request,urlopen
def get_token():
    import fanfou_api_key
    consumer_key,consumer_secret = fanfou_api_key.get()

    request_token_url = 'http://fanfou.com/oauth/request_token'
    access_token_url = 'http://fanfou.com/oauth/access_token'
    authorize_url = 'http://fanfou.com/oauth/authorize'

    ''' get the token '''
    consumer = oauth.Consumer(consumer_key, consumer_secret)
    client = oauth.Client(consumer)
    resp, content = client.request(request_token_url,"GET")
    if resp['status'] != '200':
        raise Exception("Invalid response %s. " % resp['status'])
    request_token = dict(urlparse.parse_qsl(content))
    print "    - oauth_token        = %s" % request_token['oauth_token']
    print "    - oauth_token_secret = %s" % request_token['oauth_token_secret']

    ''' get the oauth_token '''
    print "Go to the following link in your browser:"
    print "%s?oauth_token=%s&oauth_callback=oob" % (authorize_url, request_token['oauth_token'])

    accepted = 'n'
    while accepted.lower() == 'n':
        accepted = raw_input('Have you authorized me? (y/n) ')
    oauth_verifier = raw_input('What is the PIN? ')

    token = oauth.Token(request_token['oauth_token'],
                            request_token['oauth_token_secret'])
    token.set_verifier(oauth_verifier)
    client = oauth.Client(consumer, token)

    resp, content = client.request(access_token_url, "GET")
    if resp['status'] != '200':
        raise Exception("Invalid response %s." % resp['status'])
    access_token = dict(urlparse.parse_qsl(content))
    print "Access Token:"
    print "    - oauth_token        = %s" % access_token['oauth_token']
    print "    - oauth_token_secret = %s" % access_token['oauth_token_secret']
    print "You may now access protected resources using the access tokens above." 
    oauth_token        = access_token['oauth_token']
    oauth_token_secret = access_token['oauth_token_secret']

    ''' write into database '''
    import sqlite3
    conn = sqlite3.connect('oauth2.db')
    c = conn.cursor()
    c.execute('create table token(oauth_token varchar(100),oauth_token_secret varchar(100))')
    c.execute("insert into token(oauth_token,oauth_token_secret) values(?,?)",
          [oauth_token,oauth_token_secret])
    conn.commit()
    conn.close()


