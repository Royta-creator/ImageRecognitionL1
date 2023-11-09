# Roy TAMWO 01/10/2023

import tkinter as tk
from tkinter import filedialog
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input, decode_predictions
import numpy as np
import pyttsx3
engine = pyttsx3.init()
root = tk.Tk()
root.withdraw()
#Initialisation de la voix
def text_to_speech(text):
    engine.setProperty('rate', 150) 
    engine.setProperty('volume', 0.9) 

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    engine.say(text)
    engine.runAndWait()
#Preparation du model basé sur inceptionV3 au moment de ImageNet
def load_model():
    return InceptionV3(weights='imagenet')

def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(299, 299))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return preprocess_input(img_array)

def predict_animal(model, img_array):
    predictions = model.predict(img_array)
    decoded_predictions = decode_predictions(predictions, top=1)[0]

    for i, (_, label, score) in enumerate(decoded_predictions):
        print(f"{i}: {label} ({score:.2f})")
        text_to_speech(f"the image seems to represent a {label}")
#Chatbot pour prendre les inputs de l'utilisateur
def chatbot():
    print("Chatbot: Hello! I'm your image recognition chatbot.")
    text_to_speech("Hello! I'm your image recognition chatbot.")

    
    while True:
        user_input = input("You: ").lower()

        if user_input == 'quit':
            print("Chatbot: Goodbye!")
            text_to_speech("Goodbye!")

            break

        elif "recognize image" in user_input:
            text_to_speech("Choose an image")
            root.lift()
            root.attributes('-topmost',True)
            root.after_idle(root.attributes,'-topmost',False)
            img_path = filedialog.askopenfilename(title="Choose an image")
            model = load_model()
            img_array = preprocess_image(img_path)
            predict_animal(model, img_array)

        else:
            text_to_speech("I'm not sure how to respond to that. You can ask me to recognize an image.")
            print("Chatbot: I'm not sure how to respond to that. You can ask me to recognize an image.")

if __name__ == "__main__":
    chatbot()
