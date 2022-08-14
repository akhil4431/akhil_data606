import io
import os
import numpy as np
import streamlit as st
import cv2
import pickle
from PIL import Image

def load_image():
    uploaded_file = st.file_uploader(label='Pick an image to test')
    if uploaded_file is not None:
        image_data = uploaded_file.getvalue()
        st.image(image_data)
        pim = Image.open(io.BytesIO(image_data))
        nimg = np.array(pim)
        image = cv2.cvtColor(nimg, cv2.COLOR_RGB2BGR)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        if image is not None:
            image = cv2.resize(image, (255, 255))
            image = image.reshape(1,65025)
            return np.asarray(image)
    else:
        return None


def predictModel(categories, image):
    model = pickle.load(open("xmodel.pkl", 'rb'))
    pred = model.predict(image)[0]
    score = model.predict_proba(image)[0]
    print(pred, score)
    statement = "Predicted label is {} ".format(categories[pred])
    print(statement)
    st.write(statement)


def main():
    st.title('Leaf disease Recognition')
    categories = ['Anthracnose', 'algal leaf', 'bird eye spot', 'brown blight', 'gray light', 'healthy', 'red leaf spot', 'white spot']
    image = load_image()
    result = st.button('Run on image')
    if result:
        st.write('Calculating results...')
        predictModel(categories, image)


if __name__ == '__main__':
    main()
