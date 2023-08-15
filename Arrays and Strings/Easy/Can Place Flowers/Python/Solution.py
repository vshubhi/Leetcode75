class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = len(flowerbed)
        for i in range(m):
            if flowerbed[i] == 0:
                is_left_plot_empty = (i==0 or flowerbed[i-1]==0)
                is_right_plot_empty = (i==m-1 or flowerbed[i+1]==0)

                if is_left_plot_empty and is_right_plot_empty:
                    flowerbed[i]=1
                    n-=1
            if n<=0:
                return True

        return n==0
            