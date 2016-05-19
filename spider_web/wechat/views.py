# coding=utf-8
from django.shortcuts import render
from django.shortcuts import HttpResponse
from wechat.config import *
from wechat_sdk.basic import WechatBasic
from django.views.decorators.csrf import csrf_exempt


wechat = WechatBasic(token=WEIXIN_TOKEN, appid=WEIXIN_APPID,
                     appsecret=WEIXIN_APPSECRET)

@csrf_exempt
def main(request):
    if request.method == "GET":
        signature = request.GET.get("signature", None)
        timestamp = request.GET.get("timestamp", None)
        nonce = request.GET.get("nonce", None)
        echostr = request.GET.get("echostr", None)
    # 对签名进行校验, 微信服务器联通业务服务器
        if wechat.check_signature(signature=signature, timestamp=timestamp,
                                  nonce=nonce):
            return HttpResponse(echostr)
        else:
            return HttpResponse("weixin index")
    elif request.method == "POST":
        # 微信服务器发送过来的xml包体
        body_text = request.body
        # xml包体解析成dict,实例化Message类
        wechat.parse_data(body_text)
        message = wechat.get_message()
        response = None
        if message.type == 'text':
            if message.content == 'wechat':
                response = wechat.response_text(u'^_^')
            else:
                response = wechat.response_text(u'文字' + message.content)
        elif message.type == 'image':
            response = wechat.response_text(u'图片' + str(message.media_id))
        elif message.type == 'voice':
            response = wechat.response_text(u'语音' + str(message.media_id))
        elif message.type == 'shortvideo':
            response = wechat.response_text(u'小视频' + str(message.media_id))
        elif message.type == 'location':
            response = wechat.response_text(u'地理位置' + str(message.location))
        else:
            response = wechat.response_text(u'未知')
        return HttpResponse(response)


def create_menu(request):
    wechat.create_menu({
        'button': [
            {
                       'type': 'view',
                       'name': '明日头条',
                       'url': 'http://www.itcastcpp.cn/app/'
                       }
        ]})
    return HttpResponse("ok")


def index(request):
    return HttpResponse("hello")
