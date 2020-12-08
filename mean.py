def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values())/len(value)
    else:
        the_mean = sum(value)/len(value)
    return the_mean


li = [12.3, 5.5, 5.6]
di = {"ramesh": 12.3, "suresh": 5.5, "mukesh": 5.6}
print(mean(di))