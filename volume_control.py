import cv2
import mediapipe as mp
import pyautogui

x1 = y1 = x2 = y2 = 0

cap = cv2.VideoCapture(0)
my_hands = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

while True:
    red, img = cap.read()
    img = cv2.flip(img, 1)
    h, w, c = img.shape

    rgbImage = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = my_hands.process(rgbImage)
    hands = results.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(img, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * w)
                y = int(landmark.y * h)
                if id == 8:
                    cv2.circle(img=img, center=(x, y), radius=8, color=(0, 255,255), thickness=3)
                    x1 = x
                    y1 = y
                if id == 4:
                    cv2.circle(img=img, center=(x, y), radius=8, color=(255, 0,255), thickness=3)
                    x2 = x
                    y2 = y
        dist = ((x2-x1)**2 + (y2-y1)**2)**(0.5)//4
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 5)
        if dist > 25:
            pyautogui.press("volumeup")
        else:
            pyautogui.press("volumedown")

    cv2.imshow("Image", img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
