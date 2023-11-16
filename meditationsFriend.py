
from pathlib import Path
from openai import OpenAI
client = OpenAI()

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

mymedscript = "Relax and close your eyes. Get comfortable either lying down or sitting against some pillows. Breathe deeply and begin to become aware of your breath."

speech_file_path = Path(__file__).parent / "meditationFriendAnxiety.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="onyx",
  input=mymedscript
)

response.stream_to_file(speech_file_path)

def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to Wolf Cove Labs! 👋")
    st.markdown(
        """
       Welcome to my very first amazing streamlit app with OpenAI!!! WOO. 
    """
    )


if __name__ == "__main__":
    run()



