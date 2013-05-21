// JavaScript Document
/* --------------------------------------------------------------------------------
   [Check for Internet Exlporer]
-------------------------------------------------------------------------------- */
function isIE(){

  // make sure `g` is not found higher up the scope chain, by declaring it here
  var g = null;
  return (function(){
    var f = function g(){};
    // `g` should be resolved to `null` (the one we declared outside this function)
    // but since named function expression identifier leaks onto the enclosing scope in IE, 
    // it will be resolved to a function
    return (typeof g == 'function');
  })();
  
  //return true if current browser is IE
  
}
