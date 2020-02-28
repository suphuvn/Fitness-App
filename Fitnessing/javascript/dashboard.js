/*eslint-env browser*/

function setBackground(element) {
    "use strict";
    element.style.backgroundImage = "url('Images/Tab.svg')";
    element.style.backgroundRepeat = "no-repeat";
    element.style.backgroundPosition = "right center";
    element.style.backgroundSize = "100px 130px";
}

function getURL() {
    "use strict";
    var pathname = window.document.location.pathname;
    var curr;
    
    if (pathname.endsWith("/home.html")) {
        curr = document.querySelector(".link1");
        setBackground(curr);
        document.querySelector(".home").src = "images/Home Icon.svg";
        document.querySelector(".workouts").src = "images/Weight Icon.svg";
        document.querySelector(".stats").src = "images/Bar Chart Icon.svg";
    } else if (pathname.endsWith("/workouts.html")) {
        curr = document.querySelector(".link2");
        setBackground(curr);
        document.querySelector(".workouts").src = "images/Weight Icon - Purple.svg";
        document.querySelector(".home").src = "images/Home Icon - White.svg";
        document.querySelector(".stats").src = "images/Bar Chart Icon.svg";

    } else if (pathname.endsWith("/stats.html")) {
        curr = document.querySelector(".link3");
        setBackground(curr);
        document.querySelector(".stats").src = "images/Bar Chart Icon - Purple.svg";
        document.querySelector(".workouts").src = "images/Weight Icon.svg";
        document.querySelector(".home").src = "images/Home Icon - White.svg";
    }
}

getURL();