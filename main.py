#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from bson import ObjectId
from wsgiserver import WSGIServer
from sandbox.dbClient import client
import os

# db = client.lorem_ipsum


def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return ['WSGIserver is running!']
    # identity = ObjectId("5ef2149a3ffacd636cf254c2")
    # result = db.reviews.update_one({"_id": identity},
    #                                {
    #                                    "$inc": {"rating": 1},
    #                                    "$currentDate": {"operation.date." + str(os.getpid()): {"$type": "timestamp"}}
    #                                })
    # yield 'result'


wsgi_server = WSGIServer(app, port=8080)
wsgi_server.start()
