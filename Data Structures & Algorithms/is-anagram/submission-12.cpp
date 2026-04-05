class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        std::unordered_map<char, int> letters;
        for (const char& c : s) {
            letters[c]++;
        }        
        for (const char& c : t) {
            if (letters.contains(c)) {
                letters[c]--;
                if (letters[c] < 0) {
                    return false;
                }
            } else {
                return false;
            }

        }
        return true;
    }
};
