#!/usr/bin/env python

"""
fork from : https://github.com/kennethreitz/background.git
创建多实例任务对象,一个任务下可以绑定多个work,每个任务下的回调单独绑定到work上

"""

import multiprocessing
import concurrent.futures
from functools import wraps


def default_n():
    return multiprocessing.cpu_count()

n = default_n()
pool = concurrent.futures.ThreadPoolExecutor(max_workers=n)

pool._max_workers = n
pool._adjust_thread_count()

callbacks = []
results = []

class Background:
    def __init__(self):
        self._callbacks = []
        self._futures = []

    def task(self,f):
        @wraps(f)
        def wrapper(*args,**kwargs):
            _future = pool.submit(f, *args, **kwargs)
            self._futures.append(_future)
            for callback in self._callbacks:
                _future.add_done_callback(callback)
            return _future
        return wrapper

    def callback(self,f):
        self._callbacks.append(f)
        @wraps(f)
        def wrapper(*args,**kwargs):
            f(*args,**kwargs)
        return wrapper
    

