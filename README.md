# Local Chat App with Ollama & Streamlit

This project is a simple chat application built with [Streamlit](https://streamlit.io/) that interacts with a locally hosted language model served by [Ollama](https://ollama.com/). The model is run manually via the terminal (using `ollama serve`), and the Streamlit app communicates with it through HTTP requests.

## Overview

The application allows users to send chat messages via a web interface. When a user submits a message, the app sends an HTTP POST request to the Ollama API (running on `localhost:11434`) and displays the model's generated response. This modular setup keeps the model running independently and simplifies resource management.

## Prerequisites

- **Ollama:** Install and set up Ollama on your machine. Follow the instructions on the [Ollama website](https://ollama.com/) to download and install the desired language model(s).
- **Python:** Ensure Python 3.8 or higher is installed.
- **Streamlit:** Install Streamlit.
- **Required Python Packages:**  
  - `requests`  
  - (Optional) Any additional packages needed for your application

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/local-chat-app.git
   cd local-chat-app
   ```

2. **Create and activate a virtual environment (recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required Python packages:**

   ```bash
   pip install streamlit requests
   ```

## Configuration

The application uses a configuration file (`config.py`) to specify the model name and API endpoint. Edit the file as needed:

```python
# config.py

# Name of the Ollama model to use (e.g., "gemma2:2b")
MODEL_NAME = "gemma2:2b"

# Base URL of the Ollama API (default port is 11434)
API_URL = "http://localhost:11434/api"
```

## Running the Application

### 1. Start the Ollama API Server

Before launching the Streamlit app, open a terminal and run the following command to start the Ollama server:

```bash
ollama serve
```

This command will load your local models and listen for API requests on port 11434.

### 2. Launch the Streamlit App

In another terminal (with your virtual environment activated), run:

```bash
streamlit run app.py
```

This will open a new tab in your browser displaying the chat interface.

## Testing the API

To verify that the Ollama API is running and available, you can use the following `curl` command:

```bash
curl http://localhost:11434/api/version
```

A successful response will display the current version of the Ollama service.

## Application Code Overview

- **app.py:** Contains the Streamlit application code that:
  - Provides a text input for user messages.
  - Sends a POST request to the Ollama API’s `/generate` endpoint with the prompt.
  - Displays the response from the model.
  
- **config.py:** Holds configuration values such as the model name and API URL.

## Example HTTP Request in Code

The app uses Python’s `requests` library to interact with the Ollama API. An example function to get a response is:

```python
import json
import requests
import config

def get_model_response(prompt):
    url = f"{config.API_URL}/generate"
    payload = {
        "model": config.MODEL_NAME,
        "prompt": prompt,
        "stream": False  # Set to True for streaming responses if needed
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    response.raise_for_status()
    return response.json()
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Ollama](https://ollama.com/) for providing the local model serving capability.
- [Streamlit](https://streamlit.io/) for making it easy to build interactive web applications in 