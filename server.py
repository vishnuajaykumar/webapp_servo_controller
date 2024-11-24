#modified by Vishnu Ajay
#10/23/2023
#revC

# Import necessary libraries
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import serial
import time
from threading import Thread

# Arduino communication
ser = serial.Serial('/dev/ttyUSB0', 9600)  
def read_from_port(ser):
    while True:
        reading = ser.readline().decode().strip()  
        print(reading)  
        socketio.emit('server-msg', reading)  

thread = Thread(target=read_from_port, args=[ser]) 
thread.start()  # Start the thread

# Flask Webserver
app = Flask(__name__)  
app.config['SECRET_KEY'] = 'secret!'  
socketio = SocketIO(app)  

@app.route('/')
def index():
    return render_template('index.html')  

@socketio.on('connect')
def test_connect():
    print('Client connected')  
    emit('my response', {'data': 'Connected'})  

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')  

# Handle the LED messages
@socketio.on('servoON')
def servo_on():
    print("Servo to 90 degree!")  
    ser.write(b'H') 

@socketio.on('servoOFF')
def servo_off():
    print("Servo to noraml state")  
    ser.write(b'L')  

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)  
    socketio.run(app)  # 
