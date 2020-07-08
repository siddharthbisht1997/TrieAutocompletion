# Word Autocompletion using Tries

TrieRecommender is python class capable of giving autocomplete suggestions for the entered query.

## Installation
You can download the Module from here or even copy the code.

## Usage

Import the Trie Recommender

```python
from Trie.TrieRecommender import TrieRecommender
```

Create the Object of the Trie Recommender
```python
Recommender = TrieRecommender()
```

Get the Vocabulary, the Recommender only accepts Lists to build the Trie
```python
vocab_file = "vocabulary.txt"     #Add the file path here
with open(vocab_file,"r") as file:
  vocabulary = file.read().split("\n")
```

Call the Build function of the TrieRecommender Class
```python:
Recommender.build(vocabulary)
```
You can see the entire vocabulary as well using the get_vocabulary method, you are required to send in the root node of the Recommender
```python:
root = Recommender.root
Recommender.get_vocabulary(root)
```

You can search for a word as well
```python:
word = input("Enter word to search -> ")
Recommender.search(word)
```

Use the Autocomplete method to get suggestions, the Autocomplete method returns a list
```python:
query = input("Enter the query word -> ")
suggestions = Recommender.autocomplete(query)
print("Possible Sugesstions are {}".format(suggestions))
```


## License
[MIT](https://choosealicense.com/licenses/mit/)
