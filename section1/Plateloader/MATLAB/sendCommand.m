function response = sendCommand(command)

apiUrl = "http://fisherds-pi400-s2.rose-hulman.edu:8080/api/";
getUrl = apiUrl + command
response = webread(getUrl)

end

