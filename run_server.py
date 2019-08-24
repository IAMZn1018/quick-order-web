from falcon_cors import CORS
import falcon
import json
import os

from src.cors.meal import get_content

class GetContent(object):

    def on_get(self, req, resp, filename):
        '''
        '''
        menu = get_content(filename)

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

def handle_404(req, resp):
    result = {
            'code': 404,
            'content': {
                'r': '请求路径错误'
            },
            'message': 'fail'
        }

    resp.status = falcon.HTTP_404
    resp.body = json.dumps(result)

def handle_500(req, resp):
    result = {
            'code': 500,
            'content': {
                'r': '服务器内部错误'
            },
            'message': 'fail'
        }
        
    resp.status = falcon.HTTP_500
    resp.body = json.dumps(result)


public_cors = CORS(allow_all_origins=True,
                   allow_all_headers=True, allow_all_methods=True)

application = falcon.API(middleware=[public_cors.middleware])
application.req_options.auto_parse_form_urlencoded=True
# router
application.add_route('/api/{filename}/', GetContent())
application.add_route('/api/order/', Order())
application.add_route('/api/suggestion/', Suggestion())

application.add_sink(handle_404, '')
application.add_sink(handle_500, '')