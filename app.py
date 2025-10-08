import cv2
import mediapipe as mp
import pyautogui
import math
import numpy as np
import time

# Optional imports with error handling
try:
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
    from comtypes import CLSCTX_ALL
    volume_available = True
except ImportError:
    print(" pycaw not installed. Volume control disabled.")
    volume_available = False

# Safety settings for pyautogui
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.1

# Initialize mediapipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)
mp_drawing = mp.solutions.drawing_utils

# Screen size
screen_w, screen_h = pyautogui.size()
print(f"Screen resolution: {screen_w}x{screen_h}")


# Initialize camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ Cannot open camera")
    exit()

print("✅ Camera initialized")

# Timing variables
last_screenshot = 0
last_media = 0
last_click = 0
last_right_click = 0

def is_palm_open(coords):
    """Check if all fingers are stretched"""
    try:
        # Check if fingertips are above their respective joints
        return (coords[8][1] < coords[6][1] and  # Index finger
                coords[12][1] < coords[10][1] and # Middle finger
                coords[16][1] < coords[14][1] and # Ring finger
                coords[20][1] < coords[18][1])    # Pinky
    except IndexError:
        return False

def is_thumbs_up(coords):
    """Check if thumb is up and other fingers down"""
    try:
        return (coords[4][1] < coords[3][1] and    # Thumb up
                coords[8][1] > coords[6][1] and    # Index down
                coords[12][1] > coords[10][1])     # Middle down
    except IndexError:
        return False


print("🎮 Hand Control System Started")
print("Controls:")
print("- Move index finger to control mouse")
print("- Index + middle finger close = Left click")
print("- Thumb + index finger close = Right click")
print("- Open palm = Screenshot")
print("- Press ESC to exit")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to read from camera")
        break
    
    # Flip frame horizontally for mirror effect
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    
    # Convert BGR to RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand in results.multi_hand_landmarks:
            # Draw hand landmarks
            mp_drawing.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

            # Get landmark coordinates
            landmarks = hand.landmark
            coords = [(int(lm.x * w), int(lm.y * h)) for lm in landmarks]

            # Mouse control with index finger tip
            if len(coords) > 8:
                index_x, index_y = coords[8]
                # Map camera coordinates to screen coordinates
                mouse_x = int(np.interp(index_x, [0, w], [0, screen_w]))
                mouse_y = int(np.interp(index_y, [0, h], [0, screen_h]))
                
                try:
                    pyautogui.moveTo(mouse_x, mouse_y, duration=0.1)
                except pyautogui.FailSafeException:
                    print("PyAutoGUI fail-safe triggered")
                    break

                # Left click (index + middle finger close together)
                if len(coords) > 12:
                    ix, iy = coords[8]  # Index tip
                    mx, my = coords[12] # Middle tip
                    click_dist = math.hypot(mx - ix, my - iy)
                    
                    if click_dist < 30 and time.time() - last_click > 0.5:
                        pyautogui.click()
                        print("🖱️ Left click")
                        last_click = time.time()

                # Right click (thumb + index finger close)
                if len(coords) > 4:
                    tx, ty = coords[4]  # Thumb tip
                    right_click_dist = math.hypot(tx - ix, ty - iy)
                    
                    if right_click_dist < 30 and time.time() - last_right_click > 0.5:
                        pyautogui.rightClick()
                        print("🖱️ Right click")
                        last_right_click = time.time()

                    # # Volume control (thumb-index distance)
                    # vol_dist = math.hypot(tx - ix, ty - iy)
                    # if vol_dist > 30:  # Avoid conflict with right click
                    #     vol_level = np.interp(vol_dist, [40, 200], [-65.25, 0])
                    #     safe_set_volume(vol_level)

                # # Brightness control (index-middle distance)
                # if len(coords) > 12:
                #     bright_dist = math.hypot(mx - ix, my - iy)
                #     if bright_dist > 30:  # Avoid conflict with left click
                #         brightness = np.interp(bright_dist, [40, 200], [10, 100])
                #         safe_set_brightness(brightness)


                # # App switch (thumb + pinky close)
                # if len(coords) > 20:
                #     px, py = coords[20]  # Pinky tip
                #     if math.hypot(px - tx, py - ty) < 40:
                #         pyautogui.hotkey("alt", "tab")
                #         print("🔄 App switch")
                #         time.sleep(0.5)  # Prevent spam

                # Screenshot (open palm gesture)
                if is_palm_open(coords) and time.time() - last_screenshot > 3:
                    try:
                        screenshot = pyautogui.screenshot()
                        screenshot.save("screenshot.png")
                        print("📸 Screenshot saved")
                        last_screenshot = time.time()
                    except Exception as e:
                        print(f"Screenshot error: {e}")

                # # Media control (thumbs up gesture)
                # if is_thumbs_up(coords) and time.time() - last_media > 2:
                #     pyautogui.press("playpause")
                #     print("🎵 Play/Pause toggled")
                #     last_media = time.time()

                # Zoom control (pinch/spread gesture)
                # if len(coords) > 4 and time.time() - last_zoom > 1:
                #     zoom_dist = math.hypot(tx - ix, ty - iy)
                #     if zoom_dist < 30:  # Very close = zoom out
                #         pyautogui.hotkey("ctrl", "-")
                #         print("🔍 Zoom out")
                #         last_zoom = time.time()
                #     elif zoom_dist > 150:  # Far apart = zoom in
                #         pyautogui.hotkey("ctrl", "+")
                #         print("🔍 Zoom in")
                #         last_zoom = time.time()

    # Add status text to frame
    cv2.putText(frame, "Hand Control System - Press ESC to exit", 
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Show frame
    cv2.imshow("Hand Control System", frame)

    # Exit on ESC key
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC key
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
print("🛑 Hand Control System stopped")