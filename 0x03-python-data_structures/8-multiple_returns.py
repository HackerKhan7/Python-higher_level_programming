#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        sentence[:1] = None
    return (len(sentence), sentence[:1])