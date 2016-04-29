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

    THREADS = []
    for appname in settings.APPLICATIONS:
        mod = __import__(appname +".ws")
        header = {"Type" : "receiver"}
        header.update(mod.ws.WSThread.ACCOUNT)
        client = websocket.create_connection("{0}{1}".format(
            settings.URL,
            mod.ws.WSThread.URL
            ), header=header)
        thread = mod.ws.WSThread(client)
        thread.start()
    #     print(" === connect {} === ".format(i))

    # import sys
    # if len(sys.argv) > 1:
    #     connect(sys.argv[1]).start()
    # else:
    #     ws1 = websocket.create_connection("ws://localhost:8080/test/", header={"User":"ctare", "Type":"sender"})
    #     ws1.send("YO")

    # ws2 = websocket.create_connection("ws://localhost:8080/test/", header={"User":"ctare", "Type":"receiver"})
    # ws3 = websocket.create_connection("ws://localhost:8080/test/", header={"User":"ctare", "Type":"receiver"})
    # print("ws1: " + ws2.recv())
    # print("ws1: " + ws2.recv())
    # print("ws1: " + ws2.recv())
    # # print("ws2: " + ws2.recv())
    # print("ws3: " + ws3.recv())
    # thread = WSThread(ws)
    # thread.start()
