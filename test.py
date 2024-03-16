import SuffixTrie as trie
import time
import random
from Suffix_Tree import SuffixTree
from Suffx_Tree_Search import CheckSubString

seq =    "TAAAAGCCGCGAAAACT"
search = "TTCGAGCCGCGAAAACT"

t = SuffixTree(seq)
t.build_suffix_tree()
a = CheckSubString(t, seq, findall=True, k = 2 )
print(a.acceptable(seq, search))

