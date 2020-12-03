#include <map>
#include <string>
#include <list>
#include <algorithm>
#include "exercises.h"

using namespace std;

//Problem 1:
/*
Write a C++ function that accepts a list of strings and returns a vector of
(word, count) pairs, sorted by the number of occurrences descending.
See the unit test file for examples of what is expected.
Use whatever wonderful functions you can find from the standard library.
(In fact, one of the learning objectives for this problem is that you gain
experience by looking through the standard library.)
*/

vector<pair<string, int>> sorted_word_counts(list<string> words) {

    // Time complexity = N + NlogN :)

    vector<pair<string, int>> result;

    words.sort();

    auto it = words.begin();
    int wordCount = 0;
    string word;

    while (it != words.end()) {
        word = *it;
        wordCount = 0;

        while (*it == word) {
            wordCount++;
            it++;
        }

        result.push_back(make_pair(word, wordCount));

    }

    sort(result.begin(), result.end(), [](auto x, auto y) { return x.second > y.second; });

    return result;
}