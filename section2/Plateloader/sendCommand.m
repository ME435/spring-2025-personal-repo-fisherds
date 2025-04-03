function response = sendCommand(command)

getUrl = "http://fisherds-pi400-s2.rose-hulman.edu:8080/api/" + command
% response = webread(getUrl)

options = weboptions('Timeout', 30); % Set timeout to 30 seconds
response = webread(getUrl, options);


end

