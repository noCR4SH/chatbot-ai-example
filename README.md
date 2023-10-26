
# Chatbot AI Example

Source code for Chatbot built during webinar:
https://futurecollars.com/wydarzenia-fc/bezplatny-webinar-stworz-personalizowany-czat-z-wykorzystaniem-ai/

## Getting Started

These instructions will help you set up the project locally.

### Prerequisites

- Git
- Python (version, e.g., 3.7 or later)
- pip
- virtualenv (optional but recommended)

### Clone the Repository

To clone the repository, run the following command:

```bash
git clone https://github.com/noCR4SH/chatbot-ai-example
cd chatbot-ai-example
```
### Setting up a Virtual Environment
It's a good practice to create a virtual environment for your Python projects to ensure dependencies don't conflict. Here's how you can set it up:

```bash
python -m venv venv
```
### Activate the Virtual Environment
Windows:
```bash
.\venv\Scripts\activate
```

macOS and Linux:
```bash
source venv/bin/activate
```
### Install Dependencies
To install the required packages:

```bash
pip install -r requirements.txt
```

### Configure API Key
Open the constants.py file in your preferred editor and replace APIKEY value with your OpenAI API key.

### Running the example

#### Remember to put your data into "data" folder before running!
Simply run the main.py:

```bash
python main.py
```