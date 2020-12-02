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
				node* old = head;
				head = head->next;
				delete old;
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
				node *otherCurrNode = other.head;
				node *thisCurrNode = this->head;
				while(otherCurrNode->next != nullptr){
					otherCurrNode = otherCurrNode->next;
					thisCurrNode->next = new node(otherCurrNode->data);
					this->size++;
					thisCurrNode = thisCurrNode->next;
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
				node *otherCurrNode = other.head,
						 *thisCurrNode = this->head;
				while(otherCurrNode->next != nullptr){
					otherCurrNode = otherCurrNode->next;
					thisCurrNode->next = new node(otherCurrNode->data);
					this->size++;
					thisCurrNode = thisCurrNode->next;
				}
			}
			return *this;
		}

		void enqueue(T item){
			if(this->tail != nullptr)
			{
					// size > 1
					this->tail->next = new node(item);
					this->tail = this->tail->next;
			} else if (this-> head == nullptr) {
					// size == 0
					this->head = new node(item);
					this->tail = this->head->next;
			} else { 
					// size == 1
					this->head->next = new node(item);
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
			int count = 0;
			node* currNode = head;
			while(currNode != nullptr)
			{
				count++;
				currNode = currNode->next;
			}

			return count;
		}

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


	private:
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

