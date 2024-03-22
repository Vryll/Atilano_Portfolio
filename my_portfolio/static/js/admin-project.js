// const fileInput = document.getElementById('formFile');
// const fileList = document.getElementById('uploaded-files');

// fileInput.addEventListener('change', handleFileSelection);

// function handleFileSelection(event) {
//   const files = event.target.files; // Get the selected files

//   fileList.innerHTML = ''; // Clear previous list (if any)

//   if (!files.length) {
//     return; // No files selected, do nothing
//   }

//   for (let i = 0; i < files.length; i++) {
//     const file = files[i];
//     const fileName = file.name;

//     const listItem = document.createElement('li');
//     listItem.textContent = fileName;

//     const removeButton = document.createElement('button');
//     removeButton.textContent = 'Remove';
//     removeButton.addEventListener('click', () => {
//       const newFileList = Array.from(files); // Create a copy to avoid mutation
//       newFileList.splice(i, 1); // Remove the file from the array

//       fileList.innerHTML = ''; // Clear the list again
//       renderFileList(newFileList); // Re-render the list with updated files
//     });

//     listItem.appendChild(removeButton);
//     fileList.appendChild(listItem);
//   }
// }

// function renderFileList(files) {
//   // You can optionally define logic here to handle file information display,
//   // such as size, type, thumbnails (if applicable), etc.
//   // For simplicity, we'll just re-render the file names with removal buttons.

//   if (!files.length) {
//     return;
//   }

//   for (let i = 0; i < files.length; i++) {
//     const file = files[i];
//     const fileName = file.name;

//     const listItem = document.createElement('li');
//     listItem.textContent = fileName;

//     const removeButton = document.createElement('button');
//     removeButton.textContentq= 'Remove';
//     removeButton.addEventListener('click', () => {
//       const newFileList = Array.from(files); // Create a copy
//       newFileList.splice(i, 1); // Remove the file from the array

//       fileList.innerHTML = ''; // Clear the list again
//       renderFileList(newFileList); // Re-render the list with updated files
//     });

//     listItem.appendChild(removeButton);
//     fileList.appendChild(listItem);
//   }
// }
