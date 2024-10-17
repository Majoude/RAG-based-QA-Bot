# RAG-based QA Bot

This repository contains the code for a Retrieval-Augmented Generation (RAG) based Question-Answering (QA) bot. The bot allows users to upload PDF documents, ask questions about their content, and receive answers, along with relevant sections from the document.

## Features

- **PDF Upload**: Upload a PDF document, and the bot will extract text from it.
- **Embeddings**: Generate embeddings from the text for efficient retrieval using Pinecone.
- **Question Answering**: Ask questions based on the document, and the bot will retrieve relevant sections and provide an answer.
- **Pinecone Integration**: Utilizes Pinecone for vector storage and fast similarity search.
- **Cohere Integration**: Enables the generation of answers using Cohere's AI language models.

## Table of Contents

- [Setup](#setup)
- [Usage](#usage)
- [Project Structure](#project-structure)

---

## Setup

### Prerequisites

Before you begin, ensure you have the following installed on your local machine:

- **Python 3.7+**
- **pip** for managing Python packages

### Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/Majoude/RAG-based-QA-Bot.git
cd RAG-based-QA-Bot
```

### Install Dependencies

Install the necessary dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### APIs Setup

1. **Create a Pinecone account**: If you don't have one already, sign up at [Pinecone.io](https://www.pinecone.io/).
2. **Create a Cohere account**: You also need to sign up at [Cohere](https://cohere.com/).
3. **Configure API Keys**: Ensure you have your API keys ready to use.

### Environment Variables

You can store your API keys in a `.env` file or directly in your environment. The `.env` file should include:

```bash
PINECONE_API_KEY=your_pinecone_api_key
COHERE_API_KEY=your_cohere_api_key
```

### Run the Application

Launch the Streamlit app using the following command:

```bash
streamlit run main.py
```

Once the server starts, it will open a browser window with the application running locally.

---

## Usage

### 1. **Upload a PDF**:

- The app will prompt you to upload a PDF file.
- After the file is uploaded, it will extract the text and generate embeddings in the background.
- You’ll see messages confirming each step.

### 2. **Ask a Question**:

- Once the PDF is processed, a text box will appear. Type your question about the document.
- The bot will provide an answer based on the document's content and display relevant document sections.

### 3. **View the Results**:

- The bot will show the answer to your question and highlight the sections of the document it used to derive the answer.

---

## Project Structure

```bash
RAG-based-QA-Bot/
│
├── main.py                 # Main Streamlit app code
├── requirements.txt        # Python dependencies
├── __init__.py             # Marking the directory as a Python package
├── .env                    # Example of environment variables
├── pdf_processing.py       # PDF extraction and text processing
├── embedding_generation.py # Generate embeddings from text
├── pinecone_operations.py  # Pinecone index connection and operations
├── query_handling.py       # Handle user queries using Pinecone search
└── README.md               # This file
```

### File Descriptions

- **`main.py`**: The main file that runs the Streamlit web application.
- **`pdf_processing.py`**: Handles PDF file uploads and extracts the text.
- **`embedding_generation.py`**: Responsible for generating sentence embeddings from the document.
- **`pinecone_operations.py`**: Manages the connection and storage of embeddings in Pinecone.
- **`query_handling.py`**: Handles user queries by retrieving relevant sections from Pinecone and generating an answer.
- **`requirements.txt`**: A list of Python libraries required to run the project.

---

Feel free to modify and improve the bot as needed. If you encounter any issues or have questions, feel free to open an issue in this repository.
