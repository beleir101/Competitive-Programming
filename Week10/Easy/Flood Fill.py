class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        main = image[sr][sc]
        visited = set()
        def checker(image,sr,sc,color,visited):
            if sr >= len(image) or sr < 0 or sc < 0 or sc >= len(image[0]):
                return
            if (sr,sc) in visited:
                return
            visited.add((sr,sc))
            if image[sr][sc] != main:
                return
            image[sr][sc] = color
            checker(image,sr+1,sc,color,visited)
            checker(image,sr-1,sc,color,visited)
            checker(image,sr,sc+1,color,visited)
            checker(image,sr,sc-1,color,visited)
        checker(image,sr,sc,color,visited)
        return image