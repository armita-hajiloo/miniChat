import unittest
import os
from src.models import ChatUser, Message
from src.storage import JsonStorage


class TestMiniChat(unittest.TestCase):
    def setUp(self):
        """Sets up fresh instances before every single test."""
        self.user1 = ChatUser("Alice")
        self.user2 = ChatUser("Bob")
        self.test_file = "test_history.json"
        self.storage = JsonStorage(self.test_file)

    def tearDown(self):
        """Cleans up the test environment after every single test."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_encapsulation(self):
        """Validates that properties protect inner state variables."""
        self.assertEqual(self.user1.username, "Alice")

        with self.assertRaises(AttributeError):
            self.user1.username = "Eve"

    def test_polymorphism(self):
        """Validates that the overridden abstract method works correctly."""
        self.assertEqual(self.user1.display_role(), "Chat Participant: @Alice")

    def test_message_creation(self):
        """Tests that messages correctly capture identity, content, and timestamp."""
        msg = Message(self.user1, "Hello unit tests!")
        self.assertEqual(msg.sender, self.user1)
        self.assertEqual(msg.content, "Hello unit tests!")
        self.assertIsNotNone(msg.timestamp)

    def test_json_storage_cycle(self):
        """Tests saving to and loading from a JSON file."""
        msg1 = Message(self.user1, "Persistent message.")
        self.storage.save([msg1])

        self.assertTrue(os.path.exists(self.test_file))

        users_lookup = {"Alice": self.user1, "Bob": self.user2}
        loaded_messages = self.storage.load(users_lookup)

        self.assertEqual(len(loaded_messages), 1)
        self.assertEqual(loaded_messages[0].content, "Persistent message.")
        self.assertEqual(loaded_messages[0].sender.username, "Alice")


if __name__ == "__main__":
    unittest.main()