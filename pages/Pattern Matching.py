import streamlit as st
from suffixtree2 import SuffixTree as tree
from suffixtree2modules import CheckSubString
import time 
from statistics import mean

st.header("Welcome to the pattern matching tool!")
st.subheader("Implementation")
st.write("This pattern matching tool utilizes a suffix tree to match patterns quickly. You can learn more about suffix trees in the \"Learn\" tab on the left!")

st.subheader("Ukkonen's Algorithm")
st.write("This implementation uses Ukkonen's suffix tree construction algorithm, which constructs a suffix tree in linear time. You can learn more about this algorithm as well in the \"Learn\" tab!")
st.divider()


st.write("Input your sequence below (enter or click elsewhere to submit):")
sequence = st.text_input("DNA/RNA/Protein Sequence")
start = time.time()

t = tree(sequence)
t.build_suffix_tree()

end = time.time()
st.write(f"sequence length: {len(sequence)}")
st.write(f"took {end - start} seconds to construct tree.")

st.write("\n")
st.write("Input your pattern below (enter or click elsewhere to submit):")
pattern = st.text_input("DNA/RNA/Protein Pattern to Search for")

on = st.toggle("Find only one pattern")

t.print_dfs()

# if on:
#    a = CheckSubString(t, pattern, findall=False)
# else:
#    a = CheckSubString(t, pattern, findall=True)

# print(a.check())

st.divider()

st.subheader("Results")


