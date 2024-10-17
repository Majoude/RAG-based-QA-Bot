
# RAG-based QA Bot

This repository contains the code for a Retrieval-Augmented Generation (RAG) based Question-Answering (QA) bot. The bot allows users to upload PDF documents, ask questions about their content, and receive answers, along with relevant sections from the document.

## Features
- **PDF Upload**: Upload a PDF document, and the bot will extract text from it.
- **Embeddings**: Generate embeddings from the text for efficient retrieval using Pinecone.
- **Question Answering**: Ask questions based on the document, and the bot will retrieve relevant sections and provide an answer.
- **Pinecone Integration**: Utilizes Pinecone for vector storage and fast similarity search.

## Demo
Upload a PDF, ask a question, and get real-time answers based on the document's content!

## Table of Contents
- [Setup](#setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies](#technologies)
- [License](#license)

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

The `requirements.txt` file should contain dependencies such as:
- Streamlit
- Pinecone
- OpenAI (for embeddings, if used)
- PyMuPDF (for PDF processing)

### Pinecone Setup
1. **Create a Pinecone account**: If you don't have one already, sign up at [Pinecone.io](https://www.pinecone.io/).
2. **Create an Index**: Create an index for storing the embeddings.
3. **Configure API Key**: Ensure you have your Pinecone API key and environment ready.

### Environment Variables
You can store your API keys (like Pinecone) in a `.env` file or directly in your environment. The `.env` file should include:

```bash
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENVIRONMENT=your_pinecone_environment
```

### OpenAI API (Optional)
If you use OpenAI for embedding generation, you'll also need an API key. Set it up in `.env`:
```bash
OPENAI_API_KEY=your_openai_api_key
```

### Run the Application
Launch the Streamlit app using the following command:
```bash
streamlit run app.py
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
├── app.py                  # Main Streamlit app code
├── requirements.txt        # Python dependencies
├── .env.example            # Example of environment variables
├── pdf_processing.py       # PDF extraction and text processing
├── embedding_generation.py # Generate embeddings from text
├── pinecone_operations.py  # Pinecone index connection and operations
├── query_handling.py       # Handle user queries using Pinecone search
└── README.md               # This file
```

### File Descriptions
- **`app.py`**: The main file that runs the Streamlit web application.
- **`pdf_processing.py`**: Handles PDF file uploads and extracts the text.
- **`embedding_generation.py`**: Responsible for generating sentence embeddings from the document.
- **`pinecone_operations.py`**: Manages the connection and storage of embeddings in Pinecone.
- **`query_handling.py`**: Handles user queries by retrieving relevant sections from Pinecone and generating an answer.
- **`requirements.txt`**: A list of Python libraries required to run the project.

---

## Technologies

This project uses the following technologies:
- **Streamlit**: For building the web application.
- **Pinecone**: For vector storage and similarity search.
- **PyMuPDF**: For extracting text from PDF files.
- **OpenAI**: (Optional) For generating embeddings if you use OpenAI's API.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Feel free to modify and improve the bot as needed. If you encounter any issues or have questions, feel free to open an issue in this repository.

