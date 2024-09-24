# Servo Control with Flask and Micro Controller

This project demonstrates a simple web interface built with Flask to control a servo motor connected to an Adafruit Metro Mini (or similar microcontroller) via a serial connection. The interface allows you to remotely toggle the servo on and off, and also provides visual feedback on the webpage based on the servo's state.

## Features
- **Web Interface**: A sleek and interactive webpage using HTML, CSS, and JavaScript.
- **Flask Backend**: Flask manages the communication between the web interface and the servo motor.
- **Socket.IO**: Real-time, bidirectional communication for instant updates when toggling the servo.
- **Servo Control**: Control a servo motor by simply pressing a button on the webpage.

## How It Works

1. **Flask Server**: The Flask server acts as the intermediary between the front-end (webpage) and the Metro Mini (servo controller). It listens for commands from the web interface and sends instructions to the Metro Mini.
2. **Metro Mini**: The Metro Mini receives commands via serial and controls the servo accordingly.
3. **Real-Time Feedback**: Using Socket.IO, the front-end is updated in real-time, showing the current state of the servo.

### Tech Stack
- **Flask** - Python web framework
- **Socket.IO** - Real-time communication between the server and the client
- **HTML/CSS/JavaScript** - Front-end for the web interface
- **Adafruit Metro Mini** - Microcontroller for controlling the servo
- **Servo Motor** - Motor connected to the Metro Mini

## Setup

### Prerequisites
- Python 3.x
- Flask
- Socket.IO (both Python and JavaScript versions)
- Adafruit Metro Mini or any microcontroller with a servo motor
- Servo motor

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/servo-flask-control.git
    cd servo-flask-control
    ```

2. **Install the dependencies**:
    ```bash
    pip install flask flask-socketio
    ```

3. **Upload the Arduino Code**:
   Ensure the Metro Mini is connected to your computer and upload the `helloYou.ino` sketch located in the `arduino_code/` folder. This script allows the microcontroller to read serial input from the Flask app.

4. **Run the Flask server**:
    ```bash
    python server.py
    ```

5. **Access the Web Interface**:
    Open a browser and navigate to `http://localhost:5000`. You will see the servo control buttons on the page.

### Usage
- **Servo ON**: Press the "Servo ON" button to turn the servo to the ON position.
- **Servo OFF**: Press the "Servo OFF" button to return the servo to the OFF position.
- The background color of the webpage will change based on the state of the servo.

### File Structure

```bash
├── arduino_code/
│   └── servo_control.ino          # Arduino sketch for Metro Mini
├── static/
│   ├── client.js             # Client-side JavaScript for handling socket communication
│   ├── socket.io.js          # Socket.IO client library
├── templates/
│   └── index.html            # Web interface for controlling the servo
├── server.py                 # Flask server managing the communication
└── README.md                 # Project documentation
