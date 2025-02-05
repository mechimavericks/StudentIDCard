// Function to change profile picture
function changeProfilePicture() {
    document.getElementById("profilePicInput").click();
}

// Function to preview selected profile picture
function previewProfilePicture(event) {
    let reader = new FileReader();
    reader.onload = function () {
        let output = document.getElementById("profileImage");
        output.src = reader.result;
    };
    reader.readAsDataURL(event.target.files[0]);
}

// Function to download the ID card as an image
function downloadIDCard() {
    const idCard = document.getElementById("idCard");

    html2canvas(idCard, { scale: 2 }).then(canvas => {
        let link = document.createElement("a");
        link.href = canvas.toDataURL("image/png");
        link.download = "ID_Card.png";
        link.click();
    });
}

// Log when script is loaded
console.log("id.js loaded successfully.");
