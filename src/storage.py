import json
import os
from abc import ABC, abstractmethod
from typing import List, Dict
from .models import Message, ChatUser


class AbstractStorage(ABC):
    """ABSTRACTION: Defines the contract for any storage mechanism."""

    @abstractmethod
    def save(self, messages: List[Message]) -> None:
        pass

    @abstractmethod
    def load(self, user_lookup: Dict[str, ChatUser]) -> List[Message]:
        pass


class JsonStorage(AbstractStorage):
    """INHERITANCE: A specific implementation of storage using JSON."""

    def __init__(self, filepath: str):
        self._filepath = filepath

    def save(self, messages: List[Message]) -> None:
        """POLYMORPHISM: Concrete implementation of the save method."""
        with open(self._filepath, 'w', encoding='utf-8') as f:
            json.dump([msg.to_dict() for msg in messages], f, indent=4)

    def load(self, user_lookup: Dict[str, ChatUser]) -> List[Message]:
        """POLYMORPHISM: Concrete implementation of the load method."""
        if not os.path.exists(self._filepath):
            return []

        try:
            with open(self._filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [Message.from_dict(msg, user_lookup) for msg in data]
        except json.JSONDecodeError:
            return []