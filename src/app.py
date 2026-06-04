import os
from datetime import datetime
from .models import ChatUser, Message
from .storage import JsonStorage


def clear_screen():
    """Clears the terminal screen for a cleaner UI."""
    os.system('cls' if os.name == 'nt' else 'clear')


def format_timestamp(iso_str: str) -> str:
    """Converts ISO timestamp to a readable format."""
    dt = datetime.fromisoformat(iso_str)
    return dt.strftime("%H:%M:%S")


def print_ui(messages: list, current_user: ChatUser, user1: ChatUser, user2: ChatUser):
    """Handles creative console formatting to simulate a GUI chat."""
    clear_screen()

    print("+" + "=" * 60 + "+")
    print("|" + f" SECURE OFFLINE PV: {user1.username} & {user2.username} ".center(60) + "|")
    print("+" + "=" * 60 + "+")
    print(f" Commands: '/switch' (Change User) | '/quit' (Exit)".center(62))
    print("-" * 62 + "\n")

    if not messages:
        print(" (No messages yet. Start the conversation!)".center(62))

    for msg in messages:
        time_str = format_timestamp(msg.timestamp)

        if msg.sender.username == current_user.username:
            text = f"[{time_str}] YOU: {msg.content} "
            print(text.rjust(62))
        else:
            print(f" [{time_str}] {msg.sender.username}: {msg.content}")

    print("\n" + "-" * 62)
    print(f" Logged in as: {current_user.display_role()}")


def main():
    filepath = os.path.join(os.path.dirname(__file__), '..', 'chat_history.json')
    storage = JsonStorage(filepath)

    user1 = ChatUser("Armita")
    user2 = ChatUser("Arya")
    users = {user1.username: user1, user2.username: user2}

    messages = storage.load(users)
    current_user = user1

    while True:
        print_ui(messages, current_user, user1, user2)

        text = input("\n > Type a message: ").strip()

        if not text:
            continue
        if text.lower() == '/quit':
            print("\nExiting chat... Goodbye!")
            break
        if text.lower() == '/switch':
            current_user = user2 if current_user == user1 else user1
            continue

        new_msg = Message(sender=current_user, content=text)
        messages.append(new_msg)
        storage.save(messages)


if __name__ == "__main__":
    main()