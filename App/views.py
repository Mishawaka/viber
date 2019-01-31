from django.shortcuts import render, HttpResponse

from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages.text_message import TextMessage

bot_configuration = BotConfiguration(
	name='AtomSpace',
	avatar='https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjy2sPww_ffAhWMpIsKHZdkC58QjRx6BAgBEAU&url=http%3A%2F%2Fodessa.net.ua%2Fnews%2Fv-odesse-vpervye-otkroet-svoi-dveri-atom-space&psig=AOvVaw2h8rp8WdUXn9-RUbLUkNIq&ust=1547906902440090',
	auth_token='4918542585e7d307-571b9f239ed4f865-17485e2f067277a3'
)
viber = Api(bot_configuration)
# viber.set_webhook('localhost:8000')


def index(request):
    index = viber.get_online(['380687895412'])
    viber.send_messages('380687895412', TextMessage(text='Hello'))
    return HttpResponse('Status: {}'.format(index))