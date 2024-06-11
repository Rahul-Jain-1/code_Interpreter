import streamlit as st
import os
from PyPDF2 import PdfReader
import pandas as pd
from docx import Document

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv() ## load all the environemnt variables

def read_pdf(file):
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to read Excel content
def read_excel(file):
    df = pd.read_excel(file)
    return df.to_string()

# Function to read CSV content
def read_csv(file):
    df = pd.read_csv(file)
    return df.to_string()

# Function to read DOCX content
def read_docx(file):
    doc = Document(file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

## Configure Genai Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To load Google Gemini Model and provide queries as response

def get_code(question,prompt,file_type,file_name):
    model=genai.GenerativeModel('gemini-pro')
    prompt[0] += f"replace the file name with {file_name}.{file_type} \n\n Here is the question : \n\n"
    print(prompt[0])
    response=model.generate_content([prompt[0],question])
    return response.text

## Fucntion To retrieve query from the database

def perform_code(file_content,code, query):
    model=genai.GenerativeModel('gemini-pro')
    prompt1 = f"the file content is {file_content}\n\n .I have given you to the pdf/csv/excel content use this content to answet this question {query}. perform this code \n\n{code} to capture the output . Give the output only not code."
    response=model.generate_content([prompt1,query])
    return response.text
    

## Define Your Prompt
prompt = [
    """
    You are a highly skilled expert in translating English questions into efficient and accurate Python code. Your goal is to provide the most optimal Python code solution for the given question. Please ensure the following:

    1. The code is correct and functional.
    2. The solution is as concise as possible, with a minimal number of lines.
    3. The code is well-commented to explain its logic and functionality.
    4. The solution adheres to best practices in Python programming, including proper naming conventions and code readability.
    5. If there are multiple ways to solve the problem, choose the one that is most efficient in terms of performance.

    
    """
]
# Remove the first and last lines from the given code.

def remove_first_and_last_line(code):
    code_lines = code.strip().split('\n')
    if len(code_lines) > 1:
        # Remove the first and last lines.
        modified_lines = code_lines[1:-1]
    else:
        modified_lines = []

    return '\n'.join(modified_lines)


## Streamlit App
st.set_page_config(page_title="Code Interpreter")
uploaded_file = st.file_uploader("Upload a file", type=["pdf", "xlsx", "csv", "docx"])

if uploaded_file is not None:
    # Read file content based on file type
    if uploaded_file.type == "application/pdf":
        file_content = read_pdf(uploaded_file)
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        file_content = read_excel(uploaded_file)
    elif uploaded_file.type == "text/csv":
        file_content = read_csv(uploaded_file)
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        file_content = read_docx(uploaded_file)
    else:
        st.error("Unsupported file type")
        file_content = ""


    # User input for prompt

    st.header("Code Interpreter ")

    question=st.text_input("Input: ",key="input")

    submit=st.button("Ask the question")

    # if submit is clicked
    if submit:
        code=get_code(question,prompt,uploaded_file.type,uploaded_file.name)
        print(code)
        
        response = remove_first_and_last_line(code)
        ans = perform_code(file_content,response, question)
        st.subheader("Code --->>>>")
        st.code(response, language='python')
        st.subheader("Output --->>>>")
        st.markdown(ans)








