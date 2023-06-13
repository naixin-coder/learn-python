# 标准库
import shutil
import os
import math
from urllib.request import urlopen
from datetime import date, datetime

# import threading
from threading import Thread
import zipfile
# help(os)
print(os.name)
print(os.path)


shutil.copyfile('input-text.txt', 'input-text2.txt')

print(math.ceil(1.321))

# with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
#     # print(response)
#     for line in response:
#         print(f'{line}')

now = date.today()
print(now)

print(datetime.today().second)


# 多线程
class AsyncZipFile(Thread):
    # infile = ''

    def __init__(self, infile, outfile):
        Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)


zipFile = AsyncZipFile('input-text.txt', 'input-text.zip')
zipFile.start()
print('The main program continues to run in foreground.')
zipFile.join()
print('Main program waited until background was done.')
