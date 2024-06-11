# Code Interpreter - Streamlit Application

Welcome to the Code Interpreter Streamlit application! This application allows users to upload files in various formats (PDF, Excel, CSV, DOCX) and ask questions about the content of these files. The application uses the Google Gemini AI model to generate Python code that answers the user's queries based on the file content.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [File Formats Supported](#file-formats-supported)
- [Functionality](#functionality)
- [Environment Variables](#environment-variables)
- [License](#license)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Rahul-Jain-1/code-interpreter.git
    cd code-interpreter
    ```

2. Install all the requirements:
    ```sh
    pip install requirements.txt
    ```

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Upload a file (PDF, Excel, CSV, DOCX) using the file uploader.

4. Enter your question in the provided input box.

5. Click the "Ask the question" button to get the Python code and the output.

## File Formats Supported

- PDF (`.pdf`)
- Excel (`.xlsx`)
- CSV (`.csv`)
- DOCX (`.docx`)

## Functionality

- **File Reading**: The application reads the content of the uploaded file.
- **Prompt Definition**: A pre-defined prompt is used to generate Python code based on the user's question.
- **Google Gemini Model**: Utilizes Google Gemini AI to generate and execute Python code.
- **Code Display**: Displays the generated Python code.
- **Output Display**: Shows the output of the executed Python code.

### Functions

- `read_pdf(file)`: Reads the text content from a PDF file.
- `read_excel(file)`: Reads the content from an Excel file and returns it as a string.
- `read_csv(file)`: Reads the content from a CSV file and returns it as a string.
- `read_docx(file)`: Reads the text content from a DOCX file.
- `get_code(question, prompt, file_type, file_name)`: Generates Python code to answer the user's question.
- `perform_code(file_content, code, query)`: Executes the generated code and returns the output.
- `remove_first_and_last_line(code)`: Removes the first and last lines from the given code.

## Environment Variables

The application uses environment variables to store sensitive information like the Google API key. Make sure to create a `.env` file in the root directory with the following content: 
```
    GOOGLE_API_KEY=your_google_api_key

```
