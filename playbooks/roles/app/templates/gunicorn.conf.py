import os


def get_workers():
    procs = os.sysconf('SC_NPROCESSORS_ONLN')
    if procs > 0:
        return procs * 2 + 1
    else:
        return 3


bind = '0.0.0.0:8000'

workers = get_workers()
worker_class = 'gevent'

max_requests = 1000
timeout = 30
keep_alive = 2

daemon = False
preload = True
