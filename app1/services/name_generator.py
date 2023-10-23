from abc import ABC, abstractmethod
import random
import string

from rhazes.decorator import bean


class StringGeneratorService(ABC):

    @abstractmethod
    def generate(self, length):
        pass


@bean(_for=StringGeneratorService)
class SimpleNameGeneratorService(StringGeneratorService):

    def generate(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))
