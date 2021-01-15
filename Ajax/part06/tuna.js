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
			xmlHttp.open('GET', 'tuna.xml', true);
			xmlHttp.onreadystatechange = handleStateChange;
			xmlHttp.send(null);
		} catch(e) {
			alert(e.toString());
		}
	}
}

// when state changes
function handleStateChange() {
	if (xmlHttp.readyState == 4) {
		if (xmlHttp.status) {
			try {
				handleResponse();
			} catch(e) {
				alert(e.toString());
			}
		} else {
			alert(xmlHttp.statusText);
		}
	}
}

// handle the response from the server
function handleResponse() {
	var xmlReponse = xmlHttp.responseXML;
	rootElement = xmlReponse.documentElement;
	names = rootElement.getElementsByTagName('name');
	ssns = rootElement.getElementsByTagName('ssn');

	var stuff = '';

	for (var i = 0; i < names.length; i++) {
		stuff += names.item(i).firstChild.data + '-' + ssns.item(i).firstChild.data + '<br>'; 
	}

	theD = document.getElementById('theD');
	theD.innerHTML = stuff;
}