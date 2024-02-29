
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        s=senate
        que=list(s)
        while len(set(que))!=1:
            if que[0]=="R":
                que.remove("D")
                que.remove("R")
                que.append("R")
            elif que[0]=="D":
                que.remove("R")
                que.remove("D")
                que.append("D")

        if que[0]=="R":
            return "Radiant"
        else:
            return "Dire"


            