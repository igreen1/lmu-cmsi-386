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

		~Queue(){
			//deconstructor for memory leaks
			while(head != nullptr){
				node* previous = head;
				head = head->next;
				delete previous;
			}
		}

		Queue(){
			head = nullptr;
			tail = nullptr;
			size = 0;
		}

		Queue(Queue&) = delete;
		Queue& operator=(Queue&) = delete;

		//Move is okay :)
		Queue(Queue&& other){
			// to stop deconstruction from destroying stuff
			this->head = nullptr;
			this->tail = nullptr;
			this->size = 0;
			if(other.head != nullptr){
				this->head = new node(other.head->data);
				this->size++;
				node *otherNode = other.head;
				node *node = this->head;
				while(otherNode->next != nullptr){
					otherNode = otherNode->next;
					node->next = new node(otherNode->data);
					this->size++;
					node = node->next;
				}
			}
		}

		Queue& operator=(Queue&& other){
			//to stop deconstruction from destroying stuff
			this->head = nullptr;
			this->tail = nullptr;
			this->size = 0;
			if(other.head != nullptr){
				this->head = new node(other.head->data);
				this->size++;
				node *otherNode = other.head,
						 *node = this->head;
				while(otherNode->next != nullptr){
					node = otherNode->next;
					node->next = new node(otherNode->data);
					this->size++;
					node = node->next;
				}
			}
			return *this;
		}

		void enqueue(T data){
			if(this->tail != nullptr) {
					// size > 1
					this->tail->next = new node(data);
					this->tail = this->tail->next;
			} else if (this-> head == nullptr) {
					// size == 0
					this->head = new node(data);
					this->tail = this->head->next;
			} else { 
					// size == 1
					this->head->next = new node(data);
					this->tail = this->head->next;
			}
			this->size++;
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

		int count_size(){
			//If we weren't storing size 
			//@Dr. Toal
			//	your specs ask us to store size buuuttt, just to prove we know what we're doing
			int queueSize = 0;
			node* node = head;
			while(node != nullptr) {
				queueSize++;
				node = node->next;
			}

			return queueSize;
		}

		friend std::ostream& operator<<(std::ostream& os, const Queue<T>& q){
				// Come up with new name for current, Toal will hate it
			auto node = q->head;
			while(node != nullptr){
				os << node->data << ", ";
				node = node->next;
			}
				os << std::endl;
			return os;
		}


	private:
		struct node{
			node(T data){
				this->data = data;
				this->next = nullptr;
			}
			node(T data, node* next){
				this->data = data;
				this->next;
			}
			node* next; 
			T data;
		};

		node *head,
					*tail;
		int size;
};

#endif

#ifndef say_H
#define say_H

#include <string>

struct Sayer {
	std::string toSay = "";
	auto operator()() {
		return toSay;
	}

	Sayer operator()(std::string s) {
		return { (toSay == "" ? "" : toSay + " ") + s };
	}
} say;


#endif

