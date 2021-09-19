# memanggil library
  from gpio import *
  from time import *

# untuk mendeklarasikan fungsi handleSensorData
  def handleSensorData():

# mendeklarasikan yang diinput dari sensor digitalRead
	value = digitalRead(0)
# Jika memiliki value 0 yang artinya tidak ada gerakan dari cursor makan garasi tidak terbuka dan lampu tidak menyala
	if value == 0:
		customWrite(2, '0')
		digitalWrite(1, LOW)
		print("Tidak ada gerakan")
# Dan bila ada gerakan dari cursor di dekat sensor gerak maka lampu dan garasi akan bernilai 1 
	else:
			customWrite(2, '1')
			digitalWrite(1, HIGH)
			print("Ada gerakan")
		
		
  def main():
	add_event_detect(0, handleSensorData)
	
	while True:
		delay(1000)

# jika fungsi main dijalankan maka akan menjalankan programnya
 if __name__ == "__main__":
	main()