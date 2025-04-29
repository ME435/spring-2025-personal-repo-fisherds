function hackyMqttTest()
clc
fprintf("Hacky MQTT Test in MATLAB\n")
mqClient = mqttclient("tcp://test.mosquitto.org");
% mqClient.Connected

mqClient.subscribe("me435/fisherds2/#", "Callback", @myCallback)

for k = 1:3
   pause(1)
%    message = sprintf("My number is %d.", k);

   messageStruct.type = "chat";
   messageStruct.payload = sprintf("My number is %d.", k);
   message = jsonencode(messageStruct);

   write(mqClient, "me435/fisherds2/to_pi", message);
end
pause(1)  % small delay to receive the last message

end

function myCallback(topic, message)
% topic
message

messageStruct = jsondecode(message);
messageType = messageStruct.type
payload = messageStruct.payload

end
