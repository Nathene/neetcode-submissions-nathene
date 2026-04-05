class MyQueue {
private:
    stack<int> main_q;
    stack<int> buffer; 

    void populate_buffer() {
        while (!main_q.empty()) {
            buffer.push(main_q.top());
            main_q.pop();
        }
    }

public:
    void push(int x) {
        main_q.push(x);
    }
    
    int pop() {
        if (buffer.empty())
            populate_buffer();
        int val = buffer.top();
        buffer.pop();
        return val;
    }
    
    int peek() {
        if (buffer.empty())
            populate_buffer();
        return buffer.top();
    }
    
    bool empty() {
        return (main_q.empty() && buffer.empty());
    }


};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */