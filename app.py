import streamlit as st
import create_jsonl as cj
import fonts
from LineObject import LineObject
prompt_help = "An prompt to give to machine learning model"
completion_help = "An ideal completion for the above prompt"
PEND_help = """a unique string that indicates the end of a prompt\n
OpenAI recommends \\n\\n###\\n\\n"""
CEND_help = """a unique string that indicates the end of a completion\n
OpenAI recommends ###"""
if 'clear_jsonl_btn' not in st.session_state:
    st.session_state['clear_jsonl_btn'] = False
def clear_jsonl():
    st.session_state['l'] = l = []
def run_app():
    with st.sidebar:
        st.markdown(fonts.tangerine("Created by Brian Salkas"),unsafe_allow_html=True )
        st.markdown("# How to use:")
        st.markdown("### **1)** Enter your desired **prompt** and **completion** into the text fields to the right")  
        st.markdown("### **2)** Optionally adjust the prompt/completion end tokens")
        st.markdown("### **3)** Click 'Append To JSONL File' to append the prompt and completion to the JSONL file")
        st.markdown("### **4)** optionally click **clear input** to clear promt/completion or click **clear file** to start over")
        st.markdown("### **5)** Repeat the above steps until you are done creating your JSONL file")
        st.markdown("### **6)** Copy the file to your clipboard by clicking in the upper-right corner of the generated text.")
        st.markdown("I am very greatful for **any and all** contributions.  github page [here](https://github.com/brianSalk/finetuneAI)")
    def clear_fields():
        st.session_state['input_completion'] = ""
        st.session_state['input_prompt'] = ""
    st.title('Create JSON Files to Fine-Tune OpenAI Models')
    l = []
    c1,c2 = st.columns([4,1],gap='medium')
    if 'l' not in st.session_state:
        st.session_state['l'] = l
    with c1:
        prompt = st.text_input('**PROMPT**',key='input_prompt'
                ,help = prompt_help)
        completion = st.text_input('**COMPLETION**',key='input_completion',
                help = completion_help)
        if st.button('Append To JSONL file'):
            if completion == "" or prompt == "":
                st.markdown(':red[**Do not leave prompt or completion blank**]')
            else:
                st.session_state['l'].append(LineObject(prompt,completion))

    with c2:
        PEND = st.text_input('prompt end',key='TI3',help=PEND_help,
                value = r"\n\n###\n\n")
        CEND = st.text_input('completion end',key='TI4',help=CEND_help,
                value = "###")
        st.button('clear input', on_click=clear_fields)
        st.title("")

        if  st.button("clear file") or st.session_state['clear_jsonl_btn']:
            st.session_state['clear_jsonl_btn'] = True
            if st.button("confirm"):
                st.session_state['clear_jsonl_btn'] = False
                clear_jsonl()
                st.experimental_rerun()
            if st.button("cancel"):
                st.session_state['clear_jsonl_btn'] = False
                st.experimental_rerun()

    if not PEND:
        st.markdown(r':red[it is recommended that you use a prompt end such as \n\n###\n\n]')
    if not CEND:
        st.markdown(r':red[it is recommended that you use a completion end such as ###]')
    st.markdown(":blue[*your JSON file is below, when you are done creating it click in the upper right corner of the below text field to copy the text to your clipboard*]")
    st.code(cj.get_jsonl_from_list(st.session_state['l'],PEND,CEND),language="json")
if __name__ == "__main__":
    run_app()
