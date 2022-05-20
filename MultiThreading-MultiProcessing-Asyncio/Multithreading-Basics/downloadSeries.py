from threading import Thread
import os

# download series using python mutlithreading

# wget is command-line utility to retrieve content from web server. must be installed in you machine.
def download(link):
    os.system(f'wget {link}')

links = []
for i in range(10):
    links.append(f'https://dl3.3rver.org/hex1/Series/Titans/S01/Titans.S01E0{i}.480p.HexDL.com.mkv')

threads = []
for link in links:
    thread = Thread(target=download, args=(link,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
