# import necessary libraries
import os
import json
import openai
import streamlit as st

# set your openAI API key
from dotenv import dotenv_values
config = dotenv_values('.env')  
openai.api_key = config['OPENAI_API_KEY']

print(openai.api_key[0])  

def display_color_blocks(colors):
    """
    This function displays a block of colors from a given list of hexcodes.

    Args:
        colors (list): A list of color hexcode.
    """
    # create a markdown to display the color block
    color_blocks = " ".join(f"<span style='display: inline-block; width: 40px; height: 40px; background: {color};'></span>" for color in colors)
    st.markdown(color_blocks, unsafe_allow_html=True)

def color_ai(msg):
    """
    Generate a color palette based on the user's input message.

    Args:
        msg (str): A string that describes the desired color palette.

    Returns:
        colors (list): A list of hex color codes.
    """
    # create a prompt for the color palette generation model
    prompt = f"""
    You are a color palette generator that uses user's text prompts to generate color palettes.
    You should generate color palettes based on user's theme, mood, and requirements. The palette should be between 5 to 8 colors.

    Q: Generate a color palette for the beach.
    A: ["#255e65", "#3591a0", "#4da6c4", "#7ac1d0", "#b3dfe3"]

    Desired Format: a JSON array of hex color codes.

    Q: Convert the following user description of a color palette into a list of colors: {msg}
    A:
    """
    # generate color using ai
    response = openai.Completion.create(
        prompt=prompt,
        model='text-davinci-003',
        max_tokens=300,
        temperature=1
    )
    # parse color from response
    colors = json.loads(response['choices'][0]['text'])
    # Display color blocks
    display_color_blocks(colors)
    return colors

# Streamlit UI
st.title('AI Color Palette Generator')
user_input = st.text_input('Enter a description of the color you want to create:')
if st.button('Generate'):
    colors = color_ai(user_input)
    st.write(colors)
