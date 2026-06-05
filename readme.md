# Mini-Chat Application: Python OOP Project

## Overview

This repository contains a purely Python-based offline terminal chat application. It was developed as a university project to rigorously demonstrate core Object-Oriented Programming principles while adhering to standard software engineering practices.

## Features

* **Offline Private Chat:** Simulates a two-way conversation between participants (Armita and Arya).
* **Persistent Storage:** Saves and loads chat histories automatically using a local JSON file.
* **Standard Library Only:** Built entirely with built-in Python modules (json, datetime, os, abc). No external dependencies or pip installations are required.
* **Creative Terminal UI:** Formatted console output that mimics a standard chat interface.

## Academic Concepts Demonstrated

This project is structurally designed to showcase the four pillars of OOP:

* **Encapsulation:** User identities and message metadata are protected using private attributes and accessed safely via property decorators.
* **Abstraction:** Base classes (`AbstractUser`, `AbstractStorage`) define contracts for derived classes, clearly separating interfaces from implementation.
* **Inheritance:** Specific components like `ChatUser` and `JsonStorage` inherit from and extend the functionality of their respective base classes.
* **Polymorphism:** Methods such as `display_role()`, `save()`, and `load()` are overridden to provide specific behaviors across different objects.

## Project Structure

```text
/
├── .git/
├── requirements.txt
├── readme.md
├── src/
│   ├── __init__.py
│   ├── models.py
│   ├── storage.py
│   └── app.py
└── tests/
    ├── __init__.py
    └── test_chat.py

```

## Setup and Execution

Since this project relies exclusively on the standard library, the `requirements.txt` is strictly empty. No environment setup is required.

To run the chat application, open your terminal at the root directory of the project and execute:

```bash
python -m src.app

or for linux/mac:

python3 -m src.app
```

Once the application starts, you can type your messages, use `/switch` to change between the two active users, and type `/quit` to safely exit the application. Your chat history is automatically saved to `chat_history.json`.

## Running Unit Tests

The project includes a comprehensive test suite using Python's built-in `unittest` module to validate encapsulation, polymorphism, data serialization, and file I/O operations.

To run the tests with detailed output messages, execute the following command from the root directory:

```bash
python -m unittest discover -s tests -v

or for linux/mac:

python3 -m unittest discover -s tests -v
```
