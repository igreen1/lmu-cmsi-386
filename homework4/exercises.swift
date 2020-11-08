/* A function that accepts a number of U.S. cents (an Int) and returns a Result object 
that can indicate (1) for success, a 4-tuple containing the smallest number of U.S. 
quarters, dimes, nickels, and pennies that equal the given amount, or (2) a failure 
whenever a negative amount was supplied. See the unit test for information on how you 
are to craft the result type. Implmentation restriction: use the Int method quotientAndRemainder. */
struct NegativeAmountError: Error { }

func change(_ amount: Int) -> Result<(Int, Int, Int, Int), NegativeAmountError> {
    if amount < 0 {
      return .failure(NegativeAmountError())
    }

    let denominations = [25, 10, 5, 1]
    var amountLeft = amount
    var coinCounts = [Int]()

    for denomination in denominations {
      coinCounts.append(amountLeft/denomination)
      amountLeft %= denomination
    }

    let quarters = coinCounts[0]
    let dimes = coinCounts[1]
    let nickels = coinCounts[2]
    let pennies = coinCounts[3]
    return .success((quarters, dimes, nickels, pennies))
}

/* A String computed property that computes a new string equal to the receiver but with all whitespace 
removed and then with the i-th grapheme (1-based) repeated i times. Note that you are to repeat graphemes, 
not code units. Good news: Swift does this automatically. */
extension String {
  var stretched: String {
    return self
        .filter { !" \n\t\r".contains($0) }
        .enumerated()
        .map { String(repeating: $1, count: $0 + 1) }
        .joined()
  }
}

/* A method on Array that maps a function over the receiver then returns the unique values after mapping. */
extension Array {
  func mapThenUnique<T>(mapper: (Element) -> T) -> Set<T> {
    return Set( self.map {mapper($0)})
  }
}

/* A function that generates powers of a given (integer) base, starting at the 0th power (namely, 1) 
through a given limit, consuming each with a closure. Note that consistent with Swift terminology, 
“through” here means including the limit value. */
// func powers(of base: Int, through limit: Int, then f: (Int) -> Int) -> Int {
//   var power = 1
//   while power <= limit {
//     power *= base
//     return f(power)
//   }
// }

/* An idiomatic Swift solution to the Animal-Cow-Sheep-Horse example that appears in the middle of the 
course notes on JavaScript. Not that in JavaScript, Python, C++, or Java, you have an Animal superclass 
with Horse, Cow, and Sheep appearing a subclasses. For your Swift solution, make Animal a protocol, and 
define the speak function as a default implementation in a protocol extension. Each of the three structs 
Horse, Cow, and Sheep should adapt the protocol, similar to the way the Rat struct in the supplied unit 
test script does. */
protocol Animal {
  var name: String { get }
  var sound: String { get }
  func speak() -> String
}

extension Animal {
  func speak() -> String {
    return self.name + " says " + self.sound
  }
}

struct Cow: Animal {
    let name: String
    let sound = "moooo"
}

struct Sheep: Animal {
    let name: String
    let sound = "baaaa"
}

struct Horse: Animal {
    let name: String
    let sound = "neigh"
}

/* The world-famous “say” function but with a little twist, namely it needs to work like this:
> say("Hello").phrase
"Hello"
> say("Hello").and("my").and("name").and("is").and("Colette").phrase
"Hello my name is Colette" */
struct Sayer {
  var phrase: String
  func and(_ word: String) -> Sayer {
    return Sayer(phrase: self.phrase + " " + word)
  }
}

func say(_ word: String) -> Sayer {
    return Sayer(phrase: word)
}

/* A function that accepts a function f and a value x> and returns f(f(x)). Remember you are doing Swift, 
not Java, so you can use functions directly (no need for objects with apply methods). */
func twice<T>(_ f: (T) -> T, appliedTo x: T) -> T {
    return f(f(x))
}

/* A function that returns the uppercased version of the first string in a list that has a length greater 
than a given value, wrapped in an Optional, since there might not be any such string in the list. 
Implementation restriction: Your solution must find the first such value using the first method, then 
since that returns an optional, use the optional chaining operator ?. when you invoke the uppercasing 
method. This is so cool, right? */
func uppercasedFirst(of a: [String], longerThan n: Int) -> String? {
  return a.first(where: {$0.count > n})?.uppercased()
}
