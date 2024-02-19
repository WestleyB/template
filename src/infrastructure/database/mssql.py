import os


def get_mssql_uri():
    """ Microsoft SQL connection string """

    return '%s://%s:%s@%s:%s/%s' % (
        os.getenv("DB_DRIVER"),
        os.getenv("DB_USERNAME"),
        os.getenv("DB_PASSWORD"),
        os.getenv("DB_HOST"),
        os.getenv("DB_PORT"),
        os.getenv("DB_NAME")
    )
