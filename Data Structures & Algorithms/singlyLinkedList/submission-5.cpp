class Node {
private:
    int val;
    Node* next;
    friend class LinkedList;
public:
    Node(int val) : val(val), next(nullptr) {}
};

class LinkedList {
private:
    Node* dummy_head;

public:
    LinkedList() : dummy_head(new Node(0)) {}

    ~LinkedList() {
        Node* curr = dummy_head;
        while (curr != nullptr) {
            Node* next = curr->next;
            delete curr;
            curr = next;
        }
    }

    int get(int index) {
        Node* curr = dummy_head->next;
        while (curr != nullptr) {
            if (index == 0) return curr->val;
            index--;
            curr = curr->next;
        }
        return -1;
    }

    void insertHead(int val) {
        Node* tmp = dummy_head->next;
        dummy_head->next = new Node(val);
        dummy_head->next->next = tmp;
    }
    
    void insertTail(int val) {
        Node* tmp = dummy_head;
        while (tmp->next != nullptr) {
            tmp = tmp->next;
        }
        tmp->next = new Node(val);
    }

    bool remove(int index) {
        Node* curr = dummy_head;

        while (curr != nullptr && index > 0) {
            curr = curr->next;
            index--;
        }
        if (curr == nullptr || curr->next == nullptr) return false;

        Node* to_del = curr->next;
        curr->next = curr->next->next;
        delete to_del;
        return true;
    }

    vector<int> getValues() {
        std::vector<int> result;
        Node* curr = dummy_head->next;

        while (curr != nullptr) {
            result.push_back(curr->val);
            curr = curr->next;
        }
        return result;
    }
};
