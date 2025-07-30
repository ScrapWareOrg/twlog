#!/home/twinkle/venv/bin/python

import os
import sys

import time
import locale

import inspect
import traceback

import asyncio
import threading

from datetime import datetime

######################################################################
# LIBS

from twlog.util.Code import *

######################################################################
# Classes - LogRecord

class LogRecord(dict):
    def __init__(self, name=None, level=None, fn=None, lno=None, msg=None, exc_info=False, func=None, extra=None, sinfo=None, *args, **kwargs) -> dict:
        super(LogRecord, self).__init__(kwargs)
        self["stack_info"]      = inspect.stack()
        self["module"] = str(self["stack_info"][1].frame.f_globals.get("__name__", "__main__"))
        self["funcName"] = func if func is not None else str(self["stack_info"][1].frame.f_code.co_name)
        self["pathname"] = str(self["stack_info"][1].filename)
        self["filename"] = os.path.basename(self["pathname"])
        self["lineno"] = lno if lno is not None else str(self["stack_info"][1].lineno)
        if not self["filename"].endswith(".py"):
            self["filename"] += ".py"
        self["args"]            = args                            # %(args)s
        self["asctime"]         = None                            # %(asctime)s
        self["created"]         = (time.time_ns()/1e-9)           # %(created)s
        self["exc_info"]        = sys.exc_info() if exc_info is True else None
        #self["filename"]        = filename                        # %(filename)s
        #self["funcName"]        = None                            # %(funcName)s
        self["level"]           = level                           # %(levelname)s
        self["levelname"]       = LEVEL_LOG[level]                # %(levelname)s
        self["levelno"]         = level                           # %(levelno)s
        #self["lineno"]          = lineno                          # %(lineno)s
        self["message"]         = None                            # %(message)s
        #self["module"]          = None                            # %(module)s
        self["msecs"]           = datetime.now().strftime("%f")   # %(msecs)s
        self["msg"]             = str(msg)
        self["name"]            = str(name)                       # %(name)s
        #self["pathname"]        = pathname                        # %(pathname)s
        self["process"]         = os.getpid()                     # %(process)s
        # if wants Limit Break(1) -> use and replace for psutio and other modules.
        try:
            self["processName"] = os.path.basename(sys.argv[0])   # %(processName)s
        except:
            self["processName"] = 'python'                # %(processName)s
        self["relativeCreated"] = os.getppid()                    # %(relativeCreated)s
        self["thread"]          = threading.get_ident()           # %(thread)s
        self["threadName"]      = threading.current_thread().name # %(threadName)s
        # Limit Break (2)
        #self["taskName"] = None
        try:
            task = asyncio.current_task()
            self["taskName"] = task.get_name() if task else None
        except Exception:
            self["taskName"] = None
    # getMessage()
    def getMessage(self):
        return self["msg"] % self["args"]

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
