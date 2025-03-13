// MQTT broker settings
const brokerUrl = 'ws://157.173.101.159:9001';
const topic = '/student_group/light_control';

// Create MQTT client
const client = mqtt.connect(brokerUrl);

// Handle connection
client.on('connect', () => {
    console.log('Connected to MQTT broker');
    updateStatus('Connected to MQTT broker');
});

// Handle errors
client.on('error', (error) => {
    console.error('MQTT Error:', error);
    updateStatus('Connection error!');
});

// Function to publish messages
function publishMessage(message) {
    client.publish(topic, message, (error) => {
        if (error) {
            console.error('Publish error:', error);
            updateStatus('Failed to send command!');
        } else {
            updateStatus(`Last command: Light ${message}`);
        }
    });
}

// Function to update status display
function updateStatus(message) {
    document.getElementById('status').textContent = message;
}