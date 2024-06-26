# Code Interpreter - Streamlit Application

Welcome to the Code Interpreter Streamlit application! This application allows users to upload files in various formats (PDF, Excel, CSV, DOCX) and ask questions about the content of these files. The application uses the Google Gemini AI model to generate Python code that answers the user's queries based on the file content.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [File Formats Supported](#file-formats-supported)
- [Functionality](#functionality)
- [Environment Variables](#environment-variables)
- [Test Cases](#test-cases)

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

This application uses the Google Gemini AI model instead of OpenAI's GPT-3.5 API. The reason for this is that I have exhausted the free API access for GPT-3.5 and do not currently have access to it. Hence, the Google Gemini API is used as an alternative to provide similar functionality.


## Test Cases

### Test Case 1: PDF File
- **File**: `sample.pdf`
- **Content**: A PDF file containing a few paragraphs of text.
- **User Prompt**: "What is the main topic of the first paragraph?"
- **Expected Output**: A summary or the main topic of the first paragraph in the PDF.

### Test Case 2: Excel File
- **File**: `sample.xlsx`
- **Content**: An Excel file with multiple sheets. One sheet contains a table of sales data.
- **User Prompt**: "What is the total sales for the month of January?"
- **Expected Output**: The total sales amount for January.

### Test Case 3: CSV File
- **File**: `sample.csv`
- **Content**: A CSV file with a list of employees, including their names, departments, and salaries.
- **User Prompt**: "Which department has the highest average salary?"
- **Expected Output**: The name of the department with the highest average salary.

### Test Case 4: DOCX File
- **File**: `sample.docx`
- **Content**: A DOCX file containing a company policy document.
- **User Prompt**: "What are the key points in the employee conduct policy?"
- **Expected Output**: A list or summary of the key points in the employee conduct policy section.

## Notes

- This application uses the Google Gemini AI model instead of OpenAI's GPT-3.5 API. The reason for this is that I have exhausted the free API access for GPT-3.5 and do not currently have access to it. Hence, the Google Gemini API is used as an alternative to provide similar functionality.
