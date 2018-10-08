def reverse_string(data):
    char_list = [item for item in data]
    final_list = []
    for i in range(len(char_list)-1, -1, -1):
        final_list.append(char_list[i])
    return "".join(final_list)

assert "hbatewhs" == reverse_string("shwetabh")

def reverse_integer(data):
    operator = ""
    split_data = [i for i in str(data)]
    if isinstance(split_data[0], int):
        pass
    else:
        operator = split_data[0]
        split_data.remove(split_data[0])

    reversed = "".join(split_data)[::-1]
    if operator:
        return int("{0}{1}".format(operator, reversed))
    else:
        return int(reversed)

assert -54321 == reverse_integer(-12345)
assert 54321 == reverse_integer(-12345)