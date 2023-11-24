import socket, json


class Network:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#ببین اطلاعاتی که در
 start دریافت می‌کنی رو باید داخل شیء ذخیره کنی تا بعدا‌ً قابل‌استفاده باشن. بنابراین در تابع __init__ یه self.data تعریف کن و برابر با دیکشنری خالی قرارش بده. بعد در start وقتی response رو دریافت کردی، با استفاده از json.loads به دیکشنری تبدیلش کن و داخل self.data بریزش.


 حالا داخل تابع send_data دیگه نیازی نداری که کانکت بشی، چون اطلاعات رو در self.data داری. سعی کن با این تغییرات، تابع send_data رو بازنویسی کنی. اگه مشکلت حل نشد یا بازم سؤالی بود، حتماً ازمون بپرس

    def start(self):
        self.s.connect((self.host, self.port))
        response = self.s.recv(1024).decode('ascii')
        with open('config.json', 'w') as outfile:
            outfile.write(response)

    def send_data(self, keys):
        self.s.connect((self.host, self.port))
        self.s.send(json.dump({'keys': keys, 'dead': False}))

    def get_data(self):
        response = str(self.s.recv(1024).decode('ascii')).replace('\'', '"')
        json_file = json.loads(response)
        return json_file['keys']