#import statements

import pickle
import streamlit as st


with open("SpamDetectionModel.pkl", "rb") as file:
    classifier = pickle.load(file)

with open("vectorizer.pkl", "rb") as file:
    cvectorizer = pickle.load(file)


def main():

    st.title("Spam Email Detection")

    text = st.text_area("Enter the message here")

    vectorized_text = cvectorizer.transform([text])
    if st.button("Detect"):
        result = classifier.predict(vectorized_text)

        if(result==1):
            st.error("This is a Spam Email")
        else:
            st.error("This is not a Spam Email")

main()