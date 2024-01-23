#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return (0)

    t_score = sum(score * weight for score, weight in my_list)
    t_weight = sum(weight for _, weight in my_list)

    if t_weight == 0:
        return (0)
    w_avg = t_score / t_weight
    return (w_avg)
