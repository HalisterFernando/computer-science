from abc import ABC, abstractclassmethod


class ManipuladorDeLog(ABC):
    @abstractclassmethod
    @classmethod
    def log(cls, msg):
        raise NotImplementedError
