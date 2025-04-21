import mqtt_helper as mh
import time

def my_first_callback(message_type, payload):
    print("Received type:", message_type)
    print("Received payload:", payload)
    # TODO: In a real program DO SOMETHING...

def main():
    print("Hacky MQTT Testing")
    mqtt_client = mh.MqttClient()
    mqtt_client.connect(subscription_topic_name="me435/fisherds",
                        publish_topic_name="me435/fisherds",
                        use_off_campus_broker=False)
    mqtt_client.callback = my_first_callback

    counter = 0
    while True:
        time.sleep(2.0)
        counter += 1
        mqtt_client.send_message("fisher", counter)


main()
