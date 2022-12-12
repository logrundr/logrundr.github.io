function createCookie(name,value,days) {
	if (days) {
		var date = new Date();
		date.setTime(date.getTime()+(days*24*60*60*1000));
		var expires = "; expires="+date.toGMTString();
	}
	else var expires = "";
	document.cookie = name+"="+value+expires+"; path=/";
}

function readCookie(name) {
	var nameEQ = name + "=";
	var ca = document.cookie.split(';');
	for(var i=0;i < ca.length;i++) {
		var c = ca[i];
		while (c.charAt(0)==' ') c = c.substring(1,c.length);
		if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
	}
	return null;
}

function eraseCookie(name) {
	createCookie(name,"",-1);
}

var current_theme = readCookie("theme");
if (current_theme == null) {
    var current_theme = createCookie("theme","black",1000);
}    

function changeThemeColors() {
    let root = document.documentElement;
  
    if (current_theme == "dark") {
        root.style.setProperty("--theme-background-color", "#ced3db");
        root.style.setProperty("--theme-text-color", "black");
        root.style.setProperty("--theme-link-color", "darkblue");
        root.style.setProperty("--theme-ext-target-color", "red");
        createCookie("theme","light",1000);
        current_theme = readCookie("theme");
    } else {
        root.style.setProperty("--theme-background-color", "#020308");
        root.style.setProperty("--theme-text-color", "#ececec");
        root.style.setProperty("--theme-link-color", "cornflowerblue");
        root.style.setProperty("--theme-ext-target-color", "red");
        createCookie("theme","dark",1000);
        current_theme = readCookie("theme");
    }
}

function loadThemeColors() {
    let root = document.documentElement;
  
    if (current_theme == "light") {
        root.style.setProperty("--theme-background-color", "#ced3db");
        root.style.setProperty("--theme-text-color", "black");
        root.style.setProperty("--theme-link-color", "darkblue");
        root.style.setProperty("--theme-ext-target-color", "red");
        createCookie("theme","light",1000);
        current_theme = readCookie("theme");
    } else {
        root.style.setProperty("--theme-background-color", "#020308");
        root.style.setProperty("--theme-text-color", "#ececec");
        root.style.setProperty("--theme-link-color", "cornflowerblue");
        root.style.setProperty("--theme-ext-target-color", "red");
        createCookie("theme","dark",1000);
        current_theme = readCookie("theme");
    }
}