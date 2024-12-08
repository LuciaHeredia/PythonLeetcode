import collections
import math
import re
import numpy as np


def removeElementInArray(nums: list[int], val: int) -> int:
    """
    - Return k : count all different numbers from val in nums. \n
    - Array(nums) at end: k different numbers first(order not important), the others at last.
    """

    nums_len = len(nums)
    k = nums_len - collections.Counter(nums)[val]
    queue = []

    # add to Queue all numbers different from val
    for i in range(nums_len):
        if nums[i] != val:
            queue.append(nums[i])

    # all Queue numbers at front of array, the others(val) at last
    for i in range(nums_len):
        if len(queue) == 0:
            nums[i] = val
        else:
            nums[i] = queue.pop()

    return k


def removeDuplicates(nums: list[int]) -> int:
    """
    Remove Duplicates(in-place) from Sorted Array(non-decreasing order). \n
    - Return k : count of unique elements in Array(nums). \n
    - Array(nums) at end: k different numbers first(as in Array initially), the others at last.
    """

    s = sorted(set(nums))
    k = len(s)

    for i, value in enumerate(s):
        nums[i] = value

    return k


def finalValueAfterOperations(operations: list[str]) -> int:
    """
    ++X and X++ increments the value of the variable X by 1.
    --X and X-- decrements the value of the variable X by 1.
    """
    x = 0
    for s in operations:
        if s == "++X" or s == "X++":
            x += 1
        else:
            x -= 1
    return x


def findWordsContaining(words: list[str], x: str) -> list[int]:
    """ Return an array of indices representing the words that contain the character x. """
    indices = []
    for i in range(0, len(words)):
        if x in words[i]:
            indices.append(i)
    return indices


def shuffle(nums: list[int], n: int) -> list[int]:
    """
    :param nums: [x1,x2,...,xn,y1,y2,...,yn].
    :param n: len of x & y individually
    :return: [x1,y1,x2,y2,...,xn,yn]
    """
    res = []
    for i in range(0, n):
        res.append(nums[i])
        res.append(nums[i + n])
    return res


def numberGame(nums: list[int]) -> list[int]:
    arr = []
    nums.sort()
    for i in range(0, len(nums) - 1, 2):
        arr.append(nums[i + 1])
        arr.append(nums[i])
    return arr


def smallerNumbersThanCurrent(nums: list[int]) -> list[int]:
    arr = []
    sorted_nums = sorted(nums)

    for i in nums:
        # result array based on position of number in sorted_nums
        num = sorted_nums.index(i)
        arr.append(num)

    return arr


def subsetXORSum(nums: list[int]) -> int:
    total = 0

    for i in range(0, len(nums)):
        total += nums[i]
        for j in range(i + 1, len(nums)):
            total += nums[i] ^ nums[j]

    return total


def maximumWealth(accounts):
    """
    List[List[int]] -> accounts[i][j]
    = amount of money the i customer has in the j bank.
    Return the wealth(sum of j) that the richest customer has.
    """

    # long solution
    """
    max_wealth = 0
    for customer in accounts:
        sum_customer = 0
        for bank in customer:
            sum_customer += bank
        if sum_customer > max_wealth:
            max_wealth = sum_customer
    return max_wealth
    """

    # short solutions -> list comprehension
    return max([sum(row) for row in accounts])


def scoreOfString(s):
    score = 0
    for i in range(len(s) - 1):
        score += abs(ord(s[i]) - ord(s[i + 1]))
    return score


def mostWordsFound(sentences):
    # return max words in a sentence, from a list of sentences
    return max(len(s.split()) for s in sentences)


def removeOccurrences(s, part):
    # remove Occurrences of part in s, starting from left side
    part_index = s.find(part)
    while part_index >= 0:
        s = s.replace(part, "", 1)
        part_index = s.find(part)
    return s


def numJewelsInStones(jewels, stones):
    # jewels(type of stones), stones(stones i have)
    # return number of stones i have that are also jewels
    return sum(stones.count(s_type) for s_type in jewels)


def cellsInRange(s):
    res_list = []
    r_start = s[1]
    r_end = s[4]
    c_start = s[0]
    c_end = s[3]

    for j in range(ord(c_start), ord(c_end) + 1):
        c_current = chr(j)
        for i in range(int(r_start), int(r_end) + 1):
            res_list.append(c_current + str(i))
    return res_list


def countMatches(items, ruleKey, ruleValue):
    # 1773. Count Items Matching a Rule
    """
    :type items: List[List[str]]
    :type ruleKey: str
    :type ruleValue: str
    :rtype: int
    """
    return sum(1 for item in items if ruleKey == "type" and ruleValue == item[0] or
               ruleKey == "color" and ruleValue == item[1] or
               ruleKey == "name" and ruleValue == item[2])


def truncateSentence(s, k):
    # 1816. Truncate Sentence
    """
    :type s: str
    :type k: int
    :rtype: str - Truncate s, so it contains only the first k words.
    """
    list_s = s.split()
    new_s = ''

    if len(list_s) <= k:
        return s

    for i in range(k):
        new_s += list_s[i] + ' '
    return new_s.strip()


def arrayStringsAreEqual(word1, word2):
    # 1662. Check If Two String Arrays are Equivalent
    """
    :type word1: List[str]
    :type word2: List[str]
    :rtype: bool
    """
    return ''.join(word1) == ''.join(word2)


def largestLocal(grid):
    # 2373. Largest Local Values in a Matrix
    """
    :type grid: List[List[int]]
    :rtype: List[List[int]]
    """
    maxLocal = []
    maxLocalSize = (len(grid) - 2)
    np_grid = np.array(grid)  # numpy library

    for j in range(maxLocalSize):
        maxLocal_row = []
        for i in range(maxLocalSize):
            new_matrix = np_grid[j:j + 3, i:i + 3]
            maxLocal_row.append(int(max(map(max, new_matrix))))
        maxLocal.append(maxLocal_row)

    return maxLocal


def restoreString(s, indices):
    """
    :type s: str
    :type indices: List[int]
    :rtype: str
    """
    shuffled_s = ""
    for i in range(len(s)):
        shuffled_s += s[indices.index(i)]
    return shuffled_s


def isAcronym(words, s):
    # 2828. Check if a String Is an Acronym of Words
    """
    :type words: List[str]
    :type s: str
    :rtype: bool
    """
    new_s = ""
    for w in words:
        new_s += w[0]
    return s == new_s


def minimumOperations(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    num_of_op = 0
    for num in nums:
        if num % 3 != 0:
            num_of_op += 1
    return num_of_op


def differenceOfSum(nums):
    # 2535. Difference Between Element Sum and Digit Sum of an Array
    """
    :type nums: List[int]
    :rtype: int
    """
    sum_nums = 0
    sum_digits_nums = 0
    for num in nums:
        sum_nums += num
        for n in list(str(num)):
            sum_digits_nums += int(n)
    return abs(sum_nums - sum_digits_nums)


def addedInteger(nums1, nums2):
    # 3131. Find the Integer Added to Array(nums1) I
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: int
    """
    return min(nums2) - min(nums1)


def canAliceWin(nums):
    # 3232. Find if Digit Game Can Be Won
    """
    :type nums: List[int]
    :rtype: bool
    """
    single_sum = 0
    double_sum = 0
    for num in nums:
        if num < 10:
            single_sum += num
        else:
            double_sum += num

    return single_sum != double_sum


def mostFrequentEven(nums: list[int]) -> int:
    # 2404. Most Frequent Even Element
    min_element = -1
    count_element = 0
    dict_even = {}

    for num in nums:
        if num % 2 == 0:
            if num not in dict_even:
                dict_even.update({num: 1})
                min_element = num
                count_element = 1
            else:
                dict_even.update({num: dict_even[num] + 1})

    for k in dict_even:
        if dict_even[k] > count_element:
            min_element = k
            count_element = dict_even[k]
        elif dict_even[k] == count_element:
            if min_element > k:
                min_element = k

    return min_element


def findIntersectionValues(nums1: list[int], nums2: list[int]) -> list[int]:
    # 2956. Find Common Elements Between Two Arrays
    ans = [0, 0]

    for i in nums1:
        if i in nums2:
            ans[0] += 1
    for i in nums2:
        if i in nums1:
            ans[1] += 1

    return ans


def countAsterisks(s: str) -> int:
    # 2315. Count Asterisks
    count = 0
    count_asterisk = True

    for i in s:
        if i == '|':
            count_asterisk = not count_asterisk
        elif i == '*' and count_asterisk is True:
            count += 1

    return count


def sortPeople(names: list[str], heights: list[str]) -> list[str]:
    # 2418. Sort the People
    sorted_tup = sorted(zip(heights, names), key=None, reverse=True)
    res = [name for height, name in sorted_tup]
    return res


def plusOne(digits: list[int]) -> list[int]:
    # 66. Plus One
    res = ""
    for num in digits:
        res += str(num)
    res = str(int(res) + 1)
    return [int(x) for x in res]


def findMaxConsecutiveOnes(nums: list[int]) -> int:
    # 485. Max Consecutive Ones
    res = 0
    current_res = 0

    for n in nums:
        if n == 1:
            current_res += 1
            if current_res > res:
                res = current_res
        else:
            current_res = 0
    return res


def searchInsert(nums: list[int], target: int) -> int:
    # 35. Search Insert Position
    index = 0
    for i in range(len(nums)):
        num = nums[i]
        if num == target or target < num:
            return i
        else:
            index = i
    return index+1


def findPoisonedDuration(timeSeries: list[int], duration: int) -> int:
    # 495. Teemo Attacking
    total_seconds = duration

    for i in range(1, len(timeSeries)):
        current = timeSeries[i]
        prev = timeSeries[i-1]
        if current-duration >= prev:
            total_seconds += duration
        else:
            total_seconds += current-prev

    return total_seconds


def countBits(n: int) -> list[int]:
    # 338. Counting Bits
    res = [0] * (n+1)  # init list's size
    for i in range(1, n+1):
        res[i] = str(bin(i)).count('1')
    return res


def main() -> None:
    n = 5
    print(countBits(n))


if __name__ == '__main__':
    main()
