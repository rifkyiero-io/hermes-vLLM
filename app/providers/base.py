from abc import ABC, abstractmethod


class BaseProvider(ABC):

    @abstractmethod
    async def chat(self, messages, temperature=0.7):
        pass
