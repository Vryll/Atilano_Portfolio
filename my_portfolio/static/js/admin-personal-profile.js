  function showFileName(inputFile) {
    const fileName = inputFile.files[0].name; // Get the filename from the first selected file
    const fileDisplay = document.createElement('span'); // Create a span element to display the filename
    fileDisplay.textContent = fileName; // Set the span content to the filename
    inputFile.parentNode.appendChild(fileDisplay); // Add the span element next to the input field
  }