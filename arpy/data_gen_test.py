import serial
import csv
import time
from twilio.rest import Client

account_sid = 'AC640e5efbb59fcb5ac0a4157057b2064b'
auth_token = '399170e4baba1135a76a4b738d11bd91'
twilio_phone_number = '+19512251178'
recipient_phone_number = ['+918090063403', '+919150465018', '+919884210662']

SERIAL_PORT = 'COM5'  

ser = serial.Serial(SERIAL_PORT, 9600) 

CSV_FILE = 'arduino_data.csv'

client = Client(account_sid, auth_token)
def send_sms(message, contact):
    client.messages.create(
        body=message,
        from_=twilio_phone_number,
        to=contact
    )

column_titles = ["Temperature", "Humidity", "Motion", "Light Intensity", "Fire State", "Air Quality", "Soil Moisture"]

def write_to_csv(data):
    with open(CSV_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

try:
    while True:
        if ser.in_waiting > 0:
            sensor_data = ser.readline().decode().strip().split(',') 
            with open('arduino_data.csv', mode ='r')as file:
                csvFile = csv.reader(file)
                if column_titles in csvFile:
                    continue
            if(sensor_data[2]==1):
                send_sms("Motion detected!", recipient_phone_number[0])    
            if(sensor_data[3]>0):
                light = sensor_data[3]
                if(light<10):   
                    send_sms("Dark, turning on the Lighting system!!", recipient_phone_number[2])
                elif(light<200):   
                    send_sms("Dim Brightness, turning on the Lighting system on Low Intensity!!", recipient_phone_number[2])
            if(sensor_data[4]==1):  
                send_sms("Fire Alert!!, turning on the Water Sprinklers!", recipient_phone_number[1])
            if(sensor_data[6]<=10):   
                send_sms("Low Soil Moisture Content, turning on the Water Sprinklers!", recipient_phone_number[2])
            if(sensor_data[7]):
                send_sms("Rack Unstable!, Take Immediate Maintainence", recipient_phone_number[2])
            write_to_csv(sensor_data)
        time.sleep(1)  
except KeyboardInterrupt:
    ser.close()

