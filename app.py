import streamlit as st
import create_jsonl as cj
from LineObject import LineObject

def clear_jsonl():
    st.session_state['l'] = l = []
st.title('Create JSON files to Fine-Tune OpenAI Models')
l = []
c1,c2 = st.columns([4,1],gap='large')
if 'l' not in st.session_state:
    st.session_state['l'] = l
with c1:
    prompt = st.text_input('**PROMPT**')
    completion = st.text_input('**COMPLETION**')
    if st.button('append line'):
        if prompt == "" or completion == "":
            st.markdown(':red[**please do not leave promp/completion blank**]') 
        else:
            st.session_state['l'].append(LineObject(prompt,completion))
with c2:
    PEND = st.text_input('prompt end')
    CEND = st.text_input('completion end')
    st.button('clear JSONL', on_click=clear_jsonl)

if not PEND:
    st.markdown(r':red[it is recommended that you use a prompt end such as \n\n###\n\n]')
if not CEND:
    st.markdown(r':red[it is recommended that you use a completion end such as ###]')
st.code(cj.get_jsonl_from_list(st.session_state['l'],PEND,CEND))

