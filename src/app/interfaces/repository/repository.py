from abc import ABC, abstractmethod
from uuid import UUID


class IRepository(ABC):
    @abstractmethod
    def create(self, entry):
        raise NotImplementedError

    @abstractmethod
    def get(self, entry_id: UUID):
        raise NotImplementedError

    @abstractmethod
    def update(self, entry):
        raise NotImplementedError

    @abstractmethod
    def delete(self, entry_id: UUID):
        raise NotImplementedError
