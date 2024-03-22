document.addEventListener("DOMContentLoaded", function() {
    const openButtons = document.querySelectorAll(".open-button");
    const closeButton = document.getElementById("close-button");
    const overlay = document.getElementById("overlay");

    

    openButtons.forEach(function(openButton) {
        openButton.addEventListener("click", function(event) {
         
            console.log(this)
            var dataId = this.getAttribute("data-id");
          
            var slideContainer = document.getElementById(`modal-container${dataId}`);
           
            slideContainer.classList.toggle("active");
            overlay.classList.toggle("active");
        });
    });


    closeButton.addEventListener("click", function() {
        const slideContainers = document.querySelectorAll(".slide-container.active");
        const activeOverlay = document.querySelector(".overlay.active");
        
        slideContainers.forEach(function(slideContainer) {
            slideContainer.classList.remove("active");
        });
        activeOverlay.classList.remove("active");
    });
});
