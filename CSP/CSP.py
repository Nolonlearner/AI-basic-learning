import itertools
# 目标函数，检查是否满足 SEND + MORE = MONEY
def is_solution(assignment):
    S, E, N, D, M, O, R, Y = assignment

    # 检查无零约束：S和M不能为0
    if S == 0 or M == 0:
        return False

    # 构造整数形式
    send = 1000 * S + 100 * E + 10 * N + D
    more = 1000 * M + 100 * O + 10 * R + E
    money = 10000 * M + 1000 * O + 100 * N + 10 * E + Y

    # 检查是否满足 SEND + MORE = MONEY
    return send + more == money


# 变量和域定义
digits = range(10)  # 0到9的数字
letters = 'SENDMOREY'

# 遍历所有字母的可能分配
solution = None
for assignment in itertools.permutations(digits, 8):
    # 检查是否找到解
    if is_solution(assignment):
        solution = assignment
        print("solution:",solution)
        break

# 输出结果
solution if solution else "No solution found"