
models_2D = require("./Models_2D.js");

equationInfo = models_2D.Exponential.SimpleExponential_WithOffset;

fittingTarget = 'SSQABS' // could be ODR, SSQREL, etc.

var textData = "" +
"  X        Y \n" +
" 5.357    10.376 \n" +
" 5.457    10.489 \n" +
" 5.797    10.874 \n" +
" 5.936    11.049 \n" +
" 6.161    11.327 \n" +
" 6.697    12.054 \n" +
" 6.731    12.077 \n" +
" 6.775    12.138 \n" +
" 8.442    14.744 \n" +
" 9.769    17.068 \n" +
" 9.861    17.104 \n";

////////////////////////////////////////////////
////////////////////////////////////////////////

// see https://github.com/extrabacon/python-shell
var PythonShell = require('python-shell');

var options = {
  mode: 'json', // use JSON for communications
  pythonPath: '', // use system default python executable in this example
  pythonOptions: ['-u'], // the "-u" invokes unbuffered stdin and stdout
  scriptPath: '.', //path to the example python interface file
  
  // call the python interface file with these arguments
  args: [JSON.stringify(equationInfo),
         JSON.stringify(textData),
         JSON.stringify(fittingTarget)
         ]
};

console.log('Calling PythonShell.run()');
PythonShell.run('interface.py', options, function (err, results) {

  if (err) throw err; // rethrow any exception from python

  // results is an array consisting of messages collected during execution
  console.log('fitted coefficients:\n%j\n', results[0]);
  console.log('pyeq2-generated javascript code:\n%j\n', results[1]);

});
