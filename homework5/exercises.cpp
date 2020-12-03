#include <map>
#include <string>
#include <list>
#include <algorithm>
#include "exercises.h"

using namespace std;

vector<pair<string, int>> sorted_word_counts(list<string> words) {

    vector<pair<string, int>> result;

    // words.sort(); //do we need this?

	auto iterator = words.begin();
	int wordCount = 0;
	std::string word;

	while (iterator != words.end()) {
		word = *iterator;
		wordCount = 0;

		while (*iterator == word) {
			wordCount++;
			iterator++;
		}

		result.push_back(make_pair(word, wordCount));
	}

    sort(result.begin(), result.end(), [](auto x, auto y) { return x.second > y.second; });

    return result;
}


Sayer say;