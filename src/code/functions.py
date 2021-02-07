import cv2
import numpy as np


def rescale_frame(frame, scale=0.5):
    """
    rescale un frame de una imagen
    Parameters
    ----------
    frame : object
        cv2.imread().
    scale : TYPE, optional
        DESCRIPTION. The default is 0.5.
    Returns
    -------
    object: frame
        image escalada.
    """
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)


def read_video(path):
    """
    Leer un video solamente
    Parameters
    ----------
    path : TYPE
        DESCRIPTION.
    Returns
    -------
    None.
    """
    cap = cv2.VideoCapture(path)
    while True:
        success, img = cap.read()
        cv2.imshow("video", img)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


def translate(img, x, y):
    """
    translations: mover imagen a la derecha o izquierda
    Parameters
    ----------
    img : TYPE
        DESCRIPTION.
    x : TYPE
        DESCRIPTION.
    y : TYPE
        DESCRIPTION.
    Returns
    -------
    TYPE
        DESCRIPTION.
    """
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, transMat, dimensions)


def rotate(img, angle, rotPoint=None):
    """
    Rotar una imagen
    Parameters
    ----------
    img : TYPE
        DESCRIPTION.
    angle : TYPE
        DESCRIPTION.
    rotPoint : TYPE, optional
        DESCRIPTION. The default is None.
    Returns
    -------
    None.
    """
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (height/2, width/2)
    rotMat = cv2.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv2.warpAffine(img, rotMat, dimensions)
