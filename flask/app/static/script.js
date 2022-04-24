function loading() {
    // document.getElementById("loading-txt").style.display = "none";
    document.getElementById("generateBtn").style.display = "none";
    document.getElementById("loading-btn").style.display = "inline-block";
    // message.innerText = "Gerando PDF...";
    // document.getElementById("loading").style.display = "inline-block";
    }

function hideSpinner() {
    // document.getElementById("loading-txt").style.display = "inline-block";
    document.getElementById("loading-btn").style.display = "none";
    document.getElementById("generateBtn").style.display = "inline-block";
    }