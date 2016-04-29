import ws

class WSThread(ws.WSThread):
    URL = ""
    ACCOUNT = {
            "User": "",
            "Secret": "",
            }

    def run(self):
        while self.loop:
            pass
