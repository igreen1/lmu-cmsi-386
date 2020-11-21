#include "exercises.h" 

#include <iostream>

// YO
// I THINK NODE* MIGHT NEED TO BE THIS->NODE*
// DON'T HAVE TIME TO CHECK, ITS GAME NIGHT

using namespace std;

template <class T>
Queue<T>::Queue(){
    this->size = 0;
    this->tail = nullptr;
    this->head = nullptr;
}

template <class T>
void Queue<T>::enqueue(T item){

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
        size++;
        return;
    }

}

template <class T>
T Queue<T>::dequeue(){

    if(this->head != nullptr){

        T result = this->head->data; 
        node* previousHead; = this->head;
        this->head = this->head->next;
        delete previousHead;
        return result;

    } else {
        // might do some library of optionals of something
        // but for now, we'll do what C++ std does :)
        return -1;
    }

}


template <class T>
int Queue<T>::get_size(){
    // Dr. Toal's specs requests we store int size, so no calculations
    return this->size;
}

template <class T>
ostream& operator<<(ostream&, const Queue<T>&){
	// Come up with new name for current, Toal will hate it
	node *current = this->head;
	while(current != nullptr){
		os << current->data << ", ";
		current = current->data;
	}
    os << endl;
    return os;
}
