import streamlit as st


st.header("Welcome to the learn tab!")
st.subheader("Click one of the buttons below to learn more!")

with st.expander("Suffix Tries"):
   st.write("Suffix Tries are a data structure that makes pattern searching O(m) where m is the length of the pattern.")
   st.image("https://media.geeksforgeeks.org/wp-content/uploads/trieSuffix.jpg")   
   #st.image("https://www.researchgate.net/publication/51517433/figure/fig1/AS:324814599409675@1454453243506/A-suffix-tree-that-represents-the-sequence-BANANA-The-beginning-of-the-sequence-is.png")
   st.write("Pictured above is a suffix trie for the word \"Banana\". The \\0 at the end of the string is a special character used to denote the end of the string. I will just be referring to it as \$ instead from now on.")
   st.write("Say you are searching for \"Anana\$\". You can find it easily in a suffix trie. Start from the root (root never has a value), and see if a node has the current letter you are searching for. In this case, the letter we are looking for first is \"A\". There is a branch with that character so we go down it. The next character we need to find is \"N\". A node with \"N\" exists so go down that path. Repeat for each character in the sequence you are searching for until you reach a \$ sign. If a \$ is reached, that means the string is present.")
   st.write("You may have noticed though that this tree might look unnecessarily big. Look at the far left branch for example, we know that no matter what it is going to end in \"ANANA\$\". Wouldn't it be more efficient space-wise to just merge that entire branch into one node? This is exactly what a suffix tree does to save memory while maintaining the same search speed. You can learn more about that below!")
   st.link_button("Wikipedia Link", "https://en.wikipedia.org/wiki/Suffix_tree")

with st.expander("Suffix Trees"):
   st.write("A suffix tree is an improved upon version of the suffix trie. It enables efficient O(m) searching where m is the length of the pattern. This tool utilizes a suffix tree and an algorithm known as Ukkonen's algorithm in order to construct it in linear time!")
   st.image("https://he-s3.s3.amazonaws.com/media/uploads/a55f8db.png")
   st.write("In the above tree, a suffix tree is constructed for \"Banana\". The \"$\" is a special character which signal the end of the string.")
   st.write("For the word Banana, the suffixes are as follows:")
   st.image("pages/banana suffixes.png")
   st.write("For every suffix listed above, there must be a way to construct it by following the suffix tree.")
   st.write("For example, if you want to see if \"ana\$\" is present in the string, start from the root (which is always valueless), and follow the path of the longest prefix you can find. In terms of the string we are searching for, \"a\" is the largest prefix which actually has a path. So we go down a. From there, we only have to search for \"na$\", and as you can see it is right under \"a\".")
   st.link_button("Wikipedia Link", "https://en.wikipedia.org/wiki/Suffix_tree#:~:text=In%20computer%20science%2C%20a%20suffix,of%20many%20important%20string%20operations.")

with st.expander("Ukkonen's Algorithm"):
   st.write("Suffix Trees are nice because they allow efficient pattern searching, but what about how long it will take to construct one? Luckily, there is an algorithm that allows us to construct a suffix tree in linear time, although it is complicated.")
   st.write("Ukkonen's algorithm would be quite difficult to explain in plain text, so here is a good animation of the procedure!")
   st.link_button("Visualization tool", "https://brenden.github.io/ukkonen-animation/")
