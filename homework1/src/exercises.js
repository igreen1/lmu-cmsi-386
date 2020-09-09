/***
 * 
 */

/*
A function that accepts a number of U.S. cents and returns an 
    array containing, respectively, the smallest number of U.S. 
    quarters, dimes, nickels, and pennies that equal the given amount. 

Input: # of US cents 
Return [quarters, dimes, nickels, pennies]
*/
function change(centsTot){
    //since this is for a given set of denominations, 
    //  I will use simple solution not a general knapscak soln


    //input verificiation
    if(centsTot < 0){
        throw RangeError()
    }

    let denomVal = [25, 10, 5, 1]   //stores the values of the denominations in decreasing order
    let denomUsed = [0,0,0,0]       //stores how many of each respective denomination was used

    //should check programmer defined values but ehh, i'm smart


    var counter = centsTot
    var temp=0
    for(var i = 0 ; i < denomVal.length ; i++)
    {
        temp = Math.floor(counter/denomVal[i])
        counter -= temp*denomVal[i]
        denomUsed[i] = temp
    }

    return denomUsed
}


/*
A function that accepts a string and returns a new string equal to the initial string with all 
    whitespace removed and then with the ith character (1-based) repeated i times. 

Input: string 
Output: input string with no white space and repeated characters based on position
*/
function stretched(inputString){

    var outputString = ""     //String to hold the manipulated string. 
                        //  Makes indexing way easier
    var stripped        //Holds the inputString without whitespace (to preserve input variable)
    
    //input validation (? tbd)

    //remove whitespace 
    //regex makes NO sense, I stole this from a program I wrote
    //  ages ago. Likely sourced from StackOverFlow
    stripped = inputString.replace(/\s+/g,'')

    //add character based on location
    for(var i = 0; i < stripped.length; i++)
    {
        //Take each element, repeat is the amount of times as its location starting at 1
        //  then append it to the output string
        outputString += stripped[i].repeat(i+1)
    }

    return outputString

}

/*
A function that randomly permutes a string. What does random mean? It means that each time you 
    call the function for a given argument, all possible permutations are equally likely. 
    Random is not the same as arbitrary. 

Input: string
Output: input string permuted randomly
*/
function scramble(inputString){

    //input validation
    if(inputString.length <= 0){
        return inputString
    }

    var outputString = ''                       //holds the output to return
    var inputAsArray
    inputAsArray = inputString.split("")    //protects input and makes easier to manipulate

    //While there are characters unassigned,
    //  1. pick a random character from input
    //  2. add it to the output string
    //  3. remove it from input string
    var j
    while (inputAsArray.length != 0){
        
        //this command is a bit of a doozy haha so i split it up
        //first, find the index to copy (random index from iAA)
        j = Math.floor(Math.random() * inputAsArray.length)
        
        //now remove that random element from inputAsArray
        //this will return an array with 1 element as a string
        //so derefence the array with .toString()
        outputString += inputAsArray.splice(j,1).toString()


    }

    return outputString

}

/*
A function that yields successive powers of a base starting at the 0th power, namely 1, and going up to some limit. Consume the values with a callback. 
*/
function powers(x, y, z){

}

/*
A JavaScript generator function that yields successive powers of a base starting at the 0th power, namely 1, and going up to some limit. 
*/
function powersGenerator(x,y){

}

/*
A “chainable” function that accepts one string per call, but when called without arguments, returns the words previously passed, in order, separated by a single spac
*/

//header might need editing, idk how to do this
function say(x){

}

/*
A function that interleaves an array with a bunch of values. If the array length is not the same as the number of values to interleave, the “extra” elements should end up at the end of the result. 
*/
function interleave(x)
{

}

/*
A function that accepts three arguments: a crypto key, a crypto algorithm, and an initialization vector, and returns an array of two functions. The first returned function is an encryption function that encrypts a string into a hex string, and the second is a decryption function that decrypts the hex string into a string. Use the functions createCipheriv and createDecipheriv from the built-in Node crypto module. 
*/
function makeCryptoFunctions(x,y,z){

}

/*
A function that returns the top ten players by points-per-game among the players that have been in 15 games or more. The input to your function will be an object, keyed by team, with a list of player stats. Each player stat is an array with the player name, the number of games played, and the total number of points, for example: 
*/
function topTenScorers(x){
}

/*
A function that returns a promise that resolves to the product of two numbers, hitting the API at https://ordinary-hazel-pink.glitch.me/multiply?x=&y=
*/
function multiply(x,y){

}

export {
  change,
  stretched,
  scramble,
  say,
  powers,
  interleave,
  powersGenerator,
  makeCryptoFunctions,
  topTenScorers,
  multiply,
} 