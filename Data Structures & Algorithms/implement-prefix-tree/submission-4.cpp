class PrefixTree {
private:
    struct Node {
        char val;
        std::unordered_map<char, Node*> children;
        bool is_word;

        Node() : val('\0'), is_word(false) {}
        Node(char val) : val(val), is_word(false) {}
    };

    Node* root;

    void clear(Node* node) {
        for (auto& child : node->children) {
            clear(child.second);
        }
        delete node;
    }

public:
    PrefixTree() {
        this->root = new Node();
    }
    ~PrefixTree() {
        clear(root);
    }
    
    void insert(string word) {
        Node* curr = this->root;

        for (const auto& c : word) {
            auto it = curr->children.find(c);
            if (it == curr->children.end()) curr->children[c] = new Node(c);
            curr = curr->children[c];
        }
        curr->is_word = true;
    }
    
    bool search(string word) {
        Node* curr = this->root;

        for (const auto& c : word) {
            auto it = curr->children.find(c);
            if (it == curr->children.end()) return false;
            curr = it->second;
        }
        return curr->is_word;
    }
    
    bool startsWith(string prefix) {
        Node* curr = this->root;

        for (const auto& c : prefix) {
            auto it = curr->children.find(c);
            if (it == curr->children.end()) return false;
            curr = it->second;
        }
        return true;
    }
};
