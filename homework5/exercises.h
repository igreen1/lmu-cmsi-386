#ifndef FUNCTIONS_H_INCLUDED
#define FUNCTIONS_H_INCLUDED

#include <vector>
#include <list>
#include <string>

std::vector<std::pair<std::string, int>> sorted_word_counts(std::list<std::string>);

#endif


#ifndef Queue_H
#define Queue_H

//Two notes for grading @ Dr. Toal
// 1. Defined in .h because there are issues on the linking stage of compilation
//		these issues come from using templates. Ian can explain if you want
// 2. Using namespace is highly frowned upon in .h hence the std:: in this .h :)
//		We can change if you want ,,, but not really an issue imo
#include <iostream>

template <typename T>
class Queue{
	public:
		Queue(){
			this->size = 0;
			this->tail = nullptr;
			this->head = nullptr;
		}
		void enqueue(T item){
			if(this->tail != nullptr)
			{
					// size > 1
					this->tail->next = new node(item);
					this->tail = this->tail->next;
					this->size++;
					return;
			} else if (this-> head == nullptr) {
					// size == 0
					this->head = new node(item);
					this->tail = this->head->next;
					this->size++;
					return;
			} else { 
					// size == 1
					this->head->next = new node(item);
					this->tail = this->head->next;
					this->size++;
					return;
			}
		}
		T dequeue(){
			if(this->head == nullptr){
				throw std::underflow_error("No data in queue");
			}

			T result = this->head->data; 
			node* previousHead = this->head;
			this->head = this->head->next;
			this->size--;
			delete previousHead;
			return result;
		}
		int get_size(){return this->size;}

		friend std::ostream& operator<<(std::ostream& os, const Queue<T>& q){
				// Come up with new name for current, Toal will hate it
			auto currNode = q->head;
			while(currNode != nullptr){
				os << currNode->data << ", ";
				currNode = currNode->next;
			}
				os << std::endl;
			return os;
		}

		struct node{
			node(T val){
				this->data = val;
				this->next = nullptr;
			}
			node(T val, node* next){
				this->data = val;
				this->next;
			}
			node* next; 
			T data;
		};

	private:
		// @ Dr. Toal, I prefer explictly adding private and placing at bottom
		//	you could just copy everything below and add it above the 'public' and default to private
		node *head, *tail;
		int size;
};

#endif

#ifndef say_H
#define say_H



#endif


// #ifndef say_H
// #define say_H

// #include <iostream>
// #include <cstring>
// #include <string>
// //Never 'use' a namespace in header files :(

// struct Sayer {

// 	public:
// 	//Dr. Toal passed in C-Strings smh so beware, not std::string

// 	std::string operator()(){
// 		return "";
// 	}

// 	std::string operator()(std::string c){
// 		std::string s = "";
// 		int len = c.length();
// 		for(int i = 0; i < len; i++){
// 			s = s + c[i];
// 		}
// 		return s;
// 	}

// 	std::string operator()(std::string s, char c[]){
// 		int len = strlen(c);
// 		for(int i = 0; i < len; i++){
// 			s = s + c[i];
// 		}// #ifndef Queue_H
// #define Queue_H


// #include <iostream>

// template <class T>
// class Queue{
// 	public:
// 		Queue();
// 		void enqueue(T);
// 		T dequeue();
// 		int get_size();
// 		friend std::ostream& operator<< <T>(std::ostream& os, const Queue<T>& q);
// 		node* makeNode(){return node}
// 		struct node<T>{
// 			node(T val){
// 				this.data = val;
// 				this.next = nullptr;
// 			}
// 			node(T val, node* next){
// 				this->data = val;
// 				this->next;
// 			}
// 			node* next; 
// 			T data;
// 		};
// 	private:
// 		// @ Dr. Toal, I prefer explictly adding private and placing at bottom
// 		//	you could just copy everything below and add it above the 'public' and default to private

		
// 		node<T>* head, tail;
// 		int size;
// };

// #endif

// 		return s;
// 	}

// };

// #endif


// #ifndef say_H
// #define say_H

// // #include <algorithm>
// // #include <cassert>
// // #include <iostream>
// #include <map>
// #include <string>
// #include <vector>

// using namespace std;

// class Sayer {
// 	operater() // YOU CAN OVERLOAD THIS OPERATOR IN C++
// }

// Sayer say(string s) {

// }

// vector<pair<list<string>, vector<pair<string, int>>>> sorted_word_counts(list<string>) {

//  }

// // #endif 
// //Start problem 3: queue definition
