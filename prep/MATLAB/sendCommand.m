function response = sendCommand(command)

% import matlab.net.*
% import matlab.net.http.*
% 
% r = RequestMessage;
% uri = URI(["http://localhost:8080/api/" command])
% resp = send(r, uri)
% response = resp.Body.Data
% fprintf("Response to %s --> %s", command, response)

response = webread('http://localhost:8080/api/' + command);

end

