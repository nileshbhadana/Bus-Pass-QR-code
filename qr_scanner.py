# import the necessary packages
from pyzbar import pyzbar
import cv2
from datetime import datetime
from datetime import date
date_format = "%m/%d/%Y"
 
 
def comparedate(start,end,now):
    a = datetime.strptime(start, date_format)
    b = datetime.strptime(now, date_format)
    c = datetime.strptime(end, date_format)
    delta1 = b - a
    delta2 = c - b
    delta3 = a - a
 
    if delta1.days >= delta3.days and delta2.days >= delta3.days:
        return True
    else:
        return False
 
now=date.today().strftime(date_format)

# camera starts
cam=cv2.VideoCapture(0)
cam.set(3,400)
# loop over the frames from the video stream
while cam.isOpened():
	# grab the frame from the threaded video stream and resize it to
	# have a maximum width of 400 pixels
    frame = cam.read()[1]

	# find the barcodes in the frame and decode each of the barcodes
    barcodes = pyzbar.decode(frame)

    	# loop over the detected barcodes
    for barcode in barcodes:
		# extract the bounding box location of the barcode and draw
		# the bounding box surrounding the barcode on the image
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 2)
        
        barcodeData = barcode.data.decode("utf-8")
        try:
            barcodeData=barcodeData.split(" ")
            start=barcodeData[0]
            end=barcodeData[1]
            if comparedate(start,end,now):
                cv2.putText(frame,"ALLOWED",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3,cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            else: 
                cv2.putText(frame,"PASS EXPIRED",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        except:
            cv2.putText(frame,"WRONG QR CODE..",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA)
    cv2.imshow("Barcode Scanner", frame)
    key = cv2.waitKey(1) & 0xFF
 
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
    	break

# close the output CSV file do a bit of cleanup
cv2.destroyAllWindows()
cam.release()
