from bot import spotify
import threading, os, time, sys

lock = threading.Lock()
counter = 0
proxies = []
proxy_counter = 0
spotify_profile = str(input("\033[96m> \033[92mUsername or Link\n\033[96m> "))
threads = (int("500"))
with open("username.txt", "w") as f:
  f.write(input("\033[96m> \033[92minput follower name\n\033[96m> "))
  proxyfile = str(input("\033[96m> \033[92mProxy File\n\033[96m> "))
  threads = int(input("\033[96m> \033[92mThreads (recommended 500 for no errors)\n\033[96m> "))

def load_proxies():
    if not os.path.exists(proxyfile):
        print(f"\n\033[91mFile {proxyfile} not found")
        time.sleep(10)
        os._exit(0)
    with open(f"{proxyfile}", "r", encoding = "UTF-8") as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            proxies.append(line)
        if not len(proxies):
            print(f"\n\033[91mNo proxies loaded in {proxyfile}")
            time.sleep(10)
            os._exit(0)

load = int(1)
if load == 1:
    load_proxies()

def safe_print(arg):
    lock.acquire()
    print(arg)
    lock.release()

def thread_starter():
    global counter
    if load == 1:
        obj = spotify(spotify_profile, proxies[proxy_counter])
    else:
        obj = spotify(spotify_profile)
    result, error = obj.follow()
    if result == True:
        counter += 1
        safe_print("\033[96m> \033[92mSent Request to api.spotify.com \033[96m| \033[92mFollowed {} ".format(counter))
        print(f'\33]0;Followed {counter}\a', end='')
        sys.stdout.flush()
    else:
        safe_print(f"\033[96m> \033[91mError {error}")

while True:
    if threading.active_count() <= threads:
        try:
            threading.Thread(target = thread_starter).start()
            proxy_counter += 1
        except:
            pass
        if len(proxies) <= proxy_counter: #Loops through proxy file
            proxy_counter = 0
