import cv2

"path是图片路径，执行后，会在同一目录下生成11张依次旋转30度的图片"
def spin(path):
    retval=cv2.imread(path)
    print(retval)
    he,we=retval.shape[:2]
    for x in range(2,13):
        M=cv2.getRotationMatrix2D(center=(we/2,he/2),angle=x*30,scale=1)
        M=cv2.warpAffine(retval,M,(we,he))
        new_path=path[:-4]+str(x).zfill(4)+'.jpg'
        #print(new_path)
        cv2.imwrite(new_path,M)
"path是图片路径，执行后会在同一目录下生成五张亮度依次递增的图片"
def light(path):
    retval=cv2.imread(path)
    img_hsv = cv2.cvtColor(retval, cv2.COLOR_BGR2HSV)
    darker_hsv = img_hsv.copy()
    for y in range(1,6):
        darker_hsv[:, :, 2] = darker_hsv[:, :, 2]+2*y
        darker_img = cv2.cvtColor(darker_hsv, cv2.COLOR_HSV2BGR)
        new_path=path[:-3]+'-light+'+str(y)+'.jpg'
        cv2.imwrite(new_path, darker_img)

if __name__ == '__main__':
    path = 'negative_image/S.jpg'
    spin(path)
    #light(path)
