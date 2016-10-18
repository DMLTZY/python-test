def rule_one(text):
    last = text[0]   # 记录上一个字符
    result = [last]  # 存放最终结果的list
    for i in text:
        if last == i:
            continue
        result.append(i)
        last = i
    print(''.join(result))


def rule_two(text):
    result = []
    my_list = list(text)
    length = len(text)
    i = 0      # 前游标
    j = i + 2  # 后游标
    last = -1  # 记录i是否移位
    while j < length-1:
        if my_list[i] == my_list[j]:
            if my_list[i+1] == my_list[j+1]:
                if last != i:
                    result.append(my_list[i])
                    result.append(my_list[i+1])
                j += 2
                last = i
            else:
                result.append(my_list[i])
                i += 1
                j += 1
        else:
            result.append(my_list[j])
            if i % 2 == 1:  # 计算游标移位方式
                i = j + 1
                j += 3
            else:
                i += 1
                j += 1
    for m in range(abs(j-length), 0, -1):  # 将最后不可能参与匹配的字符加入结果列表
        result.append(my_list[length-m])
    print(''.join(result))

if __name__ == '__main__':
    txt = 'abbbabbbaaaababbb'
    # txt = 'abbbabbb'
    rule_one(txt)
    txt = 'ababababjababababj'
    # txt = 'abababab'
    rule_two(txt)

