class TreeNode:
    def __init__(self, word):
        self.word = word
        self.left = None
        self.right = None
        self.num = 0  # 특정 단어 검색 시 개수를 출력하기 위한 변수


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, word):  # 단어 삽입 함수
        if self.root == None:
            self.root = TreeNode(word)
        else:
            self._insert_recursive(self.root, word)

    def _insert_recursive(self, node, word): # 단어 삽입을 위한 재귀함수
        if word < node.word:
            if node.left != None :
                self._insert_recursive(node.left, word)
            else:
                node.left = TreeNode(word)
        elif word > node.word:
            if node.right:
                self._insert_recursive(node.right, word)
            else:
                node.right = TreeNode(word)
        else:
            node.num += 1

    # unique_words가 set일때
    
    def _count_unique_words_recursive(self, node, unique_words):  # unique 단어 수 세기를 위한 재귀함수
        if node != None:
            if node.word not in unique_words:
                unique_words.add(node.word)
            self._count_unique_words_recursive(node.left, unique_words)
            self._count_unique_words_recursive(node.right, unique_words)
    
    def count_unique_words(self): # unique 단어 수 세기 (함수)

        unique_words = set()        # unique_words = list()
        self._count_unique_words_recursive(self.root, unique_words)
        print(unique_words)
        return len(unique_words)
    
if __name__ == '__main__':
    print('실행완료')
