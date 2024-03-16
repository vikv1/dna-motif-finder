import streamlit as st

st.header("Here are some sample sequences for the pattern matching tool")

st.write("Length 26498 DNA sequence")
with open("pages/Pattern Matching Test 1.txt", "rb") as file:
   btn = st.download_button(
            label="Download",
            data=file,
            file_name="Pattern Matching Test 1.txt",
         )


st.write("Length 10.43M DNA sequence")
with open("pages/Pattern Matching Test 2.txt", "rb") as file:
   btn = st.download_button(
            label="Download",
            data=file,
            file_name="Pattern Matching Test 2.txt",
         )

