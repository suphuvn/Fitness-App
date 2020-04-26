var START_DATE = new Date(); // put in the starting date here
var INTERVAL = 1; // in seconds
var INCREMENT = 1; // increase per tick
var START_VALUE = 0; // initial value when it's the start date
var count = 0;

String.prototype.toHHMMSS = function () {
    var sec_num = parseInt(this, 10); // don't forget the second param
    var hours   = Math.floor(sec_num / 3600);
    var minutes = Math.floor((sec_num - (hours * 3600)) / 60);
    var seconds = sec_num - (hours * 3600) - (minutes * 60);

    if (hours   < 10) {hours   = "0"+hours;}
    if (minutes < 10) {minutes = "0"+minutes;}
    if (seconds < 10) {seconds = "0"+seconds;}
    return hours+':'+minutes+':'+seconds;
}

$(document).ready(function () {
    var msInterval = INTERVAL * 1000;
    var now = new Date();
    count = parseInt((now - START_DATE) / msInterval) * INCREMENT + START_VALUE;
    time = String(count).toHHMMSS();
    document.getElementById('counter').innerHTML = time;

    window.setInterval(function () {
        count += INCREMENT;
        time = String(count).toHHMMSS();
        document.getElementById('counter').innerHTML = time;
    }, msInterval);

});