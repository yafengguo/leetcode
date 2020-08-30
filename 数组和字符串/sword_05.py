class Solution:
    @staticmethod
    def replaceSpace(s: str) -> str:
        res_str = ""
        for ch in s:
            if ch == " ":
                res_str = res_str + "%20"
            else:
                res_str = res_str + ch
        return res_str


if __name__ == "__main__":
    print(Solution.replaceSpace("xx ud s"))
