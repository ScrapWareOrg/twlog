#!/home/twinkle/venv/bin/python

import inspect
import traceback

from datetime import datetime

######################################################################
# LIBS

from twlog.util.Code import *

######################################################################
# VARS
strf_styles = ['%', '$', '{']

######################################################################
# Classes - Formatter

class Formatter():
    def __init__(self, fmt="%(message)s", datefmt="[%Y-%m-%d %H:%M:%S]", style='%', validate=True, *, defaults=None) -> None:
        super(Formatter, self).__init__()
        # Formats
        self.datefmt = str(datefmt) if datefmt is not None else "[%Y-%m-%d %H:%M:%S]"
        self.fmt = str(fmt) if fmt is not None else "%(message)s"
        self.style = str(style) if style is not None and style in strf_styles else "%"
    def formatMessage(self, record):
        record["message"] = record.getMessage()
        temp = str(self.fmt)
        if self.style == '$':
            for key in record.keys():
                temp = self.fmt.replace(f"$\x7bkey\x7ds", "{record[key]}")
        elif self.style == '{':
            temp = f"{temp}"
        else:
            for key in record.keys():
                temp = temp.replace(f"%({key})s", f"{record[key]}")
        record["message"] = temp
    # datetime
    def fomatTime(self, record, datefmt=None):
        dt = datetime.now()
        record["asctime"] = dt.strftime(datefmt)
        return record["asctime"]
    def formatException(self, exc_info):
        return True
    def formatStack(self, stack_info):
        return traceback.extract_stack(f=inspect.stack(), limit=1)
    def formatHeader(self, records):
        return records
    def formatFooter(self, records):
        return records
    # Gate
    def format(self, record):
        # %(asctime)s
        self.fomatTime(record, datefmt=self.datefmt)
        # %(message)s
        self.formatMessage(record)
        # ^^;
        return record

class BufferingFormatter(Formatter):
    def __init__(self, linefmt=None, *args, **kwargs) -> None:
        super(BufferingFormatter, self).__init__(*args, **kwargs)
        # Formats
        self.linefmt = str(linefmt) if linefmt is not None else None
    def formatHeader(self, records):
        return records
    def formatFooter(self, records):
        return records

######################################################################
# MAIN
if __name__ == "__main__":
    print(f"[{__name__}]")
    print(__doc__)

#=====================================================================
# ALL - Make it directly accessible from the top level of the package
__all__ = ["Formatter", "BufferingFormatter"]

""" __DATA__

__END__ """
