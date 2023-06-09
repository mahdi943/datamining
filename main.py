import subprocess
import time


for i in range (3):
    print("Running ... ", i)
    p = subprocess.Popen("python loop.py")
    time.sleep(10)
##    p.kill()


print('Done!')


