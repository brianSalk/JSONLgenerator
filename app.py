import streamlit as st
import create_jsonl as cj
from LineObject import LineObject
def clear_jsonl():
    st.session_state['l'] = l = []
def run_app():
    def clear_fields():
        st.session_state['input_completion'] = ""
        st.session_state['input_prompt'] = ""
    st.title('Create JSON Files to Fine-Tune OpenAI Models')
    l = []
    c1,c2 = st.columns([4,1],gap='medium')
    if 'l' not in st.session_state:
        st.session_state['l'] = l
    with c1:
        completion = st.text_input('**PROMPT**',key='input_prompt')
        prompt = st.text_input('**COMPLETION**',key='input_completion')
        if st.button('append line'):
            if completion == "" or prompt == "":
                st.markdown(':red[**Do not leave prompt or completion blank**]')
            else:
                st.session_state['l'].append(LineObject(prompt,completion))

    with c2:
        PEND = st.text_input('prompt end',value="",key='TI3')
        CEND = st.text_input('completion end',key='TI4')
        st.button('clear input', on_click=clear_fields)
        st.title("")
        st.button("clear JSONL",on_click=clear_jsonl)
    if not PEND:
        st.markdown(r':red[it is recommended that you use a prompt end such as \n\n###\n\n]')
    if not CEND:
        st.markdown(r':red[it is recommended that you use a completion end such as ###]')
    st.code(cj.get_jsonl_from_list(st.session_state['l'],PEND,CEND))
if __name__ == "__main__":
    run_app()
