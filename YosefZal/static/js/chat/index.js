//fix that to be independent code
// should redirect to the same room depended on user make new modul of tupples

var myVar = document.getElementById("myVar").value;
if (myVar === 'ziv'){
    window.location.href = '/chat/' + 'david' + '/';
}
else{
    window.location.href = '/chat/' + myVar + '/';
}
