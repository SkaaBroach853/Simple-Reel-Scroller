import cv2
import mediapipe as mp
import pyautogui
import time

class FaceControlShorts:
    def __init__(self):
        # Initialize webcam
        self.cam = cv2.VideoCapture(0)
        if not self.cam.isOpened():
            print("Error: Could not open webcam.")
            exit()

        # Initialize face mesh detector
        self.face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
        # Initialize hand detector
        self.hands = mp.solutions.hands.Hands(max_num_hands=1)
        self.mp_drawing = mp.solutions.drawing_utils
        # Cooldown to prevent multiple triggers
        self.last_action = 0
        self.cooldown = 0.005  # Cooldown time in seconds
        
        # Movement thresholds for gestures
        self.movement_threshold = 0.035  # Threshold for detecting finger movement
        self.mouth_open_threshold = 0.04 # Threshold for detecting mouth open (not used anymore)

        # Store previous y positions for index finger and thumb
        self.prev_y_index = None
        self.prev_y_thumb = None

        # For pinch-to-zoom (kept as placeholder, but not actively used for control)
        self.initial_pinch_distance = None
        self.zoom_sensitivity = 0.05 # Adjust as needed

    # --- Helper function for distance calculation ---
    def euclidean_distance(self, p1, p2):
        return ((p2.x - p1.x)**2 + (p2.y - p1.y)**2)**0.5

    # --- Mouth Detection --- (function kept but not used)
    def detect_mouth_open(self, landmarks):
        upper_lip = landmarks[13]
        lower_lip = landmarks[14]
        return (lower_lip.y - upper_lip.y) > self.mouth_open_threshold

    # --- Index Finger Movement Detection ---
    def detect_index_finger_down_movement(self, hand_landmarks):
        if not hand_landmarks:
            self.prev_y_index = None
            return False

        index_finger = hand_landmarks.landmark[8]
        
        downward_movement = False
        
        if self.prev_y_index is not None:
            if index_finger.y - self.prev_y_index > self.movement_threshold:
                downward_movement = True
        
        self.prev_y_index = index_finger.y
        return downward_movement

    # --- Thumb Movement Detection ---
    def detect_thumb_down_movement(self, hand_landmarks):
        if not hand_landmarks:
            self.prev_y_thumb = None
            return False

        thumb_tip = hand_landmarks.landmark[4]
        
        thumb_downward_movement = False
        
        if self.prev_y_thumb is not None:
            if thumb_tip.y - self.prev_y_thumb > self.movement_threshold:
                thumb_downward_movement = True
        
        self.prev_y_thumb = thumb_tip.y
        return thumb_downward_movement

    # --- Pinch-to-Zoom Detection (Conceptual - not used) ---
    def detect_pinch_zoom(self, hand_landmarks):
        if not hand_landmarks:
            self.initial_pinch_distance = None
            return None

        thumb_tip = hand_landmarks.landmark[4]
        index_tip = hand_landmarks.landmark[8]

        current_distance = self.euclidean_distance(thumb_tip, index_tip)

        if self.initial_pinch_distance is None:
            if current_distance < 0.1:
                self.initial_pinch_distance = current_distance
                return "start"
        else:
            if current_distance - self.initial_pinch_distance > self.zoom_sensitivity:
                self.initial_pinch_distance = current_distance
                return "zoom_in"
            elif self.initial_pinch_distance - current_distance > self.zoom_sensitivity:
                self.initial_pinch_distance = current_distance
                return "zoom_out"
            elif abs(current_distance - self.initial_pinch_distance) < self.zoom_sensitivity / 2:
                return "maintaining"
            else:
                self.initial_pinch_distance = None
                return None
        return None

    def start(self):
        while True:
            ret, frame = self.cam.read()
            if not ret:
                print("Error: Failed to grab frame.")
                break

            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            results_face_mesh = self.face_mesh.process(rgb_frame)
            results_hands = self.hands.process(rgb_frame)

            image = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2BGR)

            # --- Mouth control removed ---

            # --- Hand Landmarks (Index Finger and Thumb Control) ---
            if results_hands.multi_hand_landmarks:
                for hand_landmarks in results_hands.multi_hand_landmarks:
                    self.mp_drawing.draw_landmarks(image, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)

                    # Index finger down → previous short
                    if self.detect_index_finger_down_movement(hand_landmarks) and (time.time() - self.last_action) > self.cooldown:
                        pyautogui.press('up')
                        print("Index Finger Down: Previous Short")
                        self.last_action = time.time()

                    # Thumb down → next short
                    if self.detect_thumb_down_movement(hand_landmarks) and (time.time() - self.last_action) > self.cooldown:
                        pyautogui.press('down')
                        print("Thumb Down: Next Short")
                        self.last_action = time.time()

            cv2.imshow('Hand Control for YouTube Shorts', image)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cam.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    face_control = FaceControlShorts()
    face_control.start()
