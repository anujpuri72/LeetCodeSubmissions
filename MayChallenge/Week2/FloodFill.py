class Solution:
    def color(self, image1, a, b, origc, newc):
        # print(image1,)
        if (a < 0 or a >= len(image1) or b < 0 or b >= len(image1[a]) or image1[a][b] != origc):
            return
        else:
            image1[a][b] = newc
            self.color(image1, a-1, b, origc, newc)
            self.color(image1, a+1, b, origc, newc)
            self.color(image1, a, b-1, origc, newc)
            self.color(image1, a, b+1, origc, newc)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if (image[sr][sc] == newColor):
            return image
        self.color(image, sr, sc, image[sr][sc], newColor)
        return image
