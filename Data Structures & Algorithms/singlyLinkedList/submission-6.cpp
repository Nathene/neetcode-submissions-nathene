struct Node {
    int val{};
    Node* next;
    public:
    Node(int val) : val(val), next(nullptr) {}
};


class LinkedList {
    int size{};
    Node* dummy_head{};
public:
    LinkedList() {
        dummy_head = new Node(-1);
        size = 0;
    }

    int get(int index) {
        if (index >= size) return -1;

        int ind = 0;
        Node* curr = dummy_head->next;
        while (curr != nullptr && ind < index) {
            curr = curr->next;
            ind++;
        }
        if (curr == nullptr) return -1;

        return curr->val;
    }

    void insertHead(int val) {
        Node* new_node = new Node{val};
        Node* old_head = dummy_head->next;
        dummy_head->next = new_node;
        new_node->next = old_head;
        size++;
    }
    
    void insertTail(int val) {
        Node* curr = dummy_head;

        while (curr->next != nullptr) {
            curr = curr->next;
        }

        curr->next = new Node{val};
        size++;
    }

    bool remove(int index) {
        if (index < 0 || index >= size) return false;
        Node* curr = dummy_head;
        int ind{};

        while (ind < index) {
            curr = curr->next;
            ind++;
        }

        Node* temp = curr->next;
        curr->next = curr->next->next;
        delete temp;
        size--;
        return true;
    }

    vector<int> getValues() {
        std::vector<int> res{};
        Node* curr = dummy_head->next;

        while (curr != nullptr) {
            res.push_back(curr->val);
            curr = curr->next;
        }

        return res;
    }
};
