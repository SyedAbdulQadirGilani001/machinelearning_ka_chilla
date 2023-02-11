import streamlit as st
from PIL import Image
st.write("""
# Add Media to Streamlit
""")
st.write("## Image")
image = Image.open('science.aas9893.fp.png')
st.image(image, caption='The Snow Leopard', use_column_width=True)
st.write("## Video")
video_file = open('Snow Leopards 101 _ Nat Geo Wild.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
st.write("## Audio")
audio_file = open('1605676949_8s685x685x5x4x4ktm65x645685x6ktm65x6456.mp3', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/mp3')
