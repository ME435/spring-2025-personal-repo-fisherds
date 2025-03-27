async function sendCommand(command) {
    let response = await fetch(`/api/${command}`);
    let responseText = await response.text();
    console.log(responseText);

    //Display this responseText to the screen.
    document.querySelector("#responseText").innerHTML = responseText;
}

function main() {
    console.log("Ready!");

    document.querySelector("#reset").onclick = () => {
        sendCommand("RESET");
    };

    document.querySelector("#x1").onclick = () => {
        sendCommand("X-AXIS 1");
    };
    document.querySelector("#x2").onclick = () => {
        sendCommand("X-AXIS 2");
    };
    document.querySelector("#x3").onclick = () => {
        sendCommand("X-AXIS 3");
    };
    document.querySelector("#x4").onclick = () => {
        sendCommand("X-AXIS 4");
    };
    document.querySelector("#x5").onclick = () => {
        sendCommand("X-AXIS 5");
    };

    document.querySelector("#loaderStatus").onclick = () => {
        sendCommand("LOADER_STATUS");
    };

    document.querySelector("#move").onclick = () => {
        let fromIndex = document.querySelector("#fromIndex").value;
        let toIndex = document.querySelector("#toIndex").value;
        sendCommand(`MOVE ${fromIndex} ${toIndex}`);
    };
    
    

}

main();