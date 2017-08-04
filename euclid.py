# Euclidean Distance Algorithm to find similarities between the dataset elements with given input

def euclid_sim(data,person1,person2):
    sim = {}
    # Taking similar objects from person1 an person2
    for key in data[person1]:
        if key in data[person2]:
            sim[key] = 1

    # If nothing similar then
    if len(sim)==0: return 0

    # Otherwise

    dist = sum([pow(data[person1][item]-data[person2][item],2) for item in sim])
    perf = 1/(1+dist)

    return perf
