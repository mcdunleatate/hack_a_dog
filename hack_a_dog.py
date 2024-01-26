import streamlit as st
from PIL import Image, ImageOps
import io
import time
import pickle


def loading():  
    
    loading_placeholder = st.empty()

    loading_html = """
        <style>
            .loading-container {
                position: absolute;
                top: 50%;
                left: 48.5%;
                transform: translate(-50%, -50%);
                margin-top: -750px;
                z-index: 3; 
            }
            
            .dot-container {
                display: flex;
                flex-direction: column;
                align-items: center;
                transform: rotate(90deg);
            }
            
            .dot {
                width: 50px;
                height: 50px;
                background-color: #FF0000;
                border-radius: 50%;
                margin: 0 5px;
                animation: bounce 0.5s ease-in-out infinite alternate;
            }
            .dot:nth-child(2) {
                animation-delay: 0.1s;
            }
            .dot:nth-child(3) {
                animation-delay: 0.2s;
            }
            @keyframes bounce {
                to {
                    transform: translateY(-10px);
                }
            }
            .evaluating-text { 
                margin-top:25px;
                margin-right:0px;
                position: relative;
                font-size: 70px; 
                color: #FF0000;
                font-weight: bold;
                text-shadow: 2px 2px 2px black;
            }
        </style>
        <div class="loading-container">
            <div class="dot-container">
                <div class="dot"></div>
                <div class="dot"></div>
                <div class="dot"></div>
            </div>
            <p class="evaluating-text">Evaluating</p>
        </div>
    """
    #st.markdown(loading_html, unsafe_allow_html=True)
    
    loading_placeholder.markdown(loading_html, unsafe_allow_html=True)
    
    
    time.sleep(1)

  
    loading_placeholder.empty()

    
def main():
    # Set page title and icon
    st.set_page_config(page_title="Hack-A-Dog", page_icon="🌭")

    ### Title
    title_placeholder = st.empty()
    
    title_html = """
        <style>
            .title-bar {
                background-color: red;
                padding: 1px;
                border-radius: 15px;
                display: flex;
                width: 100%;
                box-sizing: border-box;
                justify-content: center;
                align-items: center;
                position: absolute;
                z-index: 2;
                top: 0;
            }
            .title-text {
                color: white;
                margin: 0;
                font-size: 75px;
                margin-right: -25px;
            }
        </style>
        <div class="title-bar">
            <h1 class="title-text">SEEFOOD</h1>
        </div>
    """
    
    title_placeholder.markdown(title_html, unsafe_allow_html=True)
    
    
    shazam_placeholder = st.empty()
    shazam_html = """
            <div style="background-color: white; padding: 0px; border-radius: 15px; position: absolute; z-index: 1; margin-top: 109px; width: 100%;">
                <p style="color: red; text-align: center; font-size: 15px; position: relative; top: 15px; left: 48%; transform: translateX(-50%); z-index:;">Shazam for Food!</p>
            </div>
        """
    
    shazam_placeholder.markdown(shazam_html, unsafe_allow_html=True)
    ### image
    
    hotdog_img = Image.open("./images/assorted_hotdog.jpg")
    
    grayscale_image = ImageOps.grayscale(hotdog_img)

    

    displayed_image = st.image(grayscale_image, use_column_width=True)
    
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    with open('./pickles/model.pkl', 'rb') as file:
        trained_model = pickle.load(file)
    
    
    if uploaded_file is not None:
        
        title_placeholder.empty()
        shazam_placeholder.empty()
        loading()
        
        image = Image.open(uploaded_file)
        displayed_image.image(image, use_column_width=True)

        
        st.markdown(
            f'<p style="color: lime; text-align: center; font-size: 40px; position: relative; margin-right: 0px; top: -200px;">✔️ Result ✔️</p>',
            unsafe_allow_html=True
        )
        

if __name__ == "__main__":
    main()