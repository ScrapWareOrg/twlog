#!/home/twinkle/venv/bin/python

import os
import sys

import time
import locale

import inspect
import traceback

import asyncio
import threading

######################################################################
# LIBS

from twlog.util.Code import *

######################################################################
# VAR

_startTime = time.time()

######################################################################
# Classes - LogRecord

class LogRecord(object):
    def __init__(self, name=None, level=None, pathname=None, lineno=None, msg=None, exc_info=None, func=None, extra=None, sinfo=None, *args, **kwargs) -> dict:
        super(LogRecord, self).__init__(*args, **kwargs)
        curr = time.time()
        self.name            = name
        self.level           = level                           # %(levelname)s
        self.levelname       = LEVEL_LOG[level]                # %(levelname)s
        self.levelno         = level                           # %(levelno)s
        self.pathname = pathname
        try:
            self.filename     = os.path.basename(pathname)
            self.module       = os.path.splitext(self.filename)[0]
        except:
            self.filename     = pathname
            self.module       = 'unknown'
        #self.module          = None                            # %(module)s
        self.stack_info       = sinfo
        #self.lineno          = lineno                          # %(lineno)s
        self.lineno           = lineno
        self.funcName         = func
        # exc_info
        if exc_info is True:
            sexc_type, exc_value, exc_traceback = sys.exc_info()
            self.exc_info    = (sexc_type, exc_value, exc_traceback)
        else:
            self.exc_info = None
        self.exc_text = None                                   # %(exc_text)s
        
        self.args            = args                            # %(args)s
        self.asctime         = None                            # %(asctime)s
        self.created         = curr                            # %(created)
        self.relativeCreated = (curr- _startTime) * 1000       # %(created)
        #self.filename        = filename                        # %(filename)s
        #self.funcName        = None                            # %(funcName)s
        self.message         = None                            # %(message)s
        self.msecs           = int((curr - curr) * 1000) + 0.0 # %(msecs)s
        self.msg             = str(msg)
        self.name            = str(name)                       # %(name)s
        #self.pathname        = pathname                        # %(pathname)s
        self.process         = os.getpid()                     # %(process)s
        # if wants Limit Break(1) -> use and replace for psutio and other modules.
        try:
            self.processName = os.path.basename(sys.argv[0])   # %(processName)s
        except:
            self.processName = 'python'                # %(processName)s
        self.relativeCreated = os.getppid()                    # %(relativeCreated)s
        self.thread          = threading.get_ident()           # %(thread)s
        self.threadName      = threading.current_thread().name # %(threadName)s
        # Limit Break (2)
        #self.taskName = None
        try:
            task = asyncio.current_task()
            self.taskName = task.get_name() if task else None
        except Exception:
            self.taskName = None
    # getMessage()
    def getMessage(self):
        return self.msg % self.args

######################################################################
# MAIN
if __name__ == "__main__":
    print(f"[{__name__}]")
    print(__doc__)

#=====================================================================
# ALL - Make it directly accessible from the top level of the package
__all__ = ["LogRecoprd"]

""" __DATA__

__END__ """
