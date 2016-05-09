import websocket
import threading


class WSThread(threading.Thread):
    loop = True
    def __init__(self, ws):
        super(WSThread, self).__init__()
        self.ws = ws

    def close(self):
        self.loop = False

def connect(name):
    return TestWSThread(websocket.create_connection("{url}/test/".format(url=settings.URL), header={"User":name, "Type":"receiver"}))


if __name__ == "__main__":
    import settings
    from importlib import import_module

    THREADS = []
    for appname in settings.APPLICATIONS:
        mod = import_module(appname +".app")
        header = {"Type" : "receiver"}
        header.update(mod.WSThread.ACCOUNT)
        client = websocket.create_connection("{0}{1}".format(
            settings.URL,
            mod.WSThread.URL
            ), header=header)
        thread = mod.WSThread(client)
        thread.start()
    #     print(" === connect {} === ".format(i))

