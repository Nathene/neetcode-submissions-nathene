class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        dont_care = {"."}

        res = 0

        seen = set()

        def prune(word: str) -> str:
            res = ""
            for c in word:
                if c in dont_care: continue
                if c == "+": break
                res += c
            
            return res

        for email in emails:
            parts = email.split("@")
            name, domain = parts[0], parts[1]

            name = prune(name)
            seen.add(name+domain)
        
        return len(seen)
