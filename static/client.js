var socket = io();

// send out LedOn message over socket
function servoON() {
    socket.emit('servoON');
	console.log('servoON');
}

// send out ledOFF message over socket
function servoOFF() {
    socket.emit('servoOFF');
	console.log('servoOFF');

}

// read the data from the message that the server sent and change the
// background of the webpage based on the data in the message
socket.on('server-msg', function(msg) {
    console.log('msg:', msg);
    switch(msg) {
        case 'light':
            document.body.style.backgroundColor = 'white';
            console.log('white')
            break;
        case 'dark':
            document.body.style.backgroundColor = 'black';
            console.log('black');
            break;
    }
});
