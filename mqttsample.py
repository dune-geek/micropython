#
# AWS IOT Client Test for ESP32  with MicroPython (20220716)
#
from umqtt.simple import MQTTClient

ENDPOINT = b'xxxxxxxxx.amazonaws.com'    # set ENDPOINT  URL (Amazon IoT Core)
ID = '_SET_YOUR_ID_'                     # set your device ID
TOPIC = "_SET_TOPIC_"                    # set topic

KEYFILE = '/certs/private.pem.key'        # set private key
CERTFILE = "/certs/certificate.pem.crt"   # set cert file

def _cb(topic, msg):
    print("-------- call back ----------")
    print(f"topic:{topic}")
    print(f"msg:{msg}")
    print("-----------------------------")

with open(KEYFILE, 'r') as f:
    key = f.read()

with open(CERTFILE, 'r') as f:
    cert = f.read()

# SSL certificates.
SSL_PARAMS = {'key': key, 'cert': cert, 'server_side': False}
client = MQTTClient(client_id=ID, server=ENDPOINT, port=8883, ssl=True, ssl_params=SSL_PARAMS)

client.set_callback(_cb)
client.connect()
client.subscribe(topic=TOPIC)

while True:
   print("---loop---------------")
   client.wait_msg()
