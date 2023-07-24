class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flippers = []
        for i in range(len(arr)):
            #print(arr,flippers)
            if arr == sorted(arr):
                return flippers
            max = (0,0)
            for j in range(len(arr)-i):
                if max[0] < arr[j]:
                    max = (arr[j],j)
            if max[1] != 0:
                flippers.append(max[1]+1)
                c = arr[:max[1]+1]
                c.reverse()
                arr = c + arr[max[1]+1 : ]
                flippers.append(len(arr)-i)
                if i == 0:
                    arr.reverse()
                else:
                    d = arr[:len(arr)-i]
                    d.reverse()
                    arr = d + arr[len(arr)-i:]
            else:
                flippers.append(len(arr)-i)
                if i == 0:
                    arr.reverse()
                else:
                    d = arr[:len(arr)-i]
                    d.reverse()
                    arr = d + arr[len(arr)-i:]
        return flippers
