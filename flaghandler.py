import time
import os

def main():
    while True:
        scriptexec()
        time.sleep(180)


def scriptexec():
    for script in os.listdir('scripts/'):
        execfile('scripts/'+script)











if __name__ == '__main__':
    main()