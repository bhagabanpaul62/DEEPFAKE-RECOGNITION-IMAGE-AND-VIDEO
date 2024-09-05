console.log("App Loaded");

document
  .getElementById("uploadForm")
  .addEventListener("submit", function (event) {
    console.log("Form Submitted");
    event.preventDefault(); // Prevent the default form submission

    // Create FormData object
    const formData = new FormData(this);

    // Submit form data via Fetch API
    fetch(this.action, {
      method: "POST",
      body: formData,
    })
      .then((response) => response.text())
      .then((data) => {
        // Update the message container with the response message
        document.getElementById("message").classList.remove("hidden");
        document.getElementById("message").querySelector("h2").textContent =
          "Your upload was successful!";
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  });
