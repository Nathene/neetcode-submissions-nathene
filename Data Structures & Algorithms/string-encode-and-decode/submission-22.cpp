class Solution {
public:

    string encode(vector<string>& strs) {
        std::string res{};

        for (const string& str : strs) {
            res += std::to_string(str.size()) + "#" + str;
        }

        return res;
    }

    vector<string> decode(string s) {
        int i{};
        vector<string> res{};
        while (i < s.size()) {
            int j = i;
            while (s[j] != '#') {
                j++;
            }
            int length = std::stoi(s.substr(i, j));
            i = j + 1;
            res.push_back(s.substr(i, length));
            i += length;
        }
        return res;
    }
};
