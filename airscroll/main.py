import cv2
import mediapipe as mp
import pyautogui
import time
import ctypes

from airscroll.gestures import is_thumbs_up, is_open_palm
from airscroll.screenshot import take_screenshot
import airscroll.config as cfg


def setup_dpi():
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(2)
    except:
        pass


def run():
    setup_dpi()

    mp_hands = mp.solutions.hands
    mp_draw = mp.solutions.drawing_utils

    hands = mp_hands.Hands(
        max_num_hands=cfg.MAX_HANDS,
        min_detection_confidence=cfg.DETECTION_CONFIDENCE,
        min_tracking_confidence=cfg.TRACKING_CONFIDENCE
    )

    cap = cv2.VideoCapture(0)

    neutral_y = None
    scroll_enabled = False
    smooth_offset = 0
    scroll_speed = 0
    last_thumb_toggle = 0
    last_screenshot_time = 0
    freeze_scroll_until = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(rgb)
        current_time = time.time()
        scroll_speed = 0

        if results.multi_hand_landmarks:
            hand = results.multi_hand_landmarks[0]

            # 👍 Toggle Scroll
            if is_thumbs_up(hand) and current_time - last_thumb_toggle > cfg.THUMB_TOGGLE_COOLDOWN:
                scroll_enabled = not scroll_enabled
                last_thumb_toggle = current_time

            # ✋ Screenshot
            if is_open_palm(hand) and current_time - last_screenshot_time > cfg.SCREENSHOT_COOLDOWN:
                take_screenshot()
                last_screenshot_time = current_time
                freeze_scroll_until = current_time + cfg.FREEZE_DURATION

            # Index tracking
            index_tip = hand.landmark[8]
            x = int(index_tip.x * w)
            y = int(index_tip.y * h)

            cv2.circle(frame, (x, y), 8, (0, 255, 0), -1)

            # Pinch
            thumb_tip = hand.landmark[4]
            tx = int(thumb_tip.x * w)
            ty = int(thumb_tip.y * h)

            pinch_distance = ((x - tx) ** 2 + (y - ty) ** 2) ** 0.5

            if pinch_distance < cfg.PINCH_THRESHOLD:
                neutral_y = y

            # Scroll Logic
            if scroll_enabled and neutral_y is not None and current_time > freeze_scroll_until:
                offset = neutral_y - y

                if abs(offset) > cfg.DEADZONE:
                    smooth_offset = (
                        smooth_offset * cfg.SCROLL_SMOOTHING +
                        offset * (1 - cfg.SCROLL_SMOOTHING)
                    )
                    scroll_speed = int(smooth_offset * cfg.SCROLL_MULTIPLIER)
                    pyautogui.scroll(scroll_speed)

            mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

        # ================= UI Overlay =================

        if neutral_y is not None:
            cv2.line(frame, (0, neutral_y), (w, neutral_y), (255, 0, 0), 2)

        # Title
        cv2.putText(frame,
                    "AirScroll Pro",
                    (w // 2 - 150, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 255),
                    2)

        # Speed
        cv2.putText(frame,
                    f"Speed: {scroll_speed}",
                    (10, 80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (255, 255, 0),
                    2)

        # Status
        status = "ON" if scroll_enabled else "OFF"
        color = (0, 255, 0) if scroll_enabled else (0, 0, 255)

        cv2.putText(frame,
                    f"Scroll: {status}",
                    (10, 110),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    color,
                    2)

        cv2.imshow("AirScroll", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()
