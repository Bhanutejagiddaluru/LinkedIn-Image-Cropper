import cv2

# ====== Settings ======
TARGET_W, TARGET_H = 1200, 627               # LinkedIn target
RATIO = TARGET_W / TARGET_H                  # 1.913...
PREVIEW_SCALE = 0.5                          # start with half-size box
SAVE_BOX_PATH = "linkedin_fixed_box.jpg"
SAVE_BAND_PATH = "linkedin_vertical_band.jpg"

# ====== Load ======
img = cv2.imread("input.jpg")
if img is None:
    raise FileNotFoundError("Couldn't read input.jpg")
H, W = img.shape[:2]
clone = img.copy()

# ====== Initial fixed box (movable, resizable but ratio-locked) ======
box_w = int(TARGET_W * PREVIEW_SCALE)
box_h = int(box_w / RATIO)
x = max(0, (W - box_w) // 2)
y = max(0, (H - box_h) // 2)

dragging = False
offset_x = offset_y = 0

def clamp_box():
    global x, y, box_w, box_h
    x = max(0, min(x, W - box_w))
    y = max(0, min(y, H - box_h))

def mouse_cb(event, mx, my, flags, param):
    global dragging, x, y, offset_x, offset_y
    if event == cv2.EVENT_LBUTTONDOWN:
        dragging = True
        offset_x = mx - x
        offset_y = my - y
    elif event == cv2.EVENT_MOUSEMOVE and dragging:
        x = mx - offset_x
        y = my - offset_y
        clamp_box()
    elif event == cv2.EVENT_LBUTTONUP:
        dragging = False

cv2.namedWindow("Tool")
cv2.setMouseCallback("Tool", mouse_cb)

print("[ Instructions ]")
print(" - Drag mouse: move fixed-ratio box")
print(" - '+' / '-':  grow / shrink box (ratio locked)")
print(" - 'c':        save FIXED BOX crop ->", SAVE_BOX_PATH)
print(" - 'b':        save VERTICAL BAND (between the two lines) ->", SAVE_BAND_PATH)
print(" - 'r':        reset box size/position")
print(" - 'q':        quit")

while True:
    frame = clone.copy()

    # draw box
    cv2.rectangle(frame, (x, y), (x + box_w, y + box_h), (0, 255, 0), 2)

    # draw the two vertical guides aligned to box sides (full image height)
    left_x = x
    right_x = x + box_w
    cv2.line(frame, (left_x, 0), (left_x, H), (0, 200, 255), 1)
    cv2.line(frame, (right_x, 0), (right_x, H), (0, 200, 255), 1)

    # small labels
    cv2.putText(frame, "C=Save Box  B=Save Band  +/-=Resize  R=Reset  Q=Quit",
                (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (30, 30, 30), 2, cv2.LINE_AA)
    cv2.imshow("Tool", frame)

    key = cv2.waitKey(1) & 0xFF

    if key in (ord('+'), ord('=')):  # grow
        new_w = int(box_w * 1.05)
        new_h = int(new_w / RATIO)
        if new_w <= W and new_h <= H:
            # expand from center
            cx, cy = x + box_w // 2, y + box_h // 2
            box_w, box_h = new_w, new_h
            x, y = cx - box_w // 2, cy - box_h // 2
            clamp_box()

    elif key == ord('-'):  # shrink
        new_w = max(50, int(box_w / 1.05))
        new_h = int(new_w / RATIO)
        if new_w >= 20 and new_h >= 20:
            cx, cy = x + box_w // 2, y + box_h // 2
            box_w, box_h = new_w, new_h
            x, y = cx - box_w // 2, cy - box_h // 2
            clamp_box()

    elif key == ord('r'):  # reset
        box_w = int(TARGET_W * PREVIEW_SCALE)
        box_h = int(box_w / RATIO)
        x = (W - box_w) // 2
        y = (H - box_h) // 2
        clamp_box()

    elif key == ord('c'):  # save fixed-box crop
        crop = clone[y:y + box_h, x:x + box_w]
        crop = cv2.resize(crop, (TARGET_W, TARGET_H), interpolation=cv2.INTER_AREA)
        cv2.imwrite(SAVE_BOX_PATH, crop)
        cv2.imshow("Fixed Box", crop)
        print("Saved:", SAVE_BOX_PATH)

    elif key == ord('b'):  # save vertical band crop (full height between the two lines)
        band = clone[:, left_x:right_x]  # full height, between lines
        # resize to LinkedIn size for consistency (no padding)
        band = cv2.resize(band, (TARGET_W, TARGET_H), interpolation=cv2.INTER_AREA)
        cv2.imwrite(SAVE_BAND_PATH, band)
        cv2.imshow("Vertical Band", band)
        print("Saved:", SAVE_BAND_PATH)

    elif key == ord('q'):
        break

cv2.destroyAllWindows()
