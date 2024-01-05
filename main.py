import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)


# This function will check if the thumb is tucked across the palm.
def is_thumb_tucked(hand_landmarks, hand_type):
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_finger_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP]
    if hand_type == "Right":
        return thumb_tip.x > index_finger_mcp.x
    else:  # Left hand
        return thumb_tip.x < index_finger_mcp.x


# This function checks if the fingers are outstretched
def is_fingers_outstretched(hand_landmarks):
    # You will need to verify these indices and may need to adjust the logic
    for i in [
        mp_hands.HandLandmark.INDEX_FINGER_TIP,
        mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
        mp_hands.HandLandmark.RING_FINGER_TIP,
        mp_hands.HandLandmark.PINKY_TIP,
    ]:
        if hand_landmarks.landmark[i].y > hand_landmarks.landmark[i - 1].y:
            return False
    return True


# This function will check if the hand is in a fist with the thumb tucked in
def is_fist(hand_landmarks, hand_type):
    # Reusing your previous function, but you need to adjust it to check for thumb position
    if is_thumb_tucked(hand_landmarks, hand_type):
        for i in [
            mp_hands.HandLandmark.INDEX_FINGER_TIP,
            mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
            mp_hands.HandLandmark.RING_FINGER_TIP,
            mp_hands.HandLandmark.PINKY_TIP,
        ]:
            if hand_landmarks.landmark[i].y < hand_landmarks.landmark[i - 2].y:
                return False

        return True
    return False


# This variable will keep track of the last gesture detected
last_gesture = None

frame_counter = 0
max_frames_for_transition = 10  # Number of frames to allow for transition

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for idx, hand_landmarks in enumerate(result.multi_hand_landmarks):
            # Determine if it's a left or right hand
            handedness = result.multi_handedness[idx]
            hand_type = (
                "Right" if handedness.classification[0].label == "Right" else "Left"
            )

            if is_fingers_outstretched(hand_landmarks) and is_thumb_tucked(
                hand_landmarks, hand_type
            ):
                last_gesture = "Help part 1"
                frame_counter = 0
            elif last_gesture == "Help part 1" and is_fist(hand_landmarks, hand_type):
                print("Help sign detected!")
                last_gesture = None
                frame_counter = 0
            else:
                if last_gesture == "Help part 1":
                    frame_counter += 1
                    if frame_counter > max_frames_for_transition:
                        last_gesture = None
                        frame_counter = 0

            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Sign Language Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
