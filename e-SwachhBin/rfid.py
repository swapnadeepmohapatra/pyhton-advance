from time import sleep
import sys
from mfrc522 import SimpleMFRC522
import pyrebase
from datetime import datetime

reader = SimpleMFRC522()

config = {
    "apiKey": "AIzaSyBG510i9aGXHr7s3B_4JRIlqFj_CCYRc_8",
    "authDomain": "iottest-89b28.firebaseapp.com",
    "databaseURL": "https://iottest-89b28.firebaseio.com",
    "storageBucket": "iottest-89b28.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

try:
    while True:
        print("Hold a tag near the reader")
        id, text = reader.read()
        cardNo = id
        timeNow = datetime.now().strftime("%H:%M:%S")
        print("ID: ", cardNo)
        db.child("rfid_cards").child(cardNo).push({str(timeNow)})
        print('Updated')
        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise
