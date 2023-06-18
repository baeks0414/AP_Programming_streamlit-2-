class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, word):  # 새단어 연결 함수
        new_node = Node(word)
        if self.head == None :  # 만약 head가 없으면
            self.head = new_node
        else: # 만약 이미 헤드가 있으면
            current = self.head
            while current.link:
                current = current.link
            current.link = new_node

    def count_words(self): # 단어 수 세는 함수
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.link
        return count
    
    def count_chars(self): # 글자 수 세는 함수
        count = 0
        current = self.head
        while current:
            count += len(current.data)
            current = current.link
        return count
    
    def count_chars_spaces(self): # 공백포함 글자 수 세는 함수
        count = 0
        current = self.head
        while current:
            count += len(current.data)
            count += 1 # 공백 포함
            current = current.link
        return count-1

    def calculate_avg_word_length(self):  # 단어의 평균 길이 추출함수
        total_length = 0
        word_count = 0
        current = self.head
        while current:
            total_length += len(current.data)
            word_count += 1
            current = current.link
        if word_count == 0:
            return 0
        return total_length / word_count


# 연결 리스트를 만들고 단어를 불러와 연결하는 (함수)
def read_file(path):
    word_list = LinkedList()
    with open(path,'r',encoding = 'utf-8') as file:
        document = file.read()
    words = document.split()
    for word in words:
        word_list.insert(word)
    return words, word_list

if __name__ == '__main__':
    print('실행중')
    words, word_list = read_file('document.txt')
    print(word_list.count_words())
    print(word_list.calculate_avg_word_length())
