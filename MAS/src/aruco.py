#!/usr/bin/env python

# Ros libraries
import rospy

import numpy as np
import cv2, PIL
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

import math
# %matplotlib nbagg


# plt.figure()
# plt.imshow(frame)
# plt.show()




# aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)

# fig = plt.figure()
# nx = 7
# ny = 2
# for i in range(1, nx*ny+1):
#     ax = fig.add_subplot(ny,nx, i)
#     img = aruco.drawMarker(aruco_dict,i, 700)
#     plt.imshow(img, cmap = mpl.cm.gray, interpolation = "nearest")
#     ax.axis("off")

# plt.savefig("images/markers.png")
# plt.show()

frame = cv2.imread("images/field_3.png")



lower_white = np.array([0,0,0], dtype=np.uint8)
upper_white = np.array([0,255,255], dtype=np.uint8)

hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, lower_white, upper_white)
frame= (cv2.bitwise_and(frame, frame, mask=mask))

# %%time
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
parameters =  aruco.DetectorParameters_create()
corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
frame_markers = aruco.drawDetectedMarkers(frame.copy(), corners, ids)

print(corners)
print(ids)


plt.figure()
plt.imshow(frame_markers)


mark_loc = pd.DataFrame(columns=['id','x','y'])

for i in range(len(ids)):
    c = corners[i][0]
    plt.plot([c[:, 0].mean()], [c[:, 1].mean()], "o", label = "id={0}".format(ids[i]))
    # print("id {} is at location {} , {} ".format(ids[i],[c[:, 0].mean()], [c[:, 1].mean()]))
    id_num = (ids[i])
    x = (c[:, 0].mean())
    y = (c[:, 1].mean())

    row_add = pd.DataFrame([[id_num,x,y]],columns=['id','x','y'])
    mark_loc = mark_loc.append(row_add)




print(mark_loc)

point1 = (mark_loc.loc[mark_loc['id'] == 1])
point2 = (mark_loc.loc[mark_loc['id'] == 2])

x1,y1,x2,y2 = point1.iloc[0,1] ,point1.iloc[0,2], point2.iloc[0,1] ,point2.iloc[0,2]

print(x1,y1,x2,y2)
dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(dist)
ratio = (5.0/dist)
print("ratio to decrease is: {}".format(ratio))

mark_loc_mod = mark_loc


mark_loc_mod['x'] = mark_loc_mod['x'] - x1
mark_loc_mod['y'] = mark_loc_mod['y'] - y1

mark_loc_mod['x'] = ratio * mark_loc_mod['x']
mark_loc_mod['y'] = -ratio * mark_loc_mod['y']

print(mark_loc_mod)





plt.legend()
plt.show()