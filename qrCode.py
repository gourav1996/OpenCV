# import the necessary packages
from pyzbar import pyzbar
import cv2

def getQrCode(frame):

    frame = cv2.resize(frame,(1280,720))
    barcodes = pyzbar.decode(frame)

    for barcode in barcodes:
        (x,y,w,h) = barcode.rect
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        # print the barcode type and data to the terminal
        # print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))


    # # show the output image
    # cv2.imshow("Image", frame)

    return barcodeType, barcodeData

