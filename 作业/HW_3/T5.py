class PalindromeAndMerge:

    def __init__(self, s: str):
        """
        初始化方法，将字符串s作为成员变量。
        """
        self.s = s

    def longest_palindrome(self) -> str:
        """
        查找字符串中最长的回文子串。
        """
        if not self.s:
            return ""

        start, end = 0, 0
        for i in range(1, len(self.s)):
            left, right = i, i
            while left >= 0 and right < len(self.s) and self.s[left] == self.s[right]:
                if right - left > end - start:
                    start, end = left, right
                left -= 1
                right += 1

            left, right = i - 1, i + 1
            while left >= 0 and right < len(self.s) and self.s[left] == self.s[right]:
                if right - left > end - start:
                    start, end = left, right
                left -= 1
                right += 1

        return self.s[start:end + 1]

    def merge_sorted_lists(self, nums1: list, nums2: list) -> list:
        """
        合并两个已排序的数据集并进行排序。
        """
        merged = []
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        while i < len(nums1):
            merged.append(nums1[i])
            i += 1

        while j < len(nums2):
            merged.append(nums2[j])
            j += 1

        return merged

    def find_median_sorted_arrays(self, nums1: list, nums2: list) -> float:
        """
        求合并数据集的中位数。
        """
        merged = self.merge_sorted_lists(nums1, nums2)
        n = len(merged)
        if n % 2 == 1:
            return merged[n // 2]
        else:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2.0


def main():
    palindrome_merge = PalindromeAndMerge("babad")
    print(palindrome_merge.longest_palindrome())
    print(palindrome_merge.merge_sorted_lists([1, 2, 3], [4, 5, 6]))
    print(palindrome_merge.find_median_sorted_arrays([1, 2, 3], [4, 5, 6]))


if __name__ == "__main__":
    main()
