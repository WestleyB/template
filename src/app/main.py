import os
import time

from ..persistence.database import is_database_ready


def main():
    """ main program """

    while not is_database_ready():
        _start_wait_time: int = int(os.getenv('DB_START_WAIT_TIME'))
        print('Database is not ready. Retrying in %s second(s)' % _start_wait_time)
        time.sleep(_start_wait_time)

    # start program


if __name__ == '__main__':
    main()
