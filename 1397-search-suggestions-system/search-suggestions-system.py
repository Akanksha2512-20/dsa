class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            # Maintain a sorted list of up to three suggestions
            if len(node.suggestions) < 3:
                node.suggestions.append(word)

    def getSuggestions(self, prefix):
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        return node.suggestions
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Solution()
        # Step 1: First sort lexicographically to maintain sorted suggestions in Trie
        products.sort()
        # Step 2: Insert each product into the Trie
        for product in products:
            trie.insert(product)
        # Step 3: Build the result list by finding suggestions for each prefix of the search word
        result, prefix = [], ""
        for char in searchWord:
            prefix += char
            result.append(trie.getSuggestions(prefix))
        return result