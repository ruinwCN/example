import cv2 as cv
import pymysql

if __name__ == '__main__':
    src = cv.imread('bg.jpg')
    text = "Hi PyCharm"
    file_name = 'pic/1.jpg'

    context = src.copy()
    cv.putText(context, text, (85, 246), cv.FONT_HERSHEY_DUPLEX, 0.65, (255, 255, 255), 1, cv.LINE_AA)
    cv.imwrite(file_name, context, [int(cv.IMWRITE_JPEG_QUALITY), 90])
