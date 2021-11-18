from DeviceManager.protocols.coap import CoapClient


def cb(*args):
    print(*args)


c = CoapClient()
res = c.get("/", callback=cb)
print(res)
print("end")
