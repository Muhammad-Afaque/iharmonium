# i-harmonium

A web-based harmonium that uses your laptop's lid angle to control the bellows (air pressure). Press keys and push your laptop lid down to play!

## How It Works

- **Keys**: Press keyboard keys (A, W, S, E, D, F, T, G, Y, H, U, J, K) to play notes
- **Bellows**: Close your laptop lid (push down) to pump air and produce sound
- **Lid Angle Sensor**: Python backend reads your laptop's lid angle in real-time
- **WebSocket Connection**: Sends lid angle data to the HTML interface
- **Sound Generation**: Web Audio API creates harmonium-like tones

## Requirements

- Python 3.7+
- A web browser (Chrome, Firefox, Safari, Edge)
- **MacBook**: `websockets` and `pybooklid` libraries (for real lid sensor)
- **Windows/Linux**: `websockets` library (runs with simulated lid data for testing)

## Installation

1. **Clone this repository**:
   ```bash
   git clone <your-repo-url>
   cd iharmonium
   ```

2. **Set up a virtual environment** (recommended):
   ```bash
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   
   # Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install required Python packages**:
   ```bash
   pip install websockets
   
   # On MacBook (optional, for real lid sensor):
   pip install pybooklid
   ```

## Running the Harmonium

### Quick Start (2 terminals)

**Terminal 1 - Start the backend:**
```bash
python harmonium.py
```
You should see: `Bridge active! Waiting for your web app on port 8765...`

**Terminal 2 - Open the frontend:**
- Double-click `harmonium.html` in a file explorer, OR
- Open it in your browser directly: `open harmonium.html` (macOS) / `start harmonium.html` (Windows)

### Platform Notes

**MacBook (with lid sensor)**
- Automatic: Uses real lid angle from your MacBook's built-in sensor
- Sound responds to closing/opening your lid

**Windows/Linux (mock mode)**
- Automatic: Simulates lid opening/closing for testing
- Smooth angle oscillation from 0° (closed) to 180° (open)
- Perfect for development and demo purposes

### Playing Instructions

1. **Open the HTML file** in your browser
2. **Click anywhere on the page** once to enable audio (browser security)
3. **Press and hold keyboard keys** (A, W, S, E, D, F, T, G, Y, H, U, J, K) to play notes
4. **Close your laptop lid** (or watch the simulated angle) to pump bellows and create sound
5. The bellows meter shows air pressure - more air = louder sound

## Key Mapping

```
White Keys (Natural Notes):
A = C
S = D
D = E
F = F
G = G
H = A
J = B
K = C (octave)

Black Keys (Sharps):
W = C#
E = D#
T = F#
Y = G#
U = A#
```

## Tips

- The harder/faster you close the lid, the more air you pump
- Air slowly leaks out, just like a real harmonium
- Hold multiple keys simultaneously for chords
- The lid angle is displayed at the top of the interface

## Troubleshooting

**No sound?**
- Make sure you clicked on the page to activate audio
- Check that your system volume is up
- Verify the Python backend is running

**WebSocket connection failed?**
- Ensure `harmonium.py` is running first
- Check that port 8765 is not in use by another application
- Look for "Web App connected!" message in the Python terminal

**Lid angle not changing?**
- Verify `pybooklid` is properly installed
- Check that your MacBook's lid sensor is working
- Try closing and opening the lid to see if values change

## Stopping

- **Backend**: Press `Ctrl+C` in the terminal running `harmonium.py`
- **Frontend**: Simply close the browser tab

## License

Feel free to use and modify this project as you wish!
