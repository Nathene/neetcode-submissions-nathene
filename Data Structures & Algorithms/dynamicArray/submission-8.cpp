class DynamicArray {
    int capacity{};
    int size{};
    std::unique_ptr<int[]> arr;
public:

    DynamicArray(int capacity) : capacity(capacity), size(0) {
        this->capacity = max(this->capacity, 1);
        this-> arr = std::make_unique<int[]>(this->capacity);
    }

    int get(int i) {
        if (0 <= i <= size) {
            return this->arr[i];
        }

        return -1;
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

        std::unique_ptr<int[]> tmp = std::make_unique<int[]>(this->capacity);

        for (int i{}; i < this->size; i++) {
            tmp[i] = this->arr[i];
        }
        this->arr = std::move(tmp);
    }

    int getSize() {
        return this->size;

    }

    int getCapacity() {
        return this->capacity;
    }
};
