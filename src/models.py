from abc import ABC, abstractmethod
from datetime import datetime

class AbstractUser(ABC):
    """
    ABSTRACTION: This is an abstract base class. It defines the blueprint
    for any user in the system but cannot be instantiated on its own.
    """
    def __init__(self, username: str):
        self._username = username

    @property
    def username(self) -> str:
        """Property getter to safely access the protected username."""
        return self._username

    @abstractmethod
    def display_role(self) -> str:
        """Abstract method that forces derived classes to implement their own behavior."""
        pass

class ChatUser(AbstractUser):
    """
    INHERITANCE: ChatUser inherits from the AbstractUser base class.
    """
    def __init__(self, username: str):
        super().__init__(username)

    def display_role(self) -> str:
        """
        POLYMORPHISM: Overriding the abstract method to provide specific
        functionality for a ChatUser.
        """
        return f"Chat Participant: @{self.username}"

class Message:
    """Represents a single chat message, completely encapsulated."""
    def __init__(self, sender: ChatUser, content: str, timestamp: str = None):
        self._sender = sender
        self._content = content
        # Generate an exact timestamp if one isn't provided (e.g., when creating a new message)
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
        """Serializes the object to a dictionary for JSON storage."""
        return {
            "sender": self.sender.username,
            "content": self.content,
            "timestamp": self.timestamp
        }

    @classmethod
    def from_dict(cls, data: dict, user_lookup: dict) -> 'Message':
        """Class method to deserialize a dictionary back into a Message object."""
        sender = user_lookup.get(data['sender'], ChatUser(data['sender']))
        return cls(
            sender=sender,
            content=data['content'],
            timestamp=data['timestamp']
        )