
document.addEventListener("DOMContentLoaded", function () {
    var dropdownButton = document.querySelector(".navbar-toggle");
    var dropdownContent = document.getElementById("dropdown-content");

    dropdownButton.addEventListener("click", function () {
        if (dropdownContent.classList.contains("show")) {
            dropdownContent.classList.remove("show");
            dropdownButton.setAttribute("aria-expanded", "false");
        } else {
            dropdownContent.classList.add("show");
            dropdownButton.setAttribute("aria-expanded", "true");
        }
    });
});






