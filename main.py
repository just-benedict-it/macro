import pyautogui as pag
import mss, cv2
import numpy as np
import time
import random
# df
def compute_icon_type(img):
    mean = np.mean(img, axis=(0,1))
    result = None

    if 230>mean[0]>220 and 230>mean[1]>220 and 230>mean[2]>220:
        result = 'List'
    if 210>mean[0]>200 and 210>mean[1]>200 and 210>mean[2]>200:
        result = 'List_Opened'
    if 110>mean[0]>100 and 100>mean[1]>90 and 100>mean[2]>90:
        result = 'Refresh'

    if 237>mean[0]>235 and 237>mean[1]>235 and 237>mean[2]>235:
        result = 'Not ready'
    if 235>mean[0]>233 and 235>mean[1]>233 and 235>mean[2]>233:
        result = 'Page Changed'

    return result

def click(coords):
    pag.moveTo(x=random.uniform(coords[0][0], coords[1][0]), y=random.uniform(coords[0][1], coords[1][1]), duration = random.uniform(0.0, 0.04))
    pag.mouseDown()
    time.sleep(random.uniform(0.0, 0.03))
    pag.mouseUp()
    time.sleep(random.uniform(0.0, 0.03))


pag.Pause = random.uniform(0.02, 0.05)

# icon_position
list_icon_pos = {'left':155, 'top':660, 'width':66, 'height':21}
refresh_icon_pos = {'left':273, 'top':715, 'width':93, 'height':24}
changed_icon_pos = {'left':266, 'top':192, 'width':17, 'height':12}



# button_position
list_button = [[170, 669],[180, 675]]
refresh_button = [[300,720],[350,730]]
first_list_button = [[280,199],[283,203]]
dangil_button = [[267, 753], [315, 765]]
ok_button = [[290, 460], [305, 465]]


check = True

try:
    time.sleep(5)
    while True:
        with mss.mss() as sct:
            click(refresh_button)
            list_img = np.array(sct.grab(list_icon_pos))[:,:,:3]
            refresh_icon_img = np.array(sct.grab(refresh_icon_pos))[:,:,:3]

            list_icon = compute_icon_type(list_img)
            refresh_icon = compute_icon_type(refresh_icon_img)
            

            if list_icon == 'List':
                continue

            elif list_icon == 'List_Opened':
                print("Vaccine Opened!!!")
                click(list_button)
         
                while True:
                    first_list_img = np.array(sct.grab(changed_icon_pos))[:,:,:3]
                    first_list_icon = compute_icon_type(first_list_img)
              
                    click(first_list_button)
                    click(first_list_button)
                    click(first_list_button)
                    click(dangil_button)
                    click(dangil_button)
                    click(ok_button)
                    click(ok_button)
                    click(ok_button)
                    click(ok_button)
                    click(ok_button)
                    check = False
                    break
                else:
                    continue
                
                if check == False:
                    break
        

except KeyboardInterrupt:
    pass


# while True:
#     with mss.mss() as sct:
#         img = np.array(sct.grab(list_icon_pos))[:,:,:3]
#         compute_icon_type(img)

# while True:
#     x, y = pag.position()
#     position_str = 'X: '+str(x) +'   Y: '+str(y)
#     print(position_str)

# cv2.imshow('terminal_img', list_img)
# cv2.imshow('refresh_icon_pos', refresh_icon_img)

# cv2.waitKey(3)