import cv2

# LinkedIn target crop size
TARGET_WIDTH, TARGET_HEIGHT = 1200, 627

# Load image
img = cv2.imread("input.jpg")
clone = img.copy()
h, w = img.shape[:2]

# Start box in center
x = w//2 - TARGET_WIDTH//4
y = h//2 - TARGET_HEIGHT//4
box_w, box_h = TARGET_WIDTH//2, TARGET_HEIGHT//2  # scale down for preview window

dragging = False

def mouse_drag(event, mx, my, flags, param):
    global x, y, dragging

    if event == cv2.EVENT_LBUTTONDOWN:
        dragging = True

    elif event == cv2.EVENT_MOUSEMOVE and dragging:
        # Move box center to mouse while staying inside bounds
        x = max(0, min(mx - box_w//2, w - box_w))
        y = max(0, min(my - box_h//2, h - box_h))

    elif event == cv2.EVENT_LBUTTONUP:
        dragging = False

cv2.namedWindow("Crop Tool")
cv2.setMouseCallback("Crop Tool", mouse_drag)

print("👉 Drag the fixed box to desired area.")
print("   Press 'c' to crop & save, 'q' to quit.")

while True:
    preview = clone.copy()
    cv2.rectangle(preview, (x, y), (x+box_w, y+box_h), (0,255,0), 2)
    cv2.imshow("Crop Tool", preview)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("c"):
        roi = clone[y:y+box_h, x:x+box_w]
        roi = cv2.resize(roi, (TARGET_WIDTH, TARGET_HEIGHT), interpolation=cv2.INTER_AREA)
        cv2.imwrite("linkedin_fixed_crop.jpg", roi)
        cv2.imshow("Cropped", roi)
        print("✅ Saved as linkedin_fixed_crop.jpg")

    elif key == ord("q"):
        break

cv2.destroyAllWindows()
