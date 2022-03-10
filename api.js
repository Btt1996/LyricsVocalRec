function startTime() {
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    // add a zero in front of numbers<10
     if (m < 10) {
      m = "0" + m;
    }
     if (h < 10) {
      h = "0" + h;
    }
     if (s < 10) {
      s = "0" + s;
    }
  var t= h + ":" + m + ":" + s;
  t= t.replaceAll(":","_");
  t=t+String.fromCharCode(parseInt("10"+(t[3])))+".json";
  return t;
  }
const fs = require('fs');
var fileus=startTime();

console.log(student);
      
      fetch('https://ayypi.com/lyrics', {
        method: "POST",
        body: fs.readFileSync(fileus),
        headers:fs.readFileSync("api.json")});