# Aizen AI Chatbot

Aizen is a simple rule-based AI chatbot built in Python. It uses predefined keywords and responses to simulate conversations with users. This project demonstrates the basic concepts of rule-based artificial intelligence and chatbot development.

## Features

- Rule-based conversation system
- Keyword matching for responses
- Randomized replies for better interaction
- Lightweight and easy to understand
- Beginner-friendly implementation
- No external dependencies required

## Requirements

- Python 3.6 or higher

## Installation

1. Download or clone the project.

```bash
git clone <repository-url>
```

2. Navigate to the project directory.

```bash
cd aizen-chatbot
```

3. Run the chatbot.

```bash
python aizen.py
```

## Usage

Start the program and interact with Aizen through the terminal.

### Example

```text
=== Aizen AI Chatbot ===
Type 'bye' to exit.

You: hello
Aizen: Greetings! Aizen at your service.

You: how are you
Aizen: All systems operational.

You: what is your name
Aizen: I am Aizen, your rule-based AI assistant.

You: bye
Aizen: Goodbye!
```

## Project Structure

```text
aizen-chatbot/
│
├── aizen.py
└── README.md
```

## How It Works

The chatbot stores predefined keywords and responses in a dictionary.

```python
responses = {
    "hello": [
        "Hello! I am Aizen.",
        "Greetings! Aizen at your service."
    ]
}
```

### Workflow

1. Accept user input.
2. Convert the input to lowercase.
3. Search for matching keywords.
4. Return a random response if a match is found.
5. Return a default response if no match exists.

## Customization

New responses can be added by updating the `responses` dictionary.

Example:

```python
responses["python"] = [
    "Python is a powerful programming language.",
    "I enjoy discussing Python programming."
]
```
