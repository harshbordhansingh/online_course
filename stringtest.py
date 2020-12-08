# def testing(a, b):
#     return "{}{}".format(a, b)
#
#
# print(testing("harsh", "sing"))

re = []


def test(*args):
    c = list(args)
    for i in c:
        re.append(i.upper())
        re.sort()
    return re


print(test("hi", "glacier"))