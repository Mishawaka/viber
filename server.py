from http.server import HTTPServer, SimpleHTTPRequestHandler, HTTPStatus
import ssl
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages.text_message import TextMessage

bot_configuration = BotConfiguration(
	name='AtomSpace',
	avatar='https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjy2sPww_ffAhWMpIsKHZdkC58QjRx6BAgBEAU&url=http%3A%2F%2Fodessa.net.ua%2Fnews%2Fv-odesse-vpervye-otkroet-svoi-dveri-atom-space&psig=AOvVaw2h8rp8WdUXn9-RUbLUkNIq&ust=1547906902440090',
	auth_token='4918542585e7d307-571b9f239ed4f865-17485e2f067277a3'
)
viber = Api(bot_configuration)
# given a pem file ... openssl req -new -x509 -keyout yourpemfile.pem -out yourpemfile.pem -days 365 -nodes

httpd = HTTPServer(('localhost', 4444), SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, server_side=True,
                                certfile='cert.pem', keyfile='key.pem')

viber.set_webhook('localhost:4444')

httpd.serve_forever()