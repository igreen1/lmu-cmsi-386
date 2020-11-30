//Put sorted word count and sayer declarations here :)


//Problem 1:
/*
Write a C++ function that accepts a list of strings and returns a vector of 
(word, count) pairs, sorted by the number of occurrences descending. 
See the unit test file for examples of what is expected. 
Use whatever wonderful functions you can find from the standard library. 
(In fact, one of the learning objectives for this problem is that you gain
experience by looking through the standard library.) 
*/

#include <vector>
#include <string>
#include <list>
#include "exercises.h"

using namespace std;

vector<pair<string, int>> sorted_word_counts(list<string> words){

  //for each words, count :)

  //use List<T>::findAll !
  //then List<T>::removeAll

  vector<pair<string, int>> result = new vector<pair<string, int>>();

  auto it = words.begin();

  list<string> givenWordOccurences;
  pair<string, int> wordResults;

  //for loops try to do some fancy compilation optimization
  // but the resizing of words makes that bad... so while loop!
  while(it != words.end()){
    givenWordOccurences = words.FindAll(*it);
    wordResults = new pair<string, int>{word, givenWordOccurences.size()};
    result.push_back(wordResults);
    words.removeAll(*it):
  }

}


//Problem 2:
/*
Implement the famous say function from the previous assignment. 
Hint: consider writing say as a struct with an overloaded function call 
operator. 
*/
