from io import StringIO
import streamlit as st
from Suffix_Tree import SuffixTree as tree
from Suffx_Tree_Search import CheckSubString
import MotifSearch as ms
import time 

def displaySection(sequence, index, patternLength):
   pattern = ":green[***" + sequence[index:index + patternLength] + "***]"
   if len(sequence) <= 52:
      result = sequence[0:index] + pattern + sequence[index + patternLength:]
   else:
      lBound = max(0, index - 25)
      rBound = min(len(sequence), index + patternLength + 27)
      result = "..." if lBound != 0 else ""
      result += sequence[lBound:index] + pattern + sequence[index + patternLength:rBound]
      result += "..." if rBound != len(sequence) else ""
   return result




st.header("Welcome to the pattern matching tool!")
st.subheader("Implementation")
st.write("This pattern matching tool utilizes a suffix tree to match patterns quickly. You can learn more about suffix trees in the \"Learn\" tab on the left!")

st.subheader("Ukkonen's Algorithm")
st.write("This implementation uses Ukkonen's suffix tree construction algorithm, which constructs a suffix tree in linear time. You can learn more about this algorithm as well in the \"Learn\" tab!")
st.divider()


st.write("Input your sequence below (enter or click elsewhere to submit):")
sequence = st.text_input("DNA/RNA/Protein Sequence")

st.write("or")

uploaded_sequence = st.file_uploader("Choose a .txt file", key='sequence uploader', accept_multiple_files=False)
if uploaded_sequence is None:
   st.write("")
elif uploaded_sequence is not None:
   stringio = StringIO(uploaded_sequence.getvalue().decode("utf-8"))
   sequence = stringio.read()

if sequence and sequence[-1] != "$":
   sequence = sequence + "$"


st.write("\n")
st.write("Input your pattern below (enter or click elsewhere to submit):")
pattern = st.text_input("DNA/RNA/Protein Pattern to Search for")

st.write("or")

uploaded_pattern = st.file_uploader("Choose a .txt file", key='pattern uploader', accept_multiple_files=False)
if uploaded_pattern is None:
   st.write("")
elif uploaded_pattern is not None:
   stringio = StringIO(uploaded_pattern.getvalue().decode("utf-8"))
   sequence = stringio.read()

k = int(st.number_input("Maximal Mismatches", min_value=0, value=0, step=1, disabled=True))
on = st.checkbox("Find only one pattern", disabled=True)
export = st.checkbox('Export results to .txt (will still display below)')

motif = st.checkbox("Search for a motif (ignores input pattern)", key="motif")
length = int(st.number_input("Motif Length", min_value=0, value=0, step=1, disabled= not motif, key="motifLen"))


search = st.button("Go")


st.divider()

st.subheader("Results")

if search and motif and length > len(sequence) - 1:
   st.error("Motif length longer than sequence")
elif search and sequence and (pattern or length > 0):
   txt = ""
   with st.spinner('Constructing tree...'):
      start = time.time()

      t = tree(sequence)
      t.build_suffix_tree()

      end = time.time()
   st.success('Constructed tree!')

   st.write(f"sequence length: {len(sequence) - 1}")
   txt += f"sequence length: {len(sequence) - 1}\n"

   st.write(f"took {end - start} seconds to construct tree.")
   txt += f"took {end - start} seconds to construct tree.\n"
   indices = None
   with st.spinner('Searching...'):
      start = time.time()
      if motif:
         length = min(len(sequence), length)
         pattern = ms.maximumOccurringString(sequence, length)
      else :
         a = CheckSubString(t, pattern, findall=on, k=k)
         indices = a.check()
      end = time.time()

   st.write(f"pattern length: {len(pattern)}")
   txt += f"pattern length: {len(pattern)}\n"

   st.write(f"took {end - start} seconds to search tree.")
   txt += f"took {end - start} seconds to search tree.\n"

   if motif and pattern:
      st.write(f"\'{pattern}\' occured most commonly in the string.")
   elif indices and indices[0] != -1:
      st.write(f"Found \'{pattern}\' at index {indices}.")
      txt += f"Found \'{pattern}\' at index {indices}."

      st.markdown(displaySection(sequence[0:len(sequence) - 1], indices[0], len(pattern)))
      if export:
         st.download_button('download output results', txt)
   else:
      st.write("Pattern not present in sequence.")

elif search and (not sequence or (not pattern and length == 0)):
   st.error("Error: No sequence and/or pattern input")