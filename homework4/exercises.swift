/* A function that accepts a number of U.S. cents (an Int) and returns a Result object 
that can indicate (1) for success, a 4-tuple containing the smallest number of U.S. 
quarters, dimes, nickels, and pennies that equal the given amount, or (2) a failure 
whenever a negative amount was supplied. See the unit test for information on how you 
are to craft the result type. Implmentation restriction: use the Int method quotientAndRemainder. */

/* A String computed property that computes a new string equal to the receiver but with all whitespace 
removed and then with the i-th grapheme (1-based) repeated i times. Note that you are to repeat graphemes, 
not code units. Good news: Swift does this automatically. */

/* A method on Array that maps a function over the receiver then returns the unique values after mapping. */

/* A function that generates powers of a given (integer) base, starting at the 0th power (namely, 1) 
through a given limit, consuming each with a closure. Note that consistent with Swift terminology, 
“through” here means including the limit value. */

/* An idiomatic Swift solution to the Animal-Cow-Sheep-Horse example that appears in the middle of the 
course notes on JavaScript. Not that in JavaScript, Python, C++, or Java, you have an Animal superclass 
with Horse, Cow, and Sheep appearing a subclasses. For your Swift solution, make Animal a protocol, and 
define the speak function as a default implementation in a protocol extension. Each of the three structs 
Horse, Cow, and Sheep should adapt the protocol, similar to the way the Rat struct in the supplied unit 
test script does. */

/* The world-famous “say” function but with a little twist, namely it needs to work like this:
> say("Hello").phrase
"Hello"
> say("Hello").and("my").and("name").and("is").and("Colette").phrase
"Hello my name is Colette" */

/* A function that accepts a function f and a value x> and returns f(f(x)). Remember you are doing Swift, 
not Java, so you can use functions directly (no need for objects with apply methods). */

/* A function that returns the uppercased version of the first string in a list that has a length greater 
than a given value, wrapped in an Optional, since there might not be any such string in the list. 
Implementation restriction: Your solution must find the first such value using the first method, then 
since that returns an optional, use the optional chaining operator ?. when you invoke the uppercasing 
method. This is so cool, right? */