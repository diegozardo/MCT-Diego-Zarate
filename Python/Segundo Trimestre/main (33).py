import datetime

dia= datetime.date.today()

w=dia.weekday()+1

if(w==0):
  print("feliz domingo")

elif(w==1):
  print("wuhu, es lunes")


elif(w==2):
  print("wuhu, es martes")

elif(w==3):
  print("wuhu, es miercoles")


elif(w==4):
  print("wuhu, es jueves")


elif(w==5):
  print("wuhu, es viernes")


else:
  print("yahoo, es sabado")