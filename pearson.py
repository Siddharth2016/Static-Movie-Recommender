# Pearson Correlation Coefficient Algorithm to find the similarity score more precise as a straight line

from math import sqrt
def pearson_sim(data,person1,person2):
    sim = {}
    # Finding similar elements
    for key in data[person1]:
        if key in data[person2]:
            sim[key] = 1

    # If nothing similar
    if len(sim)==0: return 0

    #otherwise
    n = len(sim)
    sum1 = sum([data[person1][item] for item in sim])
    sum2 = sum([data[person2][item] for item in sim])

    # Sum of squares
    sumSq1 = sum([pow(data[person1][item],2) for item in sim])
    sumSq2 = sum([pow(data[person2][item],2) for item in sim])

    # Sum of product
    sop = sum([data[person1][item]*data[person2][item] for item in sim])

    num = sop - ((sum1*sum2)/n)
    den = sqrt((sumSq1 - (pow(sum1,2)/n))*(sumSq2 - (pow(sum2,2)/n)))
    if den==0: return 0
    
    return (num/den)
