import streamlit as st
import pytorch_m


st.title('Animal Identifier')
st.markdown(
    """
Identify your animal breed in 2 simple steps:
- Upload a picture of your animal
- Get a prediction of your animal's true breed
"""
)

image_file = st.file_uploader('Upload your animals picture here')

if image_file is not None:
    predict = st.button('predict breed', type = "primary")

    if predict:
        class_id, class_name  = pytorch_m.get_prediction(image_file)

        st.write(f"This animal is a {class_name}")
        st.image(image_file)