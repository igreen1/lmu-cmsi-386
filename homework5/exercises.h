#ifndef FUNCTIONS_H_INCLUDED
#define FUNCTIONS_H_INCLUDED

#include <map>
#include <string>
#include <list>
#include <algorithm>
#include <vector>

#include <iostream>

// Yes this is bad convention in a .h file
// but because we don't know the compiler / command used
// we kinda have to
// Only used in this problem because there are TONS of stds here
using namespace std; 

vector<pair<string, int>> sorted_word_counts(list<string> words) {

  vector<pair<string, int>> result;
	
  words.sort();

	auto iterator = words.begin();
	int wordCount;
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
#endif


#ifndef Queue_H
#define Queue_H

#include <iostream>

template <typename T>
class Queue {
public:

	~Queue() {
		while (head != nullptr) {
			Node* previous = head;
			head = head->next;
			delete previous;
		}
	}

	Queue() {
		head = nullptr;
		tail = nullptr;
		size = 0;
	}

	Queue(Queue&) = delete;
	Queue& operator=(Queue&) = delete;

	Queue(Queue&& other) {
		*this = std::move(other);
	}

	Queue& operator=(Queue&& other) {
		if(this != &other){
			this->head = nullptr;
			this->tail = nullptr;
			this->size = 0;
			if (other.head != nullptr) {
				this->head = new Node(other.head->data);
				this->size++;
				Node* otherNode = other.head,
					* node = this->head;
				while (otherNode->next != nullptr) {
					otherNode = otherNode->next;
					node->next = new Node(otherNode->data);
					this->size++;
					node = node->next;
				}
			}
		}
		return *this;
	}

	void enqueue(T data) {
		if (this->tail != nullptr) { // size > 1
			this->tail->next = new Node(data);
			this->tail = this->tail->next;
		}
		else if (this->head == nullptr) { // size == 0
			this->head = new Node(data);
			this->tail = this->head->next;
		}
		else { // size == 1
			this->head->next = new Node(data);
			this->tail = this->head->next;
		}
		this->size++;
	}

	T dequeue() {
		if (this->head == nullptr) {
			throw std::underflow_error("No data in queue");
		}

		T result = this->head->data;
		Node* previousHead = this->head;
		this->head = this->head->next;
		this->size--;
		delete previousHead;
		return result;
	}

	int get_size() { return this->size; }

	//This is purely to show you we know how @ Dr. Toal
	int count_size() {
		int queueSize = 0;
		Node* node = head;
		while (node != nullptr) {
			queueSize++;
			node = node->next;
		}

		return queueSize;
	}

	friend std::ostream& operator<<(std::ostream& os, const Queue<T>& q) {
		auto node = q->head;
		while (node != nullptr) {
			os << node->data << ", ";
			node = node->next;
		}
		os << std::endl;
		return os;
	}


private:
	struct Node {
		Node* next;
		T data;
		Node(T data) : data(data), next(nullptr) { }
		Node(T data, Node* next) : data(data), next(next) { }
	};

	Node* head,
		* tail;

	int size;
};

#endif


#ifndef say_H
#define say_H

#include <string>

struct Sayer {
	std::string toSay = "";
	auto operator()() { return toSay; }

	Sayer operator()(std::string s) {
		return { (toSay == "" ? "" : toSay + " ") + s };
	}
} say;

#endif