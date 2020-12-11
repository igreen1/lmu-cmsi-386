# Homework 6

## Problem 1 
Given the C++ declaration:
```
struct {
	int n;
	char c;
} A[9][9]
```
On your machine, find the addresses of `A[0][0]` and `A[3][7]`. Explain why these values are what you found them to be.

### Solution:
HINT: Look up word 'alignment'
## Problem 2
Rewrite these C++ declarations in Go
```
double *a[n];
double (*b)[n];
double (c())[n];
double (d[n])();
double (*f(int (*)(int, int[]), int)) (int, ...);
```

### Solution:
```
var a *[]float64
```

## Problem 3
What does this script print under (a) static scope rules and (b) dynamic scope rules?
```
var x = 1
function h() { var x = 9; return g() }
function f() { return x }
function g() { var x = 3; return f() }
print f() * h() - x
```

### Solution:
A) Under static scope, this program returns `0` because h(). f(), and g() all use var x = 1.

B) Under dynamic scope, this program returns `2` because f() still returns 1, but h() and g() both return 3.


## Problem 4
Show the output of the following, assuming dynamic scope and (a) deep binding, and (b) shallow binding.
```
function g(h) {
  var x = 2
  h()
}

function main() {
  var x = 5
  function f() {
    print x + 3
  }
  g(f)
}

main()
```

### Solution:
A) Using deep binding, this program outputs `8` because the binding occurs in the outer main function.

B) Using shallow binding, this program outputs `5` because the binding occurs inside the g(h) function.

## Problem 5
Show the output of the following code fragment under the following four conditions: (a) pass by value, (b) pass by reference, (c) pass by value-result, and (d) pass-by-name.
```
x = 1
y = [2, 3, 4]
function f(a, b) { b++ ; a = x + 1 }
f(y[x], x)
print x, y[0], y[1], y[2]
```

### Solution:
A) 1, 2, 3, 4

B) 2, 2, 3, 4

C) 2, 2, 2, 4

D) 2, 2, 2, 4

## Problem 6
Rewrite the following JavaScript function so that it uses only arrow functions with simple expressions, that is, no local variables and no statements and no side-effects. In other words, rewrite it into a more pure functional style. Note that this means you will replace error throwing with returning Swift-style result objects.
```
function isPrime(n) {
  if (isNaN(n) || !Number.isInteger(n)) {
    throw 'Not an integer'
  } else if (n < 2 || n > Number.MAX_SAFE_INTEGER) {
    throw 'Number too big or too small'
  } else if (n === 2 || n === 3) {
    return true
  } else if (n % 2 === 0 || n % 3 === 0) {
    return false
  }
  for (let k = 5, w = 2; k * k <= n; k += w, w = 6-w) {
    if (n % k === 0) {
      return false
    }
  }
  return true
}
```

### Solution:

## Problem 7
Describe, in good English, and precise, erudite, and accurate language, why Python doesn't suffer from the billion-dollar mistake. Show me you understand the billion-dollar mistake. If you are working on a team, every single team member better contribute to or validate this answer. You need to understand this to pass the course, right?

### Solution:
Python doesn't have the billion dollar mistake because the `NoneType` is it's own type. That means that you can never have a string or object of type `None`. But in Java, every reference type defaults to `Null` so you can have `String s = ""` which is an empty string, but you can also have `String s = null` which is a string with value null. This is just confusing and contradicts Java's mission to be a strong statically typed language.

## Problem 8
Remember that old powers function you were asked to write so many times before? Here’s your chance to write it in either Go or Elixir. You’ll need to do some research because we have not covered these languages in much detail, but since you did the assigned readings, you now have enough background.

### Solution:
```
func powers(base int, limit int, c chan int) {
  var power = 1
  for power < limit {
    c <- power
    power = power * base
  }
}
```
