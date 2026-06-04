from abc import ABC, abstractmethod
from datetime import datetime

class AbstractUser(ABC):
    def __init__(self, username: str):
        self._username = username

    @property
    def username(self) -> str:
        return self._username

    @abstractmethod
    def display_role(self) -> str:
        pass

class ChatUser(AbstractUser):
    def __init__(self, username: str):
        super().__init__(username)

    def display_role(self) -> str:
        return f"Chat Participant: @{self.username}"

class Message:
    def __init__(self, sender: ChatUser, content: str, timestamp: str = None):
        self._sender = sender
        self._content = content
        self._timestamp = timestamp or datetime.now().isoformat()

    @property
    def sender(self) -> ChatUser:
        return self._sender

    @property
    def content(self) -> str:
        return self._content

    @property
    def timestamp(self) -> str:
        return self._timestamp

    def to_dict(self) -> dict:
        return {
            "sender": self.sender.username,
            "content": self.content,
            "timestamp": self.timestamp
        }

    @classmethod
    def from_dict(cls, data: dict, user_lookup: dict) -> 'Message':
        sender = user_lookup.get(data['sender'], ChatUser(data['sender']))
        return cls(
            sender=sender,
            content=data['content'],
            timestamp=data['timestamp']
        )