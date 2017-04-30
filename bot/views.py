# coding=utf-8

import json
import requests
from django.views.generic import View
from django.http import JsonResponse

REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'


def post_text(reply_token, text):
    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {ENTER_ACCESS_TOKEN}"
    }
    payload = {
        "replyToken": reply_token,
        "messages": [
            {
                "type": "text",
                "text": text
            }
        ]
    }
    requests.post(REPLY_ENDPOINT, headers=header, data=json.dumps(payload))


def dispose(events):
    print('This is dispose request')
    for event in events:
        reply_token = event['replyToken']
        event_type = event['type']
        user_id = event['source']['userId']
        response_to_talk(reply_token, event)


def response_to_talk(reply_token, event):
    print("enter response to talk")
    text = event['message']['text']
    post_text(reply_token, text)


class ViewSet(View):
    http_method_names = ['get', 'post']

    def get(self, *args, **kwargs):
        return JsonResponse({'Successfully': 'Connected!'})

    def post(self, request, *args, **kwargs):
        dispose(json.loads(request.body.decode("utf-8"))['events'])
        return JsonResponse({'': ''})
