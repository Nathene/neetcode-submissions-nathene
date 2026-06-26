class DynamicArray {
    int capacity{};
    int size{};
    std::unique_ptr<int[]> arr;
public:

    DynamicArray(int capacity) : capacity(capacity), size(0) {
        capacity = max(capacity, 1);
        arr = std::make_unique<int[]>(capacity);
    }

    int get(int i) {
        if (0 <= i <= size) {
            return arr[i];
        }

        return -1;
    }

    void set(int i, int n) {
        if (0 <= i <= size) arr[i] = n;
    }

    void pushback(int n) {
        if (size == capacity) resize();

        arr[size] = n;
        size++;

    }

    int popback() {
        if (size == 0) return -1;
        size--;
        int val = arr[size];
        return val;
    }

    void resize() {
        capacity *= 2;

        std::unique_ptr<int[]> tmp = std::make_unique<int[]>(capacity);

        for (int i{0}; i < size; i++) {
            tmp[i] = arr[i];
        }
        arr = std::move(tmp);
    }

    int getSize() {
        return size;

    }

    int getCapacity() {
        return capacity;
    }
};
