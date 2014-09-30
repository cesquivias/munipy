"""Create a message for the LED sign to display current date and time."""

from datetime import datetime

def datetime_message(dt=None):
    now = dt if dt else datetime.now()
    return (now.strftime('%A, %b %-d'),
            now.strftime('%-I:%M %p'))

if __name__ == '__main__':
    now = datetime(2014, 9, 30, 13, 25, 30)
    msg = datetime_message(now)
    assert msg[0] == 'Tuesday, Sep 30', msg[0]
    assert msg[1] == '1:25 PM', msg[1]
