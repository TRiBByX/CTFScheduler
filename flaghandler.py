import time
import os
import sys
import logging

def main():
    logging.basicConfig(filename='flaglog.log', level=logging.INFO)
    while True:
        logging.info('-------------------------------------------! NEW TICK !-------------------------------------------')
        scriptexec()
        time.sleep(180)


def iplist():
    ips = open('ips.txt', 'r').read()
    ips = ips.split('\n')
    return ips

def scriptexec():
    for ip in iplist():
        for script in os.listdir('scripts/'):
            if script != 'Scriptslogs':
                execfile('scripts/'+script, globals={'ATK_IP': ip})











if __name__ == '__main__':
    main()