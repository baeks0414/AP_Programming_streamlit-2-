from file_process import *
from text_analyze import *
from visualizer import *

words, word_list = read_file('document.txt')

# 총 단어 수 세기
total_word_count = word_list.count_words()
print("Total Word Count:", total_word_count)

# 총 글자 수 세기
total_chars_count = word_list.count_chars()
print("Total Characters Count:", total_chars_count)

# 총 글자 수 세기 (공백 포함)
total_chars_count_space = word_list.count_chars_spaces()
print("Total Characters Count (include space):", total_chars_count_space)

# 평균 단어 길이 계산
average_word_length = word_list.calculate_avg_word_length()
print("Average Word Length:", average_word_length)

# 단어 트리 만들기
word_tree = BinaryTree()

# 트리에 단어 삽입하기
for word in words:
    word_tree.insert(word)

# unique 단어 개수 세기
unique_word_count = word_tree.count_unique_words()
print("Unique Word Count:", unique_word_count)

plot_word_frequency_distribution(words)