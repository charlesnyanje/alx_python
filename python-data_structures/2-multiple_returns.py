def multiple_returns(sentence):
    if sentence:
        return (len(sentence), sentence[0])
    else:
        return (0, None)
print(multiple_returns("At Holberton school, I learnt C!"))