class DynamicArray {
private:
    int* arr;
    int capacity;
    int size;

public:

    DynamicArray(int capacity) {
        this->capacity = capacity;
        this->size = 0;
        this-> arr = new int[capacity];
    }

    ~DynamicArray() {
        delete[] arr;
    }

    int get(int i) {
        if (0 <= i && i < this->size) return this->arr[i];

        return -1;
    }

    void set(int i, int n) {
        if (0 <= i && i < this->size) arr[i] = n;
    }

    void pushback(int n) {
        if (this->size == this->capacity) resize();
        this->arr[this->size++] = n;
    }

    int popback() {
        int val = this->arr[--this->size];
        return val;
    }

    void resize() {
        this->capacity = (this->capacity == 0) ? 1 : this->capacity * 2;
        int* tmp = new int[this->capacity];

        for (int i = 0; i < this->size; i++) {
            tmp[i] = this->arr[i];
        }

        delete[] arr;
        arr = tmp;
    }

    int getSize() {
        return this->size;
    }

    int getCapacity() {
        return this->capacity;
    }
};
