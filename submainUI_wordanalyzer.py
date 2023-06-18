import streamlit as st
import time

from file_process import *
from text_analyze import *
from visualizer import *

def clear_submit():
    st.session_state["submit"] = False

def word_analyzer():
    empty1,col1,empty2 = st.columns([0.1,1.4,0.1])
    empty1,col4,_,empty2 = st.columns([0.1,1,0.4,0.1])
    
    # sidebar
    with st.sidebar:
        with st.expander("Advanced Options"):
            show_word_count = st.checkbox("Show the number of counted words",value=True)
            show_chars_count = st.checkbox("Show the number of counted chars")
            show_chars_count_space = st.checkbox("Show the number of counted chars (including spaces)",value=True)
            show_word_average = st.checkbox("Show the average length of words")
            show_unique_word_count = st.checkbox("Show the number of unique words")
            show_most_common_plot = st.checkbox("Show most common words in bar graph")
    with col1:
        st.markdown("""
        <style>
        body {
            color: #000;
            background-color: blue;
        }
        </style>
            """, unsafe_allow_html=True)

        st.markdown("""
        # 📖Word Count Analyzer
        Enter the text you want to analyze in the text box below and select the analytics you want to perform from the *Advanced Options* section.
        """)    

        query = st.text_area("분석할 글을 입력하세요", on_change=clear_submit)





        if st.button("Submit"):
            with st.spinner('Wait for it...'):
                time.sleep(1)
            placeholder = st.empty()
            placeholder.success('Done!')
            time.sleep(1)
            placeholder.empty()

            with open('Query.txt','w',encoding='utf-8') as q:
                q.write(query)



        if query:  # Only analyze if query is not empty

            empty1,col1,empty2 = st.columns([0.3,1.0,0.3])

                
            words, word_list = read_file('Query.txt')

            # Create two columns with different widths
            col2, col3 = st.columns([2,2])

            with col2:
                st.markdown("<br/>"*2, unsafe_allow_html=True)

            if show_word_count:
                with col2:
                    st.write('Word count:', word_list.count_words())
            if show_chars_count:
                with col2:
                    st.write('Character count (excluding spaces):', word_list.count_chars())
            if show_chars_count_space:
                with col2:
                    st.write('Character count (including spaces):', word_list.count_chars_spaces())
            if show_word_average:
                with col2:
                    st.write('Average word length:', word_list.calculate_avg_word_length())
            if show_unique_word_count:
                with col2:
                # 단어 트리 만들기
                    word_tree = BinaryTree()

                # 트리에 단어 삽입하기
                for word in words:
                    word_tree.insert(word)

                # unique 단어 개수 세기
                with col2:
                    st.write('Unique word count:', word_tree.count_unique_words())
            if show_most_common_plot:

                # Plot most common words
                top_words, frequencies = most_common_words(words, N=10)
                fig = plot_word_frequency_distribution(words)

                # Use the columns
                col3.subheader('🥇🥈 Word Frequency distribution')
                col3.pyplot(fig,use_container_width=True)

            # st.balloons()


        else:
            st.error("Please enter words!")