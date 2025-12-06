import cgi 
from base64 import b64decode, encode
import pint 
import face_recognition
formdata = cgi.fieldstorage('img')
face_match=0
image=formdata.getvalue("current_image")
email=formdata.getvalue("email")
data_uri=image
header, encoded = data_uri.split(",",1)
data=b64decode(encoded)
with open("image.png", "wb")as f:
    f.write(data)
got_image = face_recognition.load_image_file("image.png")
existing_image = face_recognition.load_image_file("student/"+email+".jpg")
got_image_facialfeature = face_recognition.face_encodings(got_image)(0)
existing_image_facialfeatures = face_recognition.face_encodings(existing_image)(0)
results=face_recognition.compare_faces([existing_image_facialfeatures], got_image_facialfeature)
if(results[0]):
    face_match=1
else:
    face_match=0
print("content-type: text/html")
pint()
if(face_match==1):
    print("<scripts>alert('welcome",email,"')</scripts>")
else:
    print("<script>alert('face not recognized')</scripts>")