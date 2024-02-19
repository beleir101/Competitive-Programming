class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = []
        A = 0
        for x in s:
            if x == "(":
                st.append(A)
                A = 0
            else:
                A = st.pop()+max(A*2, 1)
        return A