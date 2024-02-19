from ...app.interfaces.repository.repository import IRepository
from ...app.interfaces.unit_of_work.uow import IUnitOfWork
from ...persistence.database import DEFAULT_SESSION_FACTORY


class UnitOfWork(IUnitOfWork):
    """ Unit of Work pattern """

    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        # self.repository: IRepository = repository.SqlAlchemyRepository(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
