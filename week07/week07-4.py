#1 2 4 8 16 32 64 128 256
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #剛剛沒寫完,現在寫完了....如果n是負的,就錯了!!!0也是錯
        if n <= 0: return False #現在成功了
        while n > 1: #因為1是2^0不用再除了
            if n%2 != 0: #竟然餘數不是0
                return False #失敗
            n = n // 2
        return True #就是成功