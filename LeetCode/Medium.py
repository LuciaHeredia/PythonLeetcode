def minOperations(boxes: str) -> [int]:
    # 1769. Minimum Number of Operations to Move All Balls to Each Box

    n: int = len(boxes)
    res: [int] = []

    # init List
    for i in range(n):
        res.append(0)

    # fill List
    for i in range(n):
        look_to_right = False
        look_to_left = False

        if int(boxes[i]) == 1:
            if i == 0:
                look_to_right = True
            elif i == n-1:
                look_to_left = True
            else:
                look_to_right = True
                look_to_left = True

        if look_to_right:
            for j in range(i + 1, n):
                res[j] += j - i
        if look_to_left:
            for j in range(i - 1, -1, -1):
                res[j] += i - j

    return res


def garbageCollection(garbage: [str], travel: [int]) -> int:
    # 2391. Minimum Amount of Time to Collect Garbage

    garbage_type = ['M', 'P', 'G']
    total_time = 0

    for t in garbage_type:
        t_time = 0
        last_i_summed = 0
        for i in range(len(garbage)):
            g = garbage[i]
            for c in g:
                if t == c:
                    t_time += 1
                    last_i_summed = i
        # sum pickup's time
        total_time += t_time
        # sum travel's time
        for j in range(last_i_summed):
            total_time += travel[j]
    return total_time


def numberOfBeams(bank: [str]) -> int:
    # 2125. Number of Laser Beams in a Bank
    total_beams = 0
    last_count = 0

    for i in bank:
        current_count = i.count('1')
        if current_count > 0:
            if last_count > 0:
                total_beams += last_count * current_count
            last_count = current_count

    return total_beams


def sortTheStudents(score: [[int]], k: int) -> [[int]]:
    # 2545. Sort the Students by Their Kth Score
    return sorted(score, key=lambda student: student[k], reverse=True)


def groupThePeople(groupSizes: [int]) -> [[int]]:
    # 1282. Group the People Given the Group Size They Belong To
    dict_res = {}
    res = []
    for person in range(len(groupSizes)):
        group_size = groupSizes[person]
        if group_size not in dict_res:
            dict_res[group_size] = [person]
        else:
            if int(group_size) == len(dict_res[group_size]):
                res.append(dict_res.pop(group_size))
                dict_res[group_size] = []
            dict_res[group_size].append(person)

    for vals in dict_res.values():
        res.append(vals)
    return res


def findMatrix(nums: [int]) -> [[int]]:
    freq = CountFrequency(sorted(nums))  # count frequency
    res = [[] for _ in range(max(freq.values()))]  # init 2D matrix
    for i in freq.keys():
        for j in range(freq[i]):
            res[j].append(i)
    return res


def CountFrequency(nums: [int]) -> dict[int, [int]]:
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq


def onesMinusZeros(grid: [[int]]) -> [[int]]:
    # 2482. Difference Between Ones and Zeros in Row and Column
    diff = []
    dict_count_columns = {}

    for i in range(len(grid)):
        row_diff = []
        row = grid[i]
        zeros_row = list(row).count(0)
        ones_row = list(row).count(1)
        for j in range(len(row)):
            if i == 0:  # count in first time
                zeros_column = 0
                ones_column = 0
                for ii in range(len(grid)):
                    column = grid[ii][j]
                    if column == 0:
                        zeros_column += 1
                    else:
                        ones_column += 1
                dict_count_columns[j] = {"zeros_column": zeros_column,
                                         "ones_column": ones_column}
            row_diff.append(ones_row + dict_count_columns[j]["ones_column"]
                            - zeros_row - dict_count_columns[j]["zeros_column"])
        diff.append(row_diff)
    return diff


def maxOperations(nums: list[int], k: int) -> int:
    # 1679. Max Number of K-Sum Pairs
    count = 0
    filtered_nums = sorted([n for n in nums if n < k])  # get relevant integers from array

    for i in range(len(filtered_nums)):
        num1 = filtered_nums[i]
        if num1 != 0:
            num2 = k - num1
            try:
                nums2_index = filtered_nums.index(num2, i+1, len(filtered_nums))
                filtered_nums[nums2_index] = 0
                filtered_nums[i] = 0
                count += 1
            except ValueError:
                continue
    return count


def findingUsersActiveMinutes(logs: list[list[int]], k: int) -> list[int]:
    # 1817. Finding the Users Active Minutes
    answer = [0 for _ in range(k)]  # init list
    filter_dict = {}

    for log in logs:
        log_id = log[0]
        log_minute = log[1]
        if log_id in filter_dict:
            filter_dict[log_id] = min(log_minute, filter_dict.get(log_id))
        else:
            filter_dict.update({log_id: log_minute})

    print(filter_dict)
    vals = list(filter_dict.values())
    for i in range(len(vals)):
        answer[i] = vals.count(vals[i])

    return answer


def main() -> None:
    logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]
    k = 5
    print(findingUsersActiveMinutes(logs, k))


if __name__ == '__main__':
    main()
