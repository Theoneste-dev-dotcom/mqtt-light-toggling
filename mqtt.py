import paho.mqtt.client as mqtt
import time

# MQTT broker settings
BROKER_URL = "157.173.101.159"
BROKER_PORT = 9001
TOPIC = "/student_group/light_control"

def on_connect(client, userdata, flags, rc, properties=None):
    print("Connected to MQTT Broker!")
    client.subscribe(TOPIC)
    print(f"Subscribed to topic: {TOPIC}")

def on_message(client, userdata, message):
    command = message.payload.decode()
    if command == "ON":
        print("💡 Light is TURNED ON")
    elif command == "OFF":
        print("💡 Light is TURNED OFF")
    else:
        print(f"Unknown command received: {command}")

def main():
    # Create MQTT client
    client = mqtt.Client(protocol=mqtt.MQTTv5, transport="websockets")
    
    # Set callback functions
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        # Connect to broker
        client.connect(BROKER_URL, BROKER_PORT, 60)
        
        # Start the loop
        print("Starting IoT device simulation...")
        print("Press Ctrl+C to exit")
        client.loop_forever()
        
    except KeyboardInterrupt:
        print("\nExiting...")
        client.disconnect()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()