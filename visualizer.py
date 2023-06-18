import matplotlib.pyplot as plt
import seaborn as sns

def most_common_words(words,N=3):  # 단어들 전처리 후 빈도수대로 추출 (함수)
    '''
     words는 단어 단위로 구분된 리스트
    '''
    # 기호 삭제, '모양'='모양.' 이 되도록 기호들 삭제된 words
    cl_words = []
    for word in words:
        word = word.strip(' .:,?!')
        if len(word) != 0:
            cl_words.append(word)

    # 각 단어의 빈도수 (dict 이용)
    word_freq = {}
    for word in cl_words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

    # 가장 빈도수가 높은 top10 추출
    try:  # 입력된 N이 현재 총 단어수보다 많은 경우 (예외처리)
        if len(sorted_words) < N:
            raise Exception('Words N Error')
        top_words = [word[0] for word in sorted_words[:N]]
        frequencies = [word[1] for word in sorted_words[:N]]
        return top_words, frequencies
    except Exception as e:
        print('오류 발생-->',e)
        print('입력하신 N의 값이 전체 단어 수 보다 많습니다.')
        print('N을 현재 단어수로 자동 조정합니다.')
        print(f'N: {N} --> {len(sorted_words)}')
        top_words = [word[0] for word in sorted_words[:]]
        frequencies = [word[1] for word in sorted_words[:]]
        return top_words, frequencies

def plot_word_frequency_distribution(words):
    from matplotlib import font_manager, rc 
    font_path = "C:/Windows/Fonts/batang.ttc"
    font = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font)

    top_words, frequencies = most_common_words(words, N=10)

    plt.style.use('ggplot')  # Use ggplot style for more attractive graphs
    fig, ax = plt.subplots(figsize=(10, 6))  # Set the size of your graph
    color_palette = sns.color_palette("Blues_d", len(top_words))  # Create color palette
    sns.barplot(x=top_words, y=frequencies, palette=list(reversed(color_palette)))  # Reverse color palette
    ax.set_xlabel('Words', fontsize=14)  # Set x label
    ax.set_ylabel('Frequency', fontsize=14)  # Set y label
    ax.set_title('Word Frequency Distribution', fontsize=16)  # Set title
    ax.grid(True)  # Show grid
    return fig



# TEST
if __name__ == '__main__':
    test=['가','나','다','라:',':']
    plot_word_frequency_distribution(test)
    most_common_words(test)
