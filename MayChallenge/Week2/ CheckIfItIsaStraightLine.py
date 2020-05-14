class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        div_zero1 = (coordinates[1][0]-coordinates[0][0])
        if((div_zero1) == 0):
            for i in coordinates:
                if (i[0] != coordinates[0]):
                    return False
            return True
        else:
            m = ((coordinates[1][1]-coordinates[0][1])/div_zero1)
            for i in range(1, len(coordinates)-1):
                div_zero = (coordinates[i+1][0]-coordinates[i][0])
                if(div_zero == 0):
                    return False
                m1 = ((coordinates[i+1][1]-coordinates[i][1])/div_zero)
                if (m1 != m):
                    return False
            return True
