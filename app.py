import streamlit as st
from typing import Any
import os
from backend import progress_bar, generate_text_from_image, generate_story_from_text, generate_speech_from_text

st.set_page_config(page_title="IMAGE TO STORY CONVERTER", page_icon="🖼️")



# Streamlit app layout
st.header("Image-to-Story Converter")
uploaded_file: Any = st.file_uploader("Please choose a file to upload", type="jpg")

if uploaded_file is not None:
    bytes_data: Any = uploaded_file.getvalue()
    with open(uploaded_file.name, "wb") as file:
        file.write(bytes_data)
        
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    progress_bar(100)
    scenario: str = generate_text_from_image(uploaded_file.name)
    story: str = generate_story_from_text(scenario)
    generate_speech_from_text(story)

    with st.expander("Generated Image Scenario"):
        st.write(scenario)
    with st.expander("Generated Short Story"):
        st.write(story)
    with st.expander("Generated Audio File"):
        st.audio(generated_audio.wav)


# Set the title of the app
st.title("Image-to-Story App")

# Add a sidebar
st.sidebar.title("Navigation")

# Add buttons in the sidebar
if st.sidebar.button("Explain Project"):
    st.sidebar.write("This project takes an image input and generates a story from it. "
                     "It uses deep learning models to process the image and convert it into meaningful text, "
                     "followed by speech synthesis to narrate the story.")

if st.sidebar.button("GitHub Repo"):
    st.sidebar.write("[Visit the GitHub Repository](https://github.com/ajay2k4/Image-Story-using-LLMs)")

if st.sidebar.button("LinkedIn"):
    st.sidebar.write("[Visit LinkedIn Profile](https://www.linkedin.com/in/YourProfile)")

# Add a main body content
st.write("Upload your image on the main page and see the project in action!")


x = st.slider('Select a value')
st.write(x, 'squared is', x * x)

