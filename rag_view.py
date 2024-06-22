import streamlit as st 
import rag_model as model

st.set_page_config(page_title="Hira (HR Assistant)") ### Modify Heading

new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">Hira : HR Assistant 🎯</p>'
st.markdown(new_title, unsafe_allow_html=True) ### Modify Title

if 'vector_index' not in st.session_state: 
    with st.spinner("📀 Wait for magic...All beautiful things in life take time :-)"): ###spinner message
        st.session_state.vector_index = model.hr_index() ### Your Index Function name from Backend File

input_text = st.text_area("Got questions about our company policy? I'm here to help—ask me anything!") 
go_button = st.button("📌submit", type="primary") ### Button Name

if go_button: 
    
    with st.spinner("📢Anytime someone tells me that I can't do something, I want to do it more - Taylor Swift"): ### Spinner message
        response_content = model.hr_rag_response(index=st.session_state.vector_index, question=input_text) ### replace with RAG Function from backend file
        st.write(response_content) 