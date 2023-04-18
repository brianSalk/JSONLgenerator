import streamlit as st

l = ['first']
sym = st.text_input('text to add')
if st.button('press to append'):
    l.extend(sym)
st.text(l)

