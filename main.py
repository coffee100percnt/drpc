import pypresence
import time
import config

class RPC():
    def __init__(self, clientid):
        self.clientid = clientid
    def up(self):
        rpclient = pypresence.Presence(client_id=self.clientid)
        rpclient.connect()

        rpclient.update(buttons=config.buttons, 
                        details=config.details) # you can add large_image, large_text

rpc = RPC(config.clientid)
rpc.up()

while True:
    time.sleep(60)