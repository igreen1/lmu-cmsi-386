import { rejects } from 'assert';
import { callbackify } from 'util';
import { Z_BLOCK } from 'zlib';

/***
 * 
 */
var crypto = require('crypto'); //I think we need this for the encryption function?
var fetch = require('node-fetch')

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


    var counter = centsTot  //holds the amount of cents we still need to make change for
    var temp = 0            //C used to yell at me and I'm scarred now. 
    for(var i = 0 ; i < denomVal.length ; i++)
    {
        temp = Math.floor(counter/denomVal[i])  //holds the amount of this denom we can use
        counter -= temp*denomVal[i]             //remove the cents since we have now 'given' change for that amount
        denomUsed[i] = temp                     //store how much 'change' we have giving
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

    var outputString = ""   //String to hold the final string 
                            //  Makes indexing way easier
    var stripped            //Holds the inputString without whitespace (to preserve input variable)
    
    //input validation (? it passes the tests so .... all good!)

    //remove whitespace 
    //regex makes NO sense, I stole this from a program I wrote
    //  ages ago. Likely sourced from StackOverFlow
    stripped = inputString.replace(/\s+/g,'')

    //could also use
    //strippped = inputString.replace(' ', '') 
    //but regex is cool!

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
    inputAsArray = inputString.split("")        //protects input and makes easier to manipulate

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

    let i = 0
    let currValue = 0

    while (Math.pow(x, i) <= y) {
        currValue = (Math.pow(x, i))
        z(currValue)
        i++
    }

}

/*
A JavaScript generator function that yields successive powers of a base starting at the 0th power, namely 1, and going up to some limit. 
*/
function* powersGenerator(x,y){
    let currValue = 1
    while (currValue <= y) {
        yield currValue
        currValue *= x
    }
}

/*
A “chainable” function that accepts one string per call, but when called without arguments, returns the words previously passed, in order, separated by a single space
*/

//header might need editing, idk how to do this
function say(x) {
    if (!x) { return '' }
    return function(next) {
        if (!next) {
            return x
        } else {
            return say(x + ' ' + next)
        }
    }
}

/*
A function that interleaves an array with a bunch of values. If the array length is not the same as the number of values to interleave, the “extra” elements should end up at the end of the result. 
*/
function interleave()
{

    let outputArray = [] //to append to, much easier

    //input validation
    if(arguments.length <=0){
        return undefined //not my problem
    }

    var arrayA = arguments[0] //the first array to interweave

    //now for the other stuff to interweave into it
    var arrayB = []
    for(var i = 1; i < arguments.length; i++){
        arrayB.push(arguments[i])
    }

    //i hate the ternary operator
    //find the smallest length to not go out of bounds
    let minLen = Math.min(arrayA.length, arrayB.length)

    var i = 0 //iterator, outside so I can do end appends
    for(i = 0; i < minLen; i++){
        outputArray.push(arrayA[i])
        outputArray.push(arrayB[i])
    }

    if(arrayA.length > minLen)
    {
        //add rest of arrayA cause it wasn't finished
        //outputArray = [...outputArray, ...arrayA]
        outputArray = outputArray.concat(arrayA.slice(i))
    }else{
        //add rest of arrayB cause it wasn't finished
        //outputArray = [...outputArray, ...arrayB]
        outputArray = outputArray.concat(arrayB.slice(i))
    }

    return outputArray

}

/*
A function that accepts three arguments: a crypto key, a crypto algorithm, and an initialization vector, and returns an array of two functions. The first returned function is an encryption function that encrypts a string into a hex string, and the second is a decryption function that decrypts the hex string into a string. Use the functions createCipheriv and createDecipheriv from the built-in Node crypto module. 
*/
function makeCryptoFunctions(x,y,z){ //x is key, y is alg, z is init. vector
    function utf8ToHex(data) {
        let cipher = crypto.createCipheriv(y, x, z) //creates cipher using alg, key, init. vector
        let encrypted = cipher.update(data, 'utf8', 'hex')
        encrypted += cipher.final('hex')
        return encrypted
    }

    function hexToUtf8(data) {
        let decipher = crypto.createDecipheriv(y, x, z) //creates decipher using alg, key, init. vector
        let decrypted = decipher.update(data, 'hex', 'utf8')
        decrypted += decipher.final('utf8')
        return decrypted
    }

    const functArray = [utf8ToHex, hexToUtf8] //puts both functions in an array
    return functArray
}

/*
A function that returns the top ten players by points-per-game among the players that have been in 15 games or more. The input to your function will be an object, keyed by team, with a list of player stats. Each player stat is an array with the player name, the number of games played, and the total number of points, for example: 
*/
function topTenScorers(x){
    return Object.entries(x).flatMap(([team, x]) => x.map(p => [...p, team])).filter(p => p[1] >= 15).map(([name, gamesPlayed, points, team]) => ({name: name, ppg: points/gamesPlayed, team:team})).sort(function(a, b) { return b.ppg - a.ppg }).slice(0,10)
}

/*
A function that returns a promise that resolves to the product of two numbers, 
hitting the API at https://ordinary-hazel-pink.glitch.me/multiply?x=&y=
*/
function multiply(a,b){

    let multURL = `https://ordinary-hazel-pink.glitch.me/multiply?x=${a}&y=${b}`

    //taken from MY github @
    //https://github.com/igreen1/dangermap

    //moved to a global import cause I think that's better
    //let fetch = require('node-fetch')

    return fetch(multURL).then(
        function(r){
            return r.json()
        }
    ).then(
        function(json_data){
            //de-json-ify
            if(json_data.result != undefined){
                return json_data.result
            }
            else{
                throw {
                    error: "Bad parameters",
                    status: 400,
                    x:a
                }
            }
            
        }

    )
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