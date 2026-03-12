import asyncio
import websockets
import json
import random

async def handler(websocket):
    print("\nWeb App connected!")
    try:
        from pybooklid import LidSensor
        sensor = LidSensor()
        sensor_available = True
    except Exception as e:
        sensor_available = False
        print(f"LidSensor not available: {e}, using mock data")
    
    if sensor_available:
        with sensor:
            for angle in sensor.monitor(interval=0.05):
                print(f"\rCurrent Lid Angle: {angle:.2f}°   ", end="", flush=True)
                
                try:
                    await websocket.send(json.dumps({"angle": angle}))
                except websockets.ConnectionClosed:
                    print("\nWeb App disconnected.")
                    break
    else:
        # Mock sensor data for testing on Windows - simulates lid open/close
        angle = 180  # Start fully open
        direction = -1  # Moving toward closed
        step = 0.5  # Degrees per update
        
        while True:
            angle += direction * step
            if angle <= 0:  # Hit closed position
                direction = 1
                angle = 0
            elif angle >= 180:  # Hit open position
                direction = -1
                angle = 180
            
            try:
                await websocket.send(json.dumps({"angle": angle}))
                await asyncio.sleep(0.05)
            except websockets.ConnectionClosed:
                print("\nWeb App disconnected.")
                break

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("Bridge active! Waiting for your web app on port 8765...")
        await asyncio.Future()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nStopping Bridge...")