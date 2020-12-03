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
// 2. Using namespace is highly frowned upon in .h hence the std:: in this .h
//		We can change if you want
#include <iostream>

template <typename T>
class Queue {
public:

	~Queue() {
		//deconstructor for memory leaks
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

	Queue(Queue&&) = default;
	Queue& operator=(Queue&&) = default;

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

//Problem 2:
/*
Implement the famous say function from the previous assignment.
Hint: consider writing say as a struct with an overloaded function call
operator.
*/

#include <string>

struct Sayer {
	std::string toSay = "";
	auto operator()() { return toSay; }

	Sayer operator()(std::string s) {
		return { (toSay == "" ? "" : toSay + " ") + s };
	}
} say;


#endif

