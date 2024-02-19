from abc import ABC, abstractmethod
from io import BytesIO


class IFileStorage(ABC):
    @abstractmethod
    def upload(self, content: bytes | BytesIO) -> dict:
        raise NotImplementedError

    @abstractmethod
    def download(self, blob_path: str) -> bytes:
        raise NotImplementedError

    @abstractmethod
    def get_properties(self, blob_path: str):
        raise NotImplementedError
