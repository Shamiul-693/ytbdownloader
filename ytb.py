import os
from yt_dlp import YoutubeDL
import streamlit as st

# Streamlit app layout
st.title("YouTube Video Downloader")
st.write("Paste the YouTube URL below to download your video.")

# Input field for video URL
video_url = st.text_input("Enter YouTube URL:", "")

if st.button("Download"):
    if video_url:
        try:
            # Set download options
            ydl_opts = {
                'format': 'best',
                'outtmpl': '%(title)s.%(ext)s',
            }

            # Download video
            st.write("Downloading...")
            with YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(video_url, download=True)
                file_name = ydl.prepare_filename(info_dict)

            st.success(f"Download complete: {file_name}")
            with open(file_name, "rb") as file:
                st.download_button(
                    label="Download Video",
                    data=file,
                    file_name=file_name,
                    mime="video/mp4",
                )

            # Cleanup the file from the server
            os.remove(file_name)

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a valid YouTube URL.")
