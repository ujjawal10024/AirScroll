import time
import os
import pyautogui
import mss
import mss.tools


def take_screenshot(output_folder="screenshots"):
    os.makedirs(output_folder, exist_ok=True)

    mouse_x, mouse_y = pyautogui.position()

    with mss.mss() as sct:
        for monitor in sct.monitors[1:]:   # <-- monitors correct
            if (
                monitor["left"] <= mouse_x <= monitor["left"] + monitor["width"] and
                monitor["top"] <= mouse_y <= monitor["top"] + monitor["height"]
            ):
                img = sct.grab(monitor)

                filename = f"{output_folder}/airscroll_{int(time.time()*1000)}.png"
                mss.tools.to_png(img.rgb, img.size, output=filename)

                return filename

    return None
