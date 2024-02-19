from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from ..infrastructure.database.postgres import get_postgres_uri

DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(
        get_postgres_uri(),
    )
)


def create_database_engine(pool_pre_ping: bool = True):
    """ create SQLAlchemy database engine """

    return create_engine(get_postgres_uri(), pool_pre_ping=pool_pre_ping)


def is_database_ready() -> bool:
    """  """

    try:
        engine = create_database_engine(pool_pre_ping=False)
        connection = engine.connect()
        print('Database connected')
        connection.close()
        return True
    except SQLAlchemyError as e:
        return False
