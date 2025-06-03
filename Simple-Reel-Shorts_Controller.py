import cv2
import mediapipe as mp
import pyautogui
import time

class HandGestureShortsController:
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        if not self.cam.isOpened():
            print("Error: Could not open webcam.")
            exit()

        self.hands = mp.solutions.hands.Hands(max_num_hands=1)
        self.mp_drawing = mp.solutions.drawing_utils

        self.last_action = 0
        self.cooldown = 0.3  # seconds to avoid accidental double triggers
        self.movement_threshold = 0.035

        self.prev_y_index = None
        self.prev_y_thumb = None

    def detect_finger_movement(self, landmark_list, index):
        finger_tip = landmark_list.landmark[index]
        prev_y = self.prev_y_index if index == 8 else self.prev_y_thumb
        movement = False

        if prev_y is not None:
            if finger_tip.y - prev_y > self.movement_threshold:
                movement = True

        if index == 8:
            self.prev_y_index = finger_tip.y
        else:
            self.prev_y_thumb = finger_tip.y

        return movement

    def start(self):
        while True:
            ret, frame = self.cam.read()
            if not ret:
                print("Error: Failed to grab frame.")
                break

            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results_hands = self.hands.process(rgb_frame)
            image = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2BGR)

            if results_hands.multi_hand_landmarks:
                for hand_landmarks in results_hands.multi_hand_landmarks:
                    self.mp_drawing.draw_landmarks(image, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)

                    now = time.time()
                    if self.detect_finger_movement(hand_landmarks, 8) and (now - self.last_action) > self.cooldown:
                        pyautogui.press('up')
                        print("Index Finger Down: Previous Reel")
                        self.last_action = now

                    if self.detect_finger_movement(hand_landmarks, 4) and (now - self.last_action) > self.cooldown:
                        pyautogui.press('down')
                        print("Thumb Down: Next Reel")
                        self.last_action = now

            cv2.imshow('Reel Controller (Thumb & Index)', image)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cam.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    controller = HandGestureShortsController()
    controller.start()
