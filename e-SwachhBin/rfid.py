from time import sleep
import sys
from mfrc522 import SimpleMFRC522
import pyrebase
from datetime import datetime

reader = SimpleMFRC522()

config = {
  "apiKey": "apiKey",
  "authDomain": "projectId.firebaseapp.com",
  "databaseURL": "https://databaseName.firebaseio.com",
  "storageBucket": "projectId.appspot.com",
  "serviceAccount": "path/to/serviceAccountCredentials.json"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

try:
    while True:
        print("Hold a tag near the reader")
        id, text = reader.read()
        cardNo = id
        print("ID: ",cardNo)
        db.child("rfid_cards").child(cardNo).update({"name": "Mortiest Morty"})

        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise
