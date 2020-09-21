//Andrew Seaman, Booker Martin, Ian Green, Veronica Backer-Peral
import crypto from "crypto"
import fetch from "node-fetch"

/*
A function that accepts a number of U.S. cents and returns an 
    array containing, respectively, the smallest number of U.S. 
    quarters, dimes, nickels, and pennies that equal the given amount. 

Input: # of US cents 
Return [quarters, dimes, nickels, pennies]
*/
function change(totalCents) {
  //input verificiation
  if (totalCents < 0) {
    throw RangeError()
  }

  let coinValues = [25, 10, 5, 1] //stores the values of the denominations in decreasing order
  let coinsUsed = [0, 0, 0, 0] //stores how many of each respective denomination was used

  let remainingCents = totalCents //holds the amount of cents we still need to make change for
  let temp = 0
  for (let i = 0; i < coinValues.length; i++) {
    temp = Math.floor(remainingCents / coinValues[i]) //holds the amount of this denom we can use
    remainingCents -= temp * coinValues[i] //remove the cents since we have now 'given' change for that amount
    coinsUsed[i] = temp //store how much 'change' we have giving
  }

  return coinsUsed
}

/*
A function that accepts a string and returns a new string equal to the initial string with all 
    whitespace removed and then with the ith character (1-based) repeated i times. 

Input: string 
Output: input string with no white space and repeated characters based on position
*/
function stretched(input) {
  let output = ""
  let stripped = input.replace(/\s+/g, "")

  //add character based on location
  for (let i = 0; i < stripped.length; i++) {
    //Take each element, repeat is the amount of times as its location starting at 1
    //  then append it to the output string
    output += stripped[i].repeat(i + 1)
  }

  return output
}

/*
A function that randomly permutes a string. What does random mean? It means that each time you 
    call the function for a given argument, all possible permutations are equally likely. 
    Random is not the same as arbitrary. 

Input: string
Output: input string permuted randomly
*/
function scramble(input) {
  //input validation
  if (input.length <= 0) {
    return input
  }

  let output = ""
  let inputAsArray = input.split("") //protects input and makes easier to manipulate

  let i
  while (inputAsArray.length != 0) {
    i = Math.floor(Math.random() * inputAsArray.length)
    output += inputAsArray.splice(i, 1)
  }

  return output
}

/*
A function that yields successive powers of a base starting at the 0th power, namely 1, and going up to some limit. Consume the values with a callback. 
*/
function powers(base, limit, callback) {
  let currentValue = 1
  while (currentValue <= limit) {
    callback(currentValue)
    currentValue *= base
  }
}

/*
A JavaScript generator function that yields successive powers of a base starting at the 0th power, namely 1, and going up to some limit. 
*/
function* powersGenerator(base, limit) {
  let currentValue = 1
  while (currentValue <= limit) {
    yield currentValue
    currentValue *= base
  }
}

/*
A “chainable” function that accepts one string per call, but when called without arguments, returns the words previously passed, in order, separated by a single space
*/
function say(input) {
  if (!input) {
    return ""
  }
  return function (next) {
    if (!next) {
      return input
    } else {
      return say(input + " " + next)
    }
  }
}

/*
A function that interleaves an array with a bunch of values. If the array length is not the same as the number of values to interleave, the “extra” elements should end up at the end of the result. 
*/
function interleave(...values) {
  let output = [] //to append to, much easier

  //input validation
  if (!values) {
    return undefined //not my problem
  }

  let arrayA = values[0] //the first array to interweave

  //now for the other stuff to interweave into it
  let arrayB = []
  for (let i = 1; i < values.length; i++) {
    arrayB.push(values[i])
  }

  //find the smallest length to not go out of bounds
  let minimumLength = Math.min(arrayA.length, arrayB.length)

  let i = 0 //iterator, outside so I can do end appends
  for (i = 0; i < minimumLength; i++) {
    output.push(arrayA[i])
    output.push(arrayB[i])
  }

  if (arrayA.length > minimumLength) {
    //add rest of arrayA cause it wasn't finished
    output = output.concat(arrayA.slice(i))
  } else {
    //add rest of arrayB cause it wasn't finished
    output = output.concat(arrayB.slice(i))
  }

  return output
}

/*
A function that accepts three arguments: a crypto key, a crypto algorithm, and an initialization vector, and returns an array of two functions. The first returned function is an encryption function that encrypts a string into a hex string, and the second is a decryption function that decrypts the hex string into a string. Use the functions createCipheriv and createDecipheriv from the built-in Node crypto module. 
*/
function makeCryptoFunctions(key, cryptoAlgorithm, initializationVector) {
  function utf8ToHex(data) {
    let cipher = crypto.createCipheriv(
      cryptoAlgorithm,
      key,
      initializationVector
    )
    let encrypted = cipher.update(data, "utf8", "hex")
    return (encrypted += cipher.final("hex"))
  }

  function hexToUtf8(data) {
    let decipher = crypto.createDecipheriv(
      cryptoAlgorithm,
      key,
      initializationVector
    )
    let decrypted = decipher.update(data, "hex", "utf8")
    return (decrypted += decipher.final("utf8"))
  }

  return [utf8ToHex, hexToUtf8]
}

/*
A function that returns the top ten players by points-per-game among the players that have been in 15 games or more. The input to your function will be an object, keyed by team, with a list of player stats. Each player stat is an array with the player name, the number of games played, and the total number of points, for example: 
*/
function topTenScorers(teamsAndPlayers) {
  return Object.entries(teamsAndPlayers)
    .flatMap(([team, teamsAndPlayers]) =>
      teamsAndPlayers.map((p) => [...p, team])
    )
    .filter((p) => p[1] >= 15)
    .map(([name, gamesPlayed, points, team]) => ({
      name: name,
      ppg: points / gamesPlayed,
      team: team,
    }))
    .sort((a, b) => b.ppg - a.ppg)
    .slice(0, 10)
}

/*
A function that returns a promise that resolves to the product of two numbers, 
hitting the API at https://ordinary-hazel-pink.glitch.me/multiply?x=&y=
*/
function multiply(a, b) {
  let multURL = `https://ordinary-hazel-pink.glitch.me/multiply?x=${a}&y=${b}`

  //create a fetch promise
  return fetch(multURL)
    .then((response) => response.json())
    .then((json_data) => {
      if ("result" in json_data) {
        return json_data.result //json_data should be a simple {result: ###} :)
      } else {
        throw json_data
      }
    })
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
