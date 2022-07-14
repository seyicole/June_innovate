function changeText(id) {
    id.innerHTML = "you have changed this text with an 'onclick' event"
}


function displayDate(id) {
    document.getElementById("date").innerHTML = Date();
}


function checkCookies() {
    let text = ""
    if (navigator.cookiesEnabled == true) {
        text = "cookies are enabled";
    } else {
        text = "cookies are not enabled";
    }
    document.getElementById("cookie").innerHTML = text;
}


function mOver(obj) {
   obj.innerHTML = "<br> Hello Olu"
}

function mOut(obj) {
    obj.innerHTML = ""
}


function sendAlert() {
    alert(location.hostname);
}


// Dark Mode code!!!!


function darkMode() {
    let element = document.body;
    let mainBox = document.getElementsByClassName("main-box"); //making a list of every element that has the "main-box" class
    let mainText = document.getElementsByClassName("main-text"); //making a list of every element that has the "main-text" class
    let state = localStorage.getItem("state") // making a variable which has the value of state (as in key:value pair value)

    element.classList.toggle("dark-mode");
    
    for (const i of mainBox) {
        i.classList.toggle("dark-modeb")  //for every item within the list mainBox, toggle dark mode on
    }

    for (const x of mainText) {
        x.classList.toggle("dark-mode") //for every item within the list mainText, toggle dark mode on
    }


    // if state isn't dark, make a key:value pair with state as the key and dark as the value
    if (state !=="dark") {
        localStorage.setItem("state","dark")
    } else {
        localStorage.setItem("state","light") //if state is dark, make a key:value pair with state as the key and light as the value
    }
}


function darkCheck(){
    let element = document.body;
    let mainBox = document.getElementsByClassName("main-box");
    let mainText = document.getElementsByClassName("main-text");
    let state = localStorage.getItem("state")

    if (state =="dark") {
        element.classList.toggle("dark-mode");
    
        for (const i of mainBox) {
            i.classList.toggle("dark-modeb")
        }
    
        for (const x of mainText) {
            x.classList.toggle("dark-mode")
        }
    }
}

// if user has selected dark mode on previous page
// new page in dark mode
// else keep page in light mode


