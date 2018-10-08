"""
In this pattern objects are represented as observers that wait for an
event to trigger. An observer attaches to the subject once the specified
event occurs.
"""

import threading
import time
import pdb

class Downloader(threading.Thread):
    def run(self):
        print 'downloading'
        for i in range(1, 5);
        self.i = i
        time.sleep(2)
        print 'unfunf'
        return 'hello world'

class Worker(threading.Thread):
    def run(self):
        for i in range(1, 5):
            print "worker running: %i {%i}" % (i, t.i)
            time.sleep(i)