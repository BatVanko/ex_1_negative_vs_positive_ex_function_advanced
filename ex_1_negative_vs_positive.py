def negative_vs_positive(*args):
    sum_negative = 0
    sum_positive = 0

    for x in args:
        if x > 0:
            sum_positive += x
        elif x < 0:
            sum_negative += x
    return sum_negative, sum_positive


nums = [int(x) for x in input().split()]
negative, positive = negative_vs_positive(*nums)
print(negative)
print(positive)
if abs(negative) > positive:
    print("The negatives are stronger than the positives")
else:
    print('The positives are stronger than the negatives')
