import os
import time

import cv2
import torch
from discord_funcs import theres_somebody_at_the_door
from dotenv import load_dotenv
from transformers import YolosImageProcessor, YolosForObjectDetection


def main():
    load_dotenv()
    URL = os.getenv('url')
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    model = YolosForObjectDetection.from_pretrained('hustvl/yolos-tiny')
    image_processor = YolosImageProcessor.from_pretrained('hustvl/yolos-tiny')

    print('Loaded Model.')

    while True:
        ret, img = cap.read()

        inputs = image_processor(images=img, return_tensors="pt")
        outputs = model(**inputs)

        logits = outputs.logits
        bboxes = outputs.pred_boxes

        height, width = img.shape[:2]

        target_sizes = torch.tensor([[height, width]])

        results = image_processor.post_process_object_detection(
            outputs, threshold=0.6, target_sizes=target_sizes)[0]

        for score, label, box in zip(results['scores'], results['labels'], results['boxes']):

            if model.config.id2label[label.item()] != 'person':
                continue

            box = [round(i, 2) for i in box.tolist()]

            print(
                f"Detected {
                    model.config.id2label[label.item()]} with confidence "
                f"{round(score.item(), 3)} at location {box}"
            )
            x1, y1, x2, y2 = box
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            confidence = round(score.item(), 3) * 100

            print('Confidence --->', confidence)
            print('Class name --->', model.config.id2label[label.item()])

            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2

            cv2.putText(img, model.config.id2label[label.item(
            )], org, font, fontScale, color, thickness)
            cv2.imwrite("images/detected_person.jpg", img)
            # cv2.imshow('Webcam', img)
            theres_somebody_at_the_door(URL, os.getenv('alert_id'))
            os.remove("images/detected_person.jpg")
            time.sleep(30)

        print('frame')
        time.sleep(3)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
