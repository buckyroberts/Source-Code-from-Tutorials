var xmlHttp = createXmlHttpRequestObject();

function createXmlHttpRequestObject() {
	var xmlHttp;

	if (window.XMLHttpRequest) {
		xmlHttp = new XMLHttpRequest();
	} else {
		xmlHttp = new ActiveXObject('Microsoft.XMLHTTP');
	}

	return xmlHttp;
}

function process() {
	if (xmlHttp) {
		try {
			xmlHttp.open('GET', 'bacon.txt', true);
			xmlHttp.onreadystatechange = handleServerResponse;
			xmlHttp.send(null);
		} catch(e) {
			alert(e.toString());
		}
	}
}

function handleServerResponse() {
	theD = document.getElementById('theD');
	if (xmlHttp.readyState == 1) {
		theD.innerHTML += 'Status 1: server connection established <br/>';
	} else if (xmlHttp.readyState == 2) {
		theD.innerHTML += 'Status 2: request received <br/>';
	} else if (xmlHttp.readyState == 3) {
		theD.innerHTML += 'Status 3: processing request <br/>';
	} else if (xmlHttp.readyState == 4) {
		if (xmlHttp.status == 200) {
			try {
				text = xmlHttp.responseText;
				theD.innerHTML += 'Status 4: request is finished and response is ready <br/>';
				theD.innerHTML += text;
			} catch(e) {
				alert(e.toString());
			}
		} else {
			alert(xmlHttp.statusText);
		}
	}
}