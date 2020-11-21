// #ifndef Sayer_H
// #define Sayer_H

// // #include <algorithm>
// // #include <cassert>
// // #include <iostream>
// #include <map>
// #include <string>

// using namespace std;

// class Sayer {
// 	operater() // YOU CAN OVERLOAD THIS OPERATOR IN C++
// }

// Sayer say(string s) {

// }

// vector<pair<list<string>, vector<pair<string, int>>>> sorted_word_counts(list<string>) {

// }

// #endif 
//Start problem 3: queue definition
#ifndef Queue_H
#define Queue_H

// Bad practice in C++ in header files
// using namespace std;

#include <iostream>

template <class T>
class Queue{
	public:
		Queue();
		void enqueue(T);
		T dequeue();
		int get_size();
		friend std::ostream& operator<< <T>(std::ostream& os, const Queue<T>& q);

	private:
		// @ Dr. Toal, I prefer explictly adding private and placing at bottom
		//	you could just copy everything below and add it above the 'public' and default to private

		struct node<T>{
			node(T val){
				this.data = val;
				this.next = nullptr;
			}
			node(T val, node* next){
				this->data = val;
				this->next;
			}
			node* next; 
			T data;
		};
		node<T>* head, tail;
		int size;
};

#endif
