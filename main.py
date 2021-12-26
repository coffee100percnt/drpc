import pypresence
import time

def uptime():
    global boottime
    f = open('/proc/stat', 'r')
    for line in f:
        if line.startswith('btime'):
            boottime = int(line.split()[1])
    return int(boottime)

class RPC():
    def __init__(self, clientid):
        self.clientid = clientid
    def up(self):
        rpclient = pypresence.Presence(client_id=self.clientid)
        rpclient.connect()
        rpclient.update(buttons=[{"label": "скачать", "url": "https://kernel.org"}], start=uptime(), details="Free and open source kernel", large_image="tux", large_text="Tux, Linux kernel mascot")

rpc = RPC("924639041285144618")
rpc.up()

while True:
    time.sleep(60)