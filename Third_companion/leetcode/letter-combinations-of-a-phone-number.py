class Solution:
    def letterCombinations(self, digits):
        graph = {"2":["a","b","c"],
                "3":["d","e","f"],
                "4":["g","h","i"],
                "5":["j","k","l"],
                "6":["m","n","o"],
                "7":["p","q","r","s"],
                "8":["t","u","v"],
                "9":["w","x","y","z"]}
        if digits == "":
            return ""
        if len(digits) == 1:
            return graph[digits]
        def printer(nums,start,puter,outed):
            if len(puter) == len(nums):
                pv = ""
                for px in puter:
                    pv += px
                outed.append(pv)
                puter.pop()
                return
            for i in graph[nums[start]]:
                puter.append(i)
                printer(nums, start + 1, puter, outed)
            if len(puter) != 0:
                puter.pop()
            elif puter == []:
                return outed
        return printer(digits,0,[],[])