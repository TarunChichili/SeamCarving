import cv2

from exe import PATH
from .seamCarve import *


def columnSample(iterPeriod):
    img = cv2.normalize(cv2.imread(PATH), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    while True:
        for i in range(iterPeriod): img = carve_column(img)
        cv2.imshow("sample", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def rowSample(iterPeriod):
    img = cv2.normalize(cv2.imread(PATH), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    while True:
        for i in range(iterPeriod): img = carve_row(img)
        cv2.imshow("sample", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def consecutiveCarve(iterPeriod):
    img = cv2.normalize(cv2.imread(PATH), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    while True:
        for i in range(iterPeriod):
            img = carve_column(carve_row(img))
        cv2.imshow("sample", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

