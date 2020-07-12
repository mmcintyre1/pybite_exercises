from datetime import datetime
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated.'

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, 'log')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/messages.log',
    logfile
)

with open(logfile) as f:
    loglines = f.readlines()


def convert_to_datetime(line):
    """
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    _, raw_date, *_ = line.split(' ')
    return datetime.strptime(raw_date, '%Y-%m-%dT%H:%M:%S')


def time_between_shutdowns(loglines):
    """
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    shutdown_events = []
    for line in loglines:
        level, raw_date, caller, msg = line.split(" ", 3)
        msg = msg.strip()
        if msg == SHUTDOWN_EVENT:
            shutdown_events.append(convert_to_datetime(line))

    return max(shutdown_events) - min(shutdown_events)


if __name__ == '__main__':
    print(time_between_shutdowns(loglines))
