# SkyKeys

> A virtual MIDI keyboard web application for "Sky: Children of the Light"

![SkyKeys Interface](/ss/screen1.png)

## Overview

SkyKeys let you play instrument using your phone while your game is runnning on PC. Using a Flask server and WebSocket communication, it enables wireless control of in-game musical features through your phone's touchscreen.

## Features

- Real-time MIDI input over local network
- Exact in-game Instrument layout
- Low latency response
- Browser-based client (no phone app installation needed)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/kozuedoingregression/skykeys.git
cd skykeys
```

2. Install dependencies
```bash
pip install flask flask-socketio keyboard
```

3. Start the server:
```bash
python app.py
```

4. Connect you phone to the same local network (you can open you PC's mobile hotspot and connect you phone to it.)

5. On your phone, navigate to the displayed IP address (e.g., `http://192.168.1.100:3000`)

## Usage

1. Run the Flask server on your PC
2. Connect your phone to the same local network
3. Open the web interface on your phone
4. Start playing using the virtual keyboard

## Configuration

Customize the app by modifying:
- `templates/index.html` - Keyboard layout and UI
- `app.py` - MIDI mapping and server settings

## Contributing

1. Give a Star 🌟
2. Fork the repository
3. Create a feature branch
4. Submit a pull request

## Acknowledgments

Thanks to the Sky: Children of the Light community and the developers of Flask and Flask-SocketIO.
