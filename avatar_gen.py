import requests
import time

DID_API_KEY = "Basic bWFuc2lqdmFyc2huZXkyMDAzbXRyQGdtYWlsLmNvbQ:PwlNj3hB6QnIr5UrhNiMM"

def generate_avatar_video(audio_path, output_file="avatar_output.mp4"):
    headers = {
        "Authorization": DID_API_KEY,
        "Content-Type": "application/json"
    }

    avatar_url = "https://create-images-results.d-id.com/DefaultImages/Emma-1.png"

    with open(audio_path, 'rb') as f:
        upload_res = requests.post(
            "https://api.d-id.com/audios",
            headers={"Authorization": DID_API_KEY},
            files={"file": f}
        )

    if upload_res.status_code != 200:
        print(f"[!] Audio upload failed: {upload_res.text}")
        return None

    audio_url = upload_res.json().get("url")
    if not audio_url:
        print("[!] Audio URL not received from D-ID")
        return None

    payload = {
        "script": {
            "type": "audio",
            "audio_url": audio_url,
            "provider": {"type": "none"}
        },
        "source_url": avatar_url,
        "config": {
            "fluent": True,
            "pad_audio": 0
        }
    }

    create_res = requests.post("https://api.d-id.com/talks", json=payload, headers=headers)
    if create_res.status_code != 200:
        print(f"[!] Video generation failed: {create_res.text}")
        return None

    talk_id = create_res.json().get("id")
    if not talk_id:
        print("[!] Talk ID not received")
        return None

    print("[⏳] Generating avatar video...")
    status_url = f"https://api.d-id.com/talks/{talk_id}"
    while True:
        status_res = requests.get(status_url, headers=headers)
        result_url = status_res.json().get("result_url")
        if result_url:
            break
        time.sleep(5)

    video_data = requests.get(result_url).content
    with open(output_file, "wb") as f:
        f.write(video_data)

    print(f"[✓] Avatar video saved as: {output_file}")
    return output_file
