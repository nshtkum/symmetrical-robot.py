from moviepy import VideoFileClip, ImageClip, TextClip, concatenate_videoclips

def create_project_video(
    avatar_path="avatar_output.mp4",
    images=[],
    slide_titles=[],
    output_file="final_project_video.mp4"
):
    clips = []
    for title in slide_titles:
        title_clip = TextClip(
            txt=title,
            fontsize=60,
            color='white',
            bg_color='black',
            size=(1280, 720)
        ).set_duration(2).fadein(0.5).fadeout(0.5)
        clips.append(title_clip)

    for img_path in images:
        img_clip = ImageClip(img_path).set_duration(3).resize(height=720).fadein(0.3).fadeout(0.3)
        clips.append(img_clip)

    avatar_clip = VideoFileClip(avatar_path).resize(height=720)
    clips.append(avatar_clip)

    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile(output_file, fps=24)

    print(f"[✓] Final video created: {output_file}")
    return output_file
