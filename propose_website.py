#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
from xml.dom.minidom import parse, parseString
# import xml.etree.ElementTree as ET


def main():
    host = 'localhost'
    port = 10500

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    try:
        data = ''
        while True:
            if '</RECOGOUT>\n.' in data:
                print(data)
                data = ''
                # root = ET.fromstring(
                #     '<?xml version="1.0"?>\n' + data[data.find(
                #         '<RECOGOUT>'):].replace('\n.', ''))
                # for whypo in root.findall('./SHYPO/WHYPO'):
                #     command = whypo.get('WORD')
                #     score = float(whypo.get('CM'))
                #
                #     if command == u'おはよう' and score >= 0.9:
                #         # ここにおはよう処理
                #
                data = ''

            else:
                data = data + client.recv(1024).decode('utf-8')
    except KeyboardInterrupt:
        client.close()


if __name__ == "__main__":
    main()
