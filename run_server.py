from falcon_cors import CORS
# from src.meal import *
import falcon
import json
import os

from src.cors.meal import get_content

class GetContent(object):

    def on_get(self, req, resp):
        '''
        '''
        menu = get_content()
        result = {
            'code': 200,
            'content': {
                'r': menu
            },
            'message': 'success'
        }
        resp.body = json.dumps(result)
        resp.status = falcon.HTTP_200

class Order(object):

    def on_post(self, req, resp):
        '''
        '''
        # print(req.params)
        # print(req.headers)
        content = req.get_param('content', '')
        num = req.get_param('num', '')
        strTime = req.get_param('strTime', '')
        remark = req.get_param('remark', '')
        totalprice = req.get_param('totalprice', '')
        print(content, num, strTime, remark, totalprice)
        result = {
            'code': 200,
            'content': {
                'r': '请求成功'
            },
            'message': 'success'
        }

        resp.body = json.dumps(result)
        resp.status = falcon.HTTP_200

class Suggestion(object):

    def on_post(self, req, resp):
        '''
        '''
        suggestion = req.get_param('suggestion', '')
        print(suggestion)
        result = {
            'code': 200,
            'content': {
                'r': '请求成功'
            },
            'message': 'success'
        }

        resp.body = json.dumps(result)
        resp.status = falcon.HTTP_200 

public_cors = CORS(allow_all_origins=True,
                   allow_all_headers=True, allow_all_methods=True)

application = falcon.API(middleware=[public_cors.middleware])
application.req_options.auto_parse_form_urlencoded=True
# router
application.add_route('/api/content/', GetContent())
application.add_route('/api/order/', Order())
application.add_route('/api/suggestion/', Suggestion())