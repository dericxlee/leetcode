class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x_sorted = sorted(rectangles, key=lambda x: x[0])
        y_sorted = sorted(rectangles, key=lambda x: x[1])
        x_tail = 0
        y_tail = 0
        x_sections = 0
        y_sections = 0

        for x1, y1, x2, y2 in x_sorted:
            if x1 >= x_tail:
                x_sections += 1

            x_tail = max(x_tail, x2)
        
        for x1, y1, x2, y2 in y_sorted:
            if y1 >= y_tail:
                y_sections += 1

            y_tail = max(y_tail, y2)
        
        if x_sections >= 3 or y_sections >= 3:
            return True
        
        return False
            
        



        