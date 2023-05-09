import streamlit as st
import spacy
from spacy import displacy

# Load the model
nlp = spacy.load(r"./model/2023-02-24_model/2023-02-24_test_model/model-best/")

# Define the Streamlit app
def main():
    st.title("Named Entity Recognition Demo")
    st.write("Enter some text below to extract named entities:")
    text = st.text_area("Input text:", height=200)
    if st.button("Extract Entities"):
        doc = nlp(text)
        if doc.ents:
            html = displacy.render(doc, style="ent")
            st.write(html, unsafe_allow_html=True)
        else:
            st.write("No entities found in the input text.")

if __name__ == "__main__":
    main()
