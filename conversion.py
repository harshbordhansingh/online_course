def conversion(li):
    new_list = [float(i) for i in li]
    c = sum(new_list)
    return c


print(conversion(['2.2', '2.3', '2.4']))