#!/home/twinkle/venv/bin/python

import inspect
import traceback

from datetime import datetime

######################################################################
# LIBS

from twlog.util.ANSIColor import ansi
from twlog.util.Code import *
from twlog.Formatters import Formatter

######################################################################
# Classes - Formatter

class ANSIFormatter(Formatter):
    def __init__(self, fmt="%(asctime)s %(levelname)s %(message)s", datefmt="[%Y-%m-%d %H:%M:%S]", style='%', validate=True, defaults=None, markup=True, rich_tracebacks=True, *args, **kwargs) -> None:
        super(ANSIFormatter, self).__init__(fmt=fmt, datefmt=datefmt, style=style, validate=validate, defaults=defaults, *args, **kwargs)
        self.markup = True if markup is True else False
        self.rich_tracebacks = True if rich_tracebacks is True else False
    def formatLevelName(self, record):
        if record['level'] == DEBUG:
            temp = f"{ansi.start}{ansi.back_light_gray};{ansi.fore_white};{ansi.text_on_bold}m"
        elif record['level'] == WARN:
            temp = f"{ansi.start}{ansi.back_yellow};{ansi.fore_white};{ansi.text_on_bold}m"
        elif record['level'] == ERROR:
            temp = f"{ansi.start}{ansi.back_red};{ansi.fore_white};{ansi.text_on_bold}m"
        elif record['level'] == CRITICAL:
            temp = f"{ansi.start}{ansi.back_light_red};{ansi.fore_black};{ansi.text_on_bold}m"
        elif record['level'] == NOTICE:
            temp = f"{ansi.start}{ansi.back_green};{ansi.fore_white};{ansi.text_on_bold}m"
        elif record['level'] == ISSUE:
            temp = f"{ansi.start}{ansi.back_purple};{ansi.fore_white};{ansi.text_on_bold}m"
        elif record['level'] == MATTER:
            temp = f"{ansi.start}{ansi.back_light_white};{ansi.fore_black};{ansi.text_on_bold}m"
        else: # Defaults (INFO)
            temp = f"{ansi.start}{ansi.back_blue};{ansi.fore_white};{ansi.text_on_bold}m"
        record["levelname"] = f"{temp}" + record["levelname"] + f"{ansi.reset}"
    def formatMessage(self, record):
        # MarkUp?
        if self.markup is True:
            self.formatLevelName(record)
        # Get Message
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
        # DateTime
        dt = datetime.now()
        # MarkUp?
        if self.markup is True:
            # Initialize
            if record['level'] == DEBUG:
                temp = f"{ansi.start}{ansi.fore_white};{ansi.text_on_bold}m"
            elif record['level'] == WARN:
                temp = f"{ansi.start}{ansi.fore_light_yellow};{ansi.text_on_bold}m"
            elif record['level'] == ERROR:
                temp = f"{ansi.start}{ansi.fore_light_red};{ansi.text_on_bold}m"
            elif record['level'] == CRITICAL:
                temp = f"{ansi.start}{ansi.fore_red};{ansi.text_on_bold}m"
            elif record['level'] == NOTICE:
                temp = f"{ansi.start}{ansi.fore_light_green};{ansi.text_on_bold}m"
            elif record['level'] == ISSUE:
                temp = f"{ansi.start}{ansi.fore_light_magenta};{ansi.text_on_bold}m"
            elif record['level'] == MATTER:
                temp = f"{ansi.start}{ansi.fore_white};{ansi.text_on_bold}m"
            else: # Defaults (INFO)
                temp = f"{ansi.start}{ansi.fore_cyan};{ansi.text_on_bold}m"
            # Colorful DateTime
            record["asctime"] = f"{temp}" + dt.strftime(datefmt) + f"{ansi.reset}"
        else:
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
__all__ = ["ANSIFormatter"]

""" __DATA__

__END__ """
