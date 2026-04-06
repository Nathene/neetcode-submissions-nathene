class KthLargest {
private:
    std::priority_queue<int, vector<int>, std::greater<int>> heap;
    int k;
    void check_size() {
        while (heap.size() > this->k) heap.pop(); 
    }
public:
    KthLargest(int k, vector<int>& nums) : k(k) {
        for (const auto& num : nums) {
            heap.push(num);

            check_size();
        }
    }
    
    int add(int val) {
        heap.push(val);
        check_size();
        return heap.top();
    }
};
