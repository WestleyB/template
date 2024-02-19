from abc import ABC, abstractmethod


class IConsumer(ABC):
    @abstractmethod
    def start_listener(self, callback):
        raise NotImplementedError
