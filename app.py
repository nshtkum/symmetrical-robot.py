import streamlit as st
import os

from scraper import scrape_magicbricks_project
from script_gen import generate_project_script
from tts import generate_tts_audio
from avatar_gen import generate_avatar_video
from video_editor import create_project_video

os.makedirs("assets", exist_ok=True)

st.set_page_config(page_title="Magicbricks AI Video Generator", layout="wide")

st.title("🏡 Magicbricks Project → AI Video 🎬")
st.markdown("Paste any [Magicbricks](https://www.magicbricks.com) project page URL below to generate an AI-powered video summary.")

url = st.text_input("Enter Magicbricks Project URL")

if st.button("Generate AI Video") and url:
    with st.spinner("🔍 Scraping project details..."):
        project_data = scrape_magicbricks_project(url)
    
    st.success("✅ Scraped project data:")
    st.json(project_data)

    with st.spinner("✍️ Generating script with GPT..."):
        script = generate_project_script(project_data, language="English")
    
    st.text_area("Generated Script", script, height=200)

    with st.spinner("🎧 Generating voiceover..."):
        audio_path = "assets/output_audio.mp3"
        generate_tts_audio(script, language="en", output_file=audio_path)

    with st.spinner("🧑 Generating AI face video..."):
        avatar_path = "assets/avatar_output.mp4"
        generate_avatar_video(audio_path, output_file=avatar_path)

    with st.spinner("🎞️ Stitching final video..."):
        image_files = []  
        title_slides = ["Project Overview", "Key Amenities", "Location Insights"]
        final_video = create_project_video(
            avatar_path=avatar_path,
            images=image_files,
            slide_titles=title_slides,
            output_file="assets/final_video.mp4"
        )

    st.success("🎉 Video Generated Successfully!")
    st.video("assets/final_video.mp4")

    with open("assets/final_video.mp4", "rb") as f:
        st.download_button("⬇️ Download Video", f, file_name="magicbricks_video.mp4", mime="video/mp4")

else:
    st.info("ℹ️ Enter a Magicbricks URL and click the button to get started.")
