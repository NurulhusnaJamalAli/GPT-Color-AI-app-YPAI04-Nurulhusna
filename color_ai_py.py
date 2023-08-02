#%%
# import necessary libraries
import os
import json
import openai
from IPython.display import HTML, display

#%%
# set your openAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

#%%
def display_color_blocks(colors):
    """
    This function displays a block of colors from a given list of hexcodes.

    Args:
        colors (list): A list of color hexcode.

    """
    # create a markdown to display the color block
    color_blocks = " ".join(f"<span style='color: {color}'>{chr(9608) * 5}</span>" for color in colors)
    display(HTML(color_blocks))

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

# Test the function with various inputs
print(color_ai("generate disney color palette"))
print(color_ai("5 pink"))
print(color_ai("create high contrast ugly color that hurt eyes"))
print(color_ai("neon color for my personal portfolio website"))
print(color_ai("aesthethic and unique colors for my personal portfolio website"))
print(color_ai("palette with this color #b9ea3a"))
print(color_ai("pastel palette for my  data visualization"))
print(color_ai('generate 2000 colors'))