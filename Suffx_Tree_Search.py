class Base:
    def __init__(self, tree):
        self.tree = tree
        self.main_string = tree._string
        self.root = tree.root


class CheckSubString(Base):
   def __init__(self, tree, sub_string, findall=False, k = 0):
      super(CheckSubString, self).__init__(tree)
      self.sub_string = sub_string
      self.latest_index = 0
      self.findall = findall
      self.continue_flag = False
      self.sub_length = len(sub_string)
      self.k = k

   def acceptable(self, string1, string2):
      mismatches = abs(len(string1) - len(string2))

      for x, y in zip(string1, string2):
         if x != y:
            mismatches += 1

      return mismatches


   def traverse(self, node, sub_string):
      indices = []
      mismatches = 0

      def traverse_recursive(current_node, remaining_substring):
         nonlocal indices
         nonlocal mismatches

         if remaining_substring:
            item = next(((char, child) for char, child in current_node.children.items() if remaining_substring.startswith(char)), None)

            if item:
                  char, child = item
                  start, end = child.start, child.end

                  # Compare the substring with the edge's substring
                  common_prefix = 0
                  while start + common_prefix <= end and common_prefix < len(remaining_substring) and self.main_string[start + common_prefix] == remaining_substring[common_prefix]:
                     if self.main_string[start + common_prefix] == remaining_substring[common_prefix]:
                        common_prefix += 1
                     else:
                        common_prefix += 1
                        mismatches += self.acceptable(self.main_string[start + common_prefix], remaining_substring[common_prefix])


                  index = start - (self.sub_length - len(remaining_substring))
                  if common_prefix == len(remaining_substring) and index not in indices:
                     # Entire substring matches, add the index to the list
                     indices.append(index)

                     if not self.findall:
                        # If findall is False, return immediately after finding the first occurrence
                        return

                  if common_prefix > 0:
                     # Partial match, call traverse for the remaining substring
                     traverse_recursive(child, remaining_substring[common_prefix:])
            # else:
            #       # No edge found that starts with the leading character of the substring
            #       return

      traverse_recursive(node, sub_string)
      return indices if indices else [-1]  # Return [-1] if no occurrences found when findall is False



   def check(self):
      if self.root is None:
         return -1
      if not isinstance(self.sub_string, str):
         return -1
      if not self.sub_string:
         # Every string starts with an empty string
         return 0

      return self.traverse(self.root, self.sub_string)

   def find_all_match(self, node, sub_length):

      def inner(node, traversed_edges):
         for char, child in node.children.items():
               if child.leaf:
                  yield child.start - traversed_edges
               else:
                  start, end = child.start, child.end
                  sub_length = end - start + 1
                  yield from inner(child, traversed_edges + sub_length)

      if node.leaf:
         first = node.start - (self.sub_length - sub_length)
         return [first, *inner(node, self.sub_length)]
      else:
         return list(inner(node, self.sub_length))