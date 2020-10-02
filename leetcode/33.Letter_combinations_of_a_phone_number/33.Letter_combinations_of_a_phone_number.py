from typing import List

def letterCombinations(digits: str) -> List[str]:
    def dfs(index, path):
        # if meet the end of the tree, do backtracking
        if len(path) == len(digits):
            result.append(path)
            return
        
        # do iterative based on len(digits)
        for i in range(index, len(digits)):
            # do iterative based on the letters in digits
            for j in dic[digits[i]]:
                dfs(i + 1, path + j)

    # exception
    if not digits:
        return []

    dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
           "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    result = []
    dfs(0, "")

    return result

print(letterCombinations("23"))