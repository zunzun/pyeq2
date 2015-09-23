
models_3D = require("./Models_3D.js");

equationInfo = models_3D.Polynomial.Linear;

fittingTarget = 'SSQABS' // could be ODR, SSQREL, etc.

var textData = "" +
"  X      Y       Z\n" +
"3.017  2.175   0.320\n" +
"2.822  2.624   0.629\n" +
"2.632  2.839   0.950\n" +
"2.287  3.030   1.574\n" +
"2.207  3.057   1.725\n" +
"2.048  3.098   2.035\n" +
"1.963  3.115   2.204\n" +
"1.784  3.144   2.570\n" +
"1.712  3.153   2.721\n" +
"2.972  2.106   0.313\n" +
"2.719  2.542   0.643\n" +
"2.495  2.721   0.956\n" +
"2.070  2.878   1.597\n" +
"1.969  2.899   1.758\n" +
"1.768  2.929   2.088\n" +
"1.677  2.939   2.240\n" +
"1.479  2.957   2.583\n" +
"1.387  2.963   2.744\n" +
"2.843  1.984   0.315\n" +
"2.485  2.320   0.639\n" +
"2.163  2.444   0.954\n" +
"1.687  2.525   1.459\n" +
"1.408  2.547   1.775\n" +
"1.279  2.554   1.927\n" +
"1.016  2.564   2.243\n" +
"0.742  2.568   2.581\n" +
"0.607  2.571   2.753";

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
