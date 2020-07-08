class TrieNode():

  def __init__(self):
    """
    This is the fundamental component of a Trie.
    It has two attributes: children and is_leaf.
    children is a dictionary/hashmap that keeps track of the next possible letters
    and is_leaf is a boolean variable storing whether the letter is a leaf node/ending letter or not.
    The values of children should store the subsequent/reference TrieNodes' Object
    """
    self.children : dict = {}
    self.is_leaf : bool = False

class TrieRecommender():
  
  def __init__(self):
    """
    This is the Trie Class, it has one variable, the Root. The Root acts
    as a pointer and also the starting of the Trie, and points to the 
    various letters
    """
    self.root = TrieNode()
    self.suggestions : list  = []
  
  def build(self, vocabulary : list) -> None:
    """
    This function takes in a Vocabulary and using the vocabulary builds
    the entire Trie
    
    Parameters:
    vocabulary : list
    List of words to be inserted into the Trie   

    """
    # Create an inline function to convert word case to lower
    lower = lambda x : x.lower()
    # Map all the items in the list, and lower the case                  
    vocabulary = list(map(lower,vocabulary))     
    for word in vocabulary:
      self.__insert__(word)
  
  def __insert__(self, word : str) -> None:
    """
    The insert method is a private method which is iteratively called by the build
    method to create the Trie

    Parameters:
    word : string
    Word to be inserted into the Trie    

    """
    # Use the root as the starting point and
    # keep appending letters as they come
    ptr = self.root                               
    for letter in word:                           
      if letter not in ptr.children:
        ptr.children[letter] = TrieNode()
      ptr = ptr.children[letter]
    
    # Once the word is inserted letter by letter,
    # add the complete word to the last letter to make it easier to identify the end point
    ptr.children[word] = TrieNode()
    ptr = ptr.children[word]
    ptr.is_leaf = True                             
    

  def search(self, word : str) -> str:
    """
    This method takes in a word from user and searches the Trie to 
    check whether it is present in the Trie or not.
    
    Parameters:
    word : string
    Word to be searched in the Trie

    returns Found/Not Found accordingly

    """
    # Use the root as the starting point
    ptr = self.root
    # Remember the Trie has been built using small letters
    word = word.lower()
    # Search for the word letter by letter
    for letter in word:
      if letter not in ptr.children:
        return word + " not found"
      ptr = ptr.children[letter]  
    if word in ptr.children:
      return word + " found"
    return word + " not found"
 
  def __get_suggestions__(self, root : TrieNode ) -> None:
    """
    Given a TrieNode, recursively traverse the trie to
    get recommendations for the given input

    Parameters:
    root : TrieNode
    The Starting Node to get the recommendations

    """
    for child in root.children.keys():
      # Append if the Child is a Leaf node
      if root.children[child].is_leaf == True:
        self.suggestions.append(child)
      else:
        self.__get_suggestions__(root.children[child])


  def autocomplete(self, word : str) -> list:
    """
    Take a word or incomplete string from the user and suggest the possible
    autocompletions.

    Parameters:
    word : String
    The word for which we need the Autocompletions

    returns the list of suggestions
    """
    self.suggestions = []
    word = word.lower()
    key = ''
    ptr = self.root
    # To get the Autocompletetion, match till the string is there in the Trie
    for letter in word:
      if letter not in ptr.children:
        break
      key += letter
      ptr = ptr.children[letter]
    self.__get_suggestions__(ptr)
    suggestions = self.suggestions
    self.suggestions = []
    return suggestions

  def get_vocabulary(self, root : TrieNode) -> None:
    """
    Recursively traverse the Trie and print all the words
    stored in the Trie

    Parameters:
    root : TrieNode
    The ptr that will be used as the starting node to traverse the Trie

    """
    for child in root.children.keys():
      if root.children[child].is_leaf == True:
        print(child)
      else:
        self.get_vocabulary(root.children[child])