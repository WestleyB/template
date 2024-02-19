import os


def get_sqlite_uri():
    """ SQLite connection string """

    return 'sqlite:////%s' % (
        os.getenv("DB_NAME")
    )
