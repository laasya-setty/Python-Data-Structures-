class StripingZero:

    @staticmethod
    def stripingZeros(lst):
        if not lst or not lst[0]:
            return lst
        zero_row = set()
        zero_col = set()
        m,n = len(lst), len(lst[0])
        for r in range(m):
            for c in range(n):
                if lst[r][c] == 0:
                    zero_row.add(r)
                    zero_col.add(c)
        for r in range(m):
            for c in range(n):
                if r in zero_row or c in zero_col:
                    lst[r][c] = 0   
        
        return lst


if __name__ == "__main__":     
    matrix = [
        [5, 1, 9, 11],
        [2, 0, 6, 8],
        [13, 3, 0, 7],
        [15, 14, 12, 16]
    ]
    result = StripingZero.stripingZeros(matrix)
    print(result)