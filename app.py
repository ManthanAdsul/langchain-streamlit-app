import streamlit as st
from src.main import generate_names

st.set_page_config(
    page_title="LangChain Baby Name Generator",
    page_icon="👶",
    layout="centered"
)

st.title("👶 Baby Name Generator (LangChain)")
st.write("Generate Indian baby names using LangChain + OpenAI")

# Gender selection
gender = st.radio(
    "Select Gender:",
    ["Boy", "Girl"],
    horizontal=True
)

context = st.text_input(
    "Describe the baby:",
    placeholder="new born baby"
)

if st.button("Generate Names"):
    if context.strip():
        with st.spinner("Generating names..."):
            result = generate_names(
                context=context,
                gender=gender.lower()
            )
        st.success("Here are some suggestions:")
        st.write(result)
    else:
        st.warning("Please enter a description.")
