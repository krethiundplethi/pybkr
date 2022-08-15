'''
Created on 14.08.2022

@author: AndreasFellnhofer
'''
import logging
import argparse
from urllib.parse import urlparse
import ibapi.client
import ibapi.wrapper


class Callbacks(ibapi.wrapper.EWrapper):
    def __init__(self):
        ibapi.wrapper.EWrapper.__init__(self)
        
    def error(self, id, errorCode, errorMsg, advancedOrderRejectJson):
        print(f"ERROR: {id} {errorCode}, {errorMsg}")    


def main(url):
    purl = urlparse(url)
    hostname = purl.hostname
    port = purl.port
    connected = False
    
    print(f'Try to connect to {hostname}:{port}...')  # will not print anything
    cb = Callbacks()
    client = ibapi.client.EClient(cb)
    print("Connect...")
    try:
        client.connect(hostname, port, 0)
        connected = True
    except:
        connected = False

    if connected:        
        print("Start api...")
        client.startApi()
        client.run()
    else:
        print("ERROR: Could not connect")
        exit(1)


if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description='IBKR TWS API demo')
    parser.add_argument('--host', dest='host', default="localhost:7497",
                    help='host and port (default: localhost:7497)')

    args = parser.parse_args()
    main("ibkr://" + args.host)