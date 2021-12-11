# Streamlit Image-Comparison Component Example

import streamlit as st
from streamlit_image_comparison import image_comparison

# set page config
st.set_page_config(page_title="Image-Comparison Example", layout="centered")

# render image-comparison
image_comparison(
    img1="image1.jpg",
    img2="image2.jpg",
)