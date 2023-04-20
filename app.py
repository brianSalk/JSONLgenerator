import streamlit as st
import create_jsonl as cj
from LineObject import LineObject
def run_app():
    def clear_fields():
        st.session_state['comp'] = st.session_state['input_completion']
        st.session_state['input_completion'] = ""
        st.session_state['prompt'] = st.session_state['input_prompt']
        st.session_state['input_prompt'] = ""
    st.title('Create JSON files to Fine-Tune OpenAI Models')
    l = []
    c1,c2 = st.columns([4,1],gap='large')
    if 'l' not in st.session_state:
        st.session_state['l'] = l
    l = ['first']
    with c1:
        st.text_input('**PROMPT**',key='input_prompt')
        st.text_input('**COMPLETION**',key='input_completion')
        if st.button('append line',on_click=clear_fields):
            completion = st.session_state['comp']
            prompt = st.session_state['prompt']
            st.session_state['l'].append(LineObject(prompt,completion))


    with c2:
        PEND = st.text_input('prompt end',value="",key='TI3')
        CEND = st.text_input('completion end',key='TI4')

    if not PEND:
        st.markdown(r':red[it is recommended that you use a prompt end such as \n\n###\n\n]')
    if not CEND:
        st.markdown(r':red[it is recommended that you use a completion end such as ###]')
    st.code(cj.get_jsonl_from_list(st.session_state['l'],PEND,CEND))
if __name__ == "__main__":
    run_app()
