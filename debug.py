import os
import time

import cv2
import numpy as np
from discord_funcs import theres_somebody_at_the_door
from dotenv import load_dotenv


def main():
    load_dotenv()
    URL = os.getenv('url')
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    ret, img = cap.read()
    cv2.imwrite("images/detected_person.jpg", img)
    theres_somebody_at_the_door(URL, os.getenv('alert_id'))
    os.remove("images/detected_person.jpg")

if __name__ == "__main__":
    main()