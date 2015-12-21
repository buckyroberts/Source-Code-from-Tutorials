// First Example
function doFirst() {
	document.write("I am first bo!");
}

function doSecond() {
	document.write(" 222222!!! ");
}

function start() {
	doFirst();
	doSecond();
}

start();

// Second Example
function doFirst() {
	document.write(" first! ");
	doSecond();
}

function doSecond() {
	document.write(" second! ");
	doFirst();
}

doFirst();