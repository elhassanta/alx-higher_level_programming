#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    first = 0
    max_score_key = None
    for k, v in a_dictionary.items():
        if first == 0:
            first = 1
            max_score = v
            max_score_key = k
        if v > max_score:
            v = max_score
            max_score_key = k
    return max_score_key
