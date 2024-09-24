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
ser = serial.Serial('/dev/ttyUSB0', 9600)  # Set up a serial connection with Arduino
def read_from_port(ser):
    while True:
        reading = ser.readline().decode().strip()  # Read data from Arduino
        print(reading)  # Print the received data to the console
        socketio.emit('server-msg', reading)  # Emit the received data to the client

thread = Thread(target=read_from_port, args=[ser])  # Create a thread for reading data from Arduino
thread.start()  # Start the thread

# Flask Webserver
app = Flask(__name__)  # Create a Flask web application
app.config['SECRET_KEY'] = 'secret!'  # Set a secret key for security purposes
socketio = SocketIO(app)  # Create a SocketIO object associated with the Flask app

@app.route('/')
def index():
    return render_template('index.html')  # Render the HTML template

@socketio.on('connect')
def test_connect():
    print('Client connected')  # Print a message when a client connects
    emit('my response', {'data': 'Connected'})  # Send a custom event and data to the client 

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')  # Print a message when a client disconnects

# Handle the LED messages
@socketio.on('servoON')
def servo_on():
    print("Servo to 90 degree!")  # Print a message when the "servoON" event is received
    ser.write(b'H')  # Send a command to Arduino 

@socketio.on('servoOFF')
def servo_off():
    print("Servo to noraml state")  # Print a message when the "servoOFF" event is received
    ser.write(b'L')  # Send a command to Arduino 

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)  # Run the Flask application on the local machine
    socketio.run(app)  # Run the SocketIO server
