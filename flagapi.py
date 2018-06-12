import requests
import logging
import socket


def post(flag, scriptname):
    HOST = 'submission.faustctf.net'
    PORT = 666
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.send(flag)
        response = s.recv(2048)
    
    logging.info('SCRIPT: {script}, FLAG: {flag}, RESPONSE: {response}'.format(script=scriptname, flag=flag, response=response))


post('scritps','help')

