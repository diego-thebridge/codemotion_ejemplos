import streamlit as st
import random
import time
from streamlit_js_eval import streamlit_js_eval
from geometry_agent import create_main_agent
from langchain_community.callbacks import get_openai_callback

with st.sidebar:
        st.subheader("Configuration")
        if st.button("Restart"):
            st.session_state.main_agent = create_main_agent()
            streamlit_js_eval(js_expressions="parent.window.location.reload()")
            

st.title("Geometry assistant")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.main_agent = create_main_agent()

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Type yor query"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        #response = st.write_stream(response_generator())

        with st.spinner("Processing ..."):

            response = st.session_state.main_agent.invoke({"input":prompt})
            st.write(response['output'])
            st.write("---------------")
            for item in response["intermediate_steps"]:
                st.write(item[0].log)
           


        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})