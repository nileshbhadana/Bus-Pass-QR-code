import qrcode,cv2,random
from datetime import datetime

def gen_qr():
    userid="BPU"+str(random.randint(1000000,9999999))
    print(userid)
    start=input("Enter the Start Date:(mm/dd/yyyy)")
    end=input("Enter the End Date:(mm/dd/yyyy)")
    date_format = "%m/%d/%Y"
    a = datetime.strptime(start, date_format)
    b = datetime.strptime(end, date_format)
    fare=int(str(b-a).split(" ")[0])*50
    print("\n\nYour total fare will be Rs. ",fare)
    #generating qr code
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,)
    qr.add_data(start+" "+end+" "+userid)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("image.jpg")
    img=cv2.imread("image.jpg")
    cv2.putText(img,"Print this",(0,18),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)
    cv2.imshow('win',img)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyWindow('win')

while True:
    choice=input("Generate new qr code?(Y/N):")
    if choice=='Y' or choice=='y':
        gen_qr()
    elif choice=='N' or choice=='n':
        break
    else:
        print("Wrong Input..")

