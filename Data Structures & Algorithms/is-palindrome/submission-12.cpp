class Solution {
public:
    bool isPalindrome(string s) {
        auto it = std::remove_if(s.begin(), s.end(), [](unsigned char c){
            return !std::isalnum(c);
        });

        s.erase(it, s.end());

        for (char& c : s) c = std::tolower((unsigned char)c);

        return std::equal(s.begin(), s.begin() + s.size() / 2, s.rbegin());
    }
};
