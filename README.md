# Mini Search Engine

A mini search engine application written in **Python** that can generate research for user questions, built with a command-line user interface as well as a streamlit UI. 


## Features

- **Simple yet powerful** CLI for indexing and searching content
- Easily extensible for future enhancements

## Prerequisites

- Python **3.8** or higher
- **Git**, for cloning the repository

## Quick Start

Follow the steps below to get the app running on your local machine:

```bash
# 1. Clone the repo
git clone https://github.com/Senash0813/Mini-Search-Engine.git
cd Mini-Search-Engine

# 2. (Optional but recommended) Create a virtual environment
python3 -m venv venv

# On macOS / Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

# 3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 4. Run the application
python main.py (for CLI UI)
streamlit run main.py (for streamlit UI)
```

## Note:
create a .env file in the **project directory** and set the following variables before running the application.
- OPENAI_API_KEY= "your_groq_api_key"
- OPENAI_API_BASE=https://api.groq.com/openai/v1

