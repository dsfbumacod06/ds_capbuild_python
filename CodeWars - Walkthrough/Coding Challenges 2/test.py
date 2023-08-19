class Solution:
    def checkStraightLine(self, coordinates):
        x1, y1 = coordinates.pop()
        x2, y2 = coordinates.pop()
        return all((y2-y1)*(x-x1) == (y-y1)*(x2-x1) for x,y in coordinates)
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))