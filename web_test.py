# streamlit run web_test.py

from file_process import *
from text_analyze import *
from visualizer import *
from submainUI_About import *
from submainUI_wordanalyzer import *
from submainUI_contact import *
from streamlit_option_menu import option_menu

import streamlit as st
import time
from tomlkit import dump, load



# page setting
st.set_page_config(
    page_title="위대하신 백승유님의 Word Count Analyzer",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)



# Sidebar

with st.sidebar:
    background = st.radio(
        "Choose a background color",
        ("White", "Black")
    )
    print(background,'변수이름')

#    set_background_color(background)

    if background != "White":
        option_menu_backcolor = "#fafafa"
    else:
        option_menu_backcolor = "#000000"


    choose = option_menu("App Gallery", ["About", "word analyzer", "Project Planning", "Python e-Course", "Contact"],
                         icons=['house', 'camera fill', 'kanban', 'book','person lines fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": option_menu_backcolor},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )

# main UI

# word analyzer page
if choose == "About":
    About()
        
elif choose == "word analyzer":
    word_analyzer()

elif choose == "Contact":
    Contact()









