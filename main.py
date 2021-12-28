import pypresence
import time

class RPC():
    def __init__(self, clientid):
        self.clientid = clientid
    def up(self):
        rpclient = pypresence.Presence(client_id=self.clientid)
        rpclient.connect()
        rpclient.update(buttons=[{"label": "Label", "url": "URL"}], 
                        details="Details")

rpc = RPC("Client ID")
rpc.up()

while True:
    time.sleep(60)