from numba import jit, cuda
import time
import sys,subprocess,time
from timeit import default_timer as timer
from threading import Thread
from builtins import super
import csv
import numpy as np
import matplotlib.pyplot as plt
from pandas import *


_thread_target_key, _thread_args_key, _thread_kwargs_key = (
    ('_target', '_args', '_kwargs')
    if sys.version_info >= (3, 0) else
    ('_Thread__target', '_Thread__args', '_Thread__kwargs')
)

class ThreadWithReturn(Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._return = None
    
    def run(self):
        target = getattr(self, _thread_target_key)
        if target is not None:
            self._return = target(
                *getattr(self, _thread_args_key),
                **getattr(self, _thread_kwargs_key)
            )
            
    def join(self, *args, **kwargs):
        super().join(*args, **kwargs)
        return self._return
    
def ave(arr):
  sum=0
  for item in (arr):
    sum = sum + item
  return round(sum/len(arr))


player_list = ['WMP', 'VLC', 'WMPC', 'KMP']
player_name = player_list[1]

codec_list = ['flv', '3gp', 'mkv', 'mp4']
codec_name = codec_list[0]


@jit(target_backend='cuda',forceobj=True)
def counter_loop():
  loop_len = 8         # [4 second]
  timeout = 0.01        # [10 mil seconds]
  counter_arr = []
  loop_start = timer()
  while loop_len > timer() - loop_start :
    counter = 0
    timeout_start = timer()
    while timeout > timer() - timeout_start :
      counter +=1
    counter_arr.append(counter)
  return counter_arr


@jit(target_backend='cuda',forceobj=True)
def WMP():
    p = subprocess.Popen("C:\\Program Files\\Windows Media Player\\wmplayer.exe E:\\Videos\\sample.mp4")
    time.sleep(5)
    p.kill()
    
@jit(target_backend='cuda',forceobj=True)
def WMPC():
      p = subprocess.Popen("C:\\Program Files (x86)\\K-Lite Codec Pack\\MPC-HC64\\mpc-hc64.exe E:\\Videos\\sample.mp4")
      time.sleep(5)
      p.kill()
      
@jit(target_backend='cuda',forceobj=True)
def VLC():
    p = subprocess.Popen("C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe E:\\Videos\\sample.mp4")
    time.sleep(5)
    p.kill()

@jit(target_backend='cuda',forceobj=True)
def KMP():
      p = subprocess.Popen("C:\\Program Files\\KMPlayer 64X\\KMPlayer64.exe  E:\\Videos\\sample.mp4")
      time.sleep(5)
      p.kill()

th_loop = ThreadWithReturn(target=counter_loop)
th_media =  ThreadWithReturn(target= eval(player_name))

th_loop.start()
th_media.start()

result = th_loop.join()

csv_file_name = 'TestData\\' + player_name + '.csv'
with open(csv_file_name, 'a', newline = '') as csvfile:
    my_writer = csv.writer(csvfile, delimiter = ',')
    my_writer.writerow(result)


 
print('\n\nNumber of counter: ',len(result))
print('\nMin: ',min(result))
print('Max: ',max(result))
print('Ave: ',ave(result))

