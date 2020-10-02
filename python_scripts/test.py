import numpy as np
import cv2
import joblib


def detect_face(img, faceCascade):
    faces = faceCascade.detectMultiScale(img, scaleFactor=1.6, minNeighbors=5, minSize=(110, 110))
    #flags = cv2.CV_HAAR_SCALE_IMAGE
    return faces


def calc_hist(img):
    histogram = [0] * 3
    for j in range(3):#range RGB
        histr = cv2.calcHist([img], [j], None, [256], [0, 256])
        histr *= 255.0 / histr.max()
        histogram[j] = histr
    return np.array(histogram)

if __name__ == "__main__":    
    # # Load model
    clf = None
    try:
        clf = joblib.load('print-attack.pkl')
    except IOError as e:
        #print("Error loading model <"+args["name"]+">: {0}".format(e.strerror))
        exit(0)
    
    
