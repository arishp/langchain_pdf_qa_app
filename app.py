import streamlit as st
from dotenv import load_dotenv
from utils import user_input, get_pdf_text, get_text_chunks, get_vector_store

load_dotenv()

st.set_page_config(page_title="Document Genie", layout="wide")

def main():
    st.header("AI clone chatbot💁")
    user_question = st.text_input("Ask a Question from the PDF Files", key="user_question")
    if user_question:  # Ensure API key and user question are provided
        st.write(user_input(user_question))

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True, key="pdf_uploader")
        if st.button("Submit & Process", key="process_button"):  # Check if API key is provided before processing
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Done")

if __name__ == "__main__":
    main()