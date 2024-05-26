import os

def spyware():
    files = os.listdir('.')
    with open('log.txt', 'w') as f:
        for file in files:
            f.write(file + '\n')

if __name__ == '__main__':
    spyware()
