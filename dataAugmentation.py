'''
This is an example for data augmentation where
 input will be list of image paths (not image)
 output will be yield function with augmented image
'''
from glob import glob

import numpy as np
import cv2
np.random.seed(42)


def readImages(impaths):
    imgScaleFactors = [.5,.25,1.5,2]
    imgRotationFactors = [cv2.ROTATE_90_CLOCKWISE,cv2.ROTATE_90_COUNTERCLOCKWISE,cv2.ROTATE_180]
    for impath in impaths:
        img = cv2.imread(impath)
        if img is None:
            # img is empty then go for next image
            pass
        else:
            yield img
            # scale the image
            for imgScaleFactor in imgScaleFactors:
                rows, cols = img.shape[:2]
                rows, cols = rows * imgScaleFactor, cols * imgScaleFactor
                rows, cols = int(rows), int(cols)
                resizedImg = cv2.resize(img, (cols, rows))
                yield resizedImg
                # rotate image
                # M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
                # yield cv2.warpAffine(img, M, (cols, rows))
                for rotationFactor in imgRotationFactors:
                    resizedRotatedImg = cv2.rotate(resizedImg, rotationFactor)
                    yield resizedRotatedImg


def main(impaths):
    for img in readImages(impaths):
        cv2.namedWindow('img', 0)
        cv2.imshow('img', img)
        cv2.waitKey(0)


if __name__ == '__main__':
    impaths = glob(r'C:\Users\Public\Pictures\Sample Pictures\*.*')
    main(impaths)
