// SVG to JSON
// (c) 2016 by Scriptol.com - Licence: MIT

// Load a SVG file and save it as a JSON file
// to be loaded from an HTML page.


var fs = require('fs');
var process = require('process');
var scriptol = require('/scriptolj/scriptol.js');


console.log();
console.log("SVG to JSON converter by Scriptol.");

var argv = process.argv
if(argv.length < 3) {
    console.log("Syntax:  node svgtojson.js filename")
    exit(1)
}

var svgname=argv[2];
if(svgname==="") {
   scriptol.die("End");
}

var p=svgname.lastIndexOf(".");
var jsoname=svgname.slice(0,p+1)+"json";

console.log("Converting " + svgname + " to " + jsoname)

var jso={};
scriptol.dLoad(jso,svgname);

for(var rootkey in jso) {
   var body = jso[rootkey] 
   var id=String(rootkey);
   break;
}

scriptol.dUnshift(body, "_00", id)

var svgnode=svgname.slice(0,p);

var jsostr=JSON.stringify(scriptol.clone(body),undefined,' ');
fs.writeFileSync(jsoname,jsostr);
console.log(jsoname+' '+"saved.");
console.log();
console.log("Usage:")
console.log("1) Load it from an HTML page")
console.log("2) Convert it into a JS object with JSON.parse")
console.log("And display it in canvas with scriptolcanvas.js");

