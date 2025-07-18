class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
  
class Solution:
    def insert(self,words):
        root = TrieNode()
        for word in words:
            current = root
            for char in word:
                if char not in current.children:
                    current.children[char]= TrieNode()
                current = current.children[char]
            current.is_word = True    
        return root
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def backtrack(r, c, node, path):
            if node.is_word:
                found_words.add(path)
                
            # Mark this cell as visited
            temp, board[r][c] = board[r][c], '#'
            
            # Explore neighbors
            for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < len(board) and 0 <= nc < len(board[0]) and
                    board[nr][nc] in node.children):
                    backtrack(nr, nc, node.children[board[nr][nc]], path + board[nr][nc])
            
            # Unmark this cell
            board[r][c] = temp

        root = self.insert(words)
        found_words = set()
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] in root.children:
                    backtrack(row, col, root.children[board[row][col]], board[row][col])
        
        return list(found_words)