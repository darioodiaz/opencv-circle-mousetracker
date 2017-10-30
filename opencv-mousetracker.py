import numpy as np, win32api as win32, win32con, math, cv2

debug = False
useMorph = not debug

camera = cv2.VideoCapture(0)
oldFrame = None

#Verde
#lower = np.array([63, 41, 65])
#upper = np.array([82, 255, 255])

#Naranja
lower = np.array([0, 216, 65])
upper = np.array([72, 255, 202])

erodeStruct = cv2.getStructuringElement(cv2.MORPH_RECT, (4, 4));
dilateStruct = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9));

if debug:
    cv2.namedWindow("trackBars")

def show(title, src):
    cv2.imshow(title, src)

def onBarChange(x):
    pass

def changeLowerUpperValues():
    global lower, upper
    minH = cv2.getTrackbarPos("Min Hue", "trackBars")
    minS = cv2.getTrackbarPos("Min Sat", "trackBars")
    minV = cv2.getTrackbarPos("Min Val", "trackBars")

    maxH = cv2.getTrackbarPos("Max Hue", "trackBars")
    maxS = cv2.getTrackbarPos("Max Sat", "trackBars")
    maxV = cv2.getTrackbarPos("Max Val", "trackBars")

    lower = np.array([minH, minS, minV])
    upper = np.array([maxH, maxS, maxV])

def createHSVTrackBars():
    cv2.createTrackbar("Min Hue", "trackBars", 0, 180, onBarChange)
    cv2.createTrackbar("Min Sat", "trackBars", 0, 255, onBarChange)
    cv2.createTrackbar("Min Val", "trackBars", 0, 255, onBarChange)

    cv2.createTrackbar("Max Hue", "trackBars", 180, 180, onBarChange)
    cv2.createTrackbar("Max Sat", "trackBars", 255, 255, onBarChange)
    cv2.createTrackbar("Max Val", "trackBars", 255, 255, onBarChange)

def doMorph(img):
    cv2.erode(img, erodeStruct, img)
    cv2.erode(img, erodeStruct, img)

    cv2.dilate(img, dilateStruct, img)
    cv2.dilate(img, dilateStruct, img)

def draw(src, cnt, pos=-1):
    cv2.drawContours(src, cnt, pos, (0, 255, 0), 2)

def drawCircle(src, point):
    print "Drawing circle"
    cv2.circle(src, point, 20, (0, 255, 0), 2)

def moveMouse(point):
    win32.SetCursorPos(point)

def scrollMouse(point):
    print point
    if point > 0:
        for x in xrange(int(math.fabs(point))):
            win32.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, point * 5, 1, 0)
    else:
        for x in xrange(int(math.fabs(point))):
            win32.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, point * 5, -1, 0)

def render(src, mask):
    global oldFrame
    if debug:
        return

    if useMorph:
        doMorph(mask)

    contours = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contours, hier = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        cnt = contours[0]
        (x, y), radius = cv2.minEnclosingCircle(cnt)
        center = (int(x), int(y))
        radius = int(radius)
        if radius > 15:
            cv2.circle(src, center, radius, (0, 255, 0), 2)
            moveMouse(center)

def __init__():
    if debug:
        print("Debugging")
        createHSVTrackBars()

    while(True):
        _, frame = camera.read()
        frame = cv2.flip(frame, 1)
        frame = cv2.medianBlur(frame, 5)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower, upper)
        copyMask = mask.copy()

        render(frame, mask)

        show("Frame", frame)
        show("Mask", copyMask)

        if debug:
            changeLowerUpperValues()

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

__init__()