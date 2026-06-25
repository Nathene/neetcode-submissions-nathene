#include <array>

class DynamicArray {
    int capacity{};
    int size{};
    int* arr;
public:

    DynamicArray(int capacity) : capacity(capacity), size(0) {
        this->capacity = max(this->capacity, 1);
        this-> arr = new int[this->capacity];
    }

    ~DynamicArray() {
        delete[] arr;
    }

    int get(int i) {
        if (i < 0 || i >= size) {
            return -1;
        }

        return this->arr[i];
    }

    void set(int i, int n) {
        if (i < 0 || i >= size) return;

        this->arr[i] = n;
    }

    void pushback(int n) {
        if (size == capacity) resize();

        this->arr[size] = n;
        size++;

    }

    int popback() {
        if (size == 0) return -1;
        size--;
        int val = this->arr[size];
        return val;
    }

    void resize() {
        this->capacity *= 2;
        int* tmp = new int[this->capacity];

        for (int i{}; i < this->size; i++) {
            tmp[i] = this->arr[i];
        }
        delete[] this->arr;
        this->arr = tmp;
    }

    int getSize() {
        return this->size;

    }

    int getCapacity() {
        return this->capacity;
    }
};
