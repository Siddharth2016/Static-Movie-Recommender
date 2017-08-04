# Ranking the critics


def rank(data,per1,sim):
    totals = {}
    simsum = {}
    for other in data:
        if other==per1: continue
        simm = sim(data,per1,other)
        if simm<=0: continue

        for movie in data[other]:
            if movie not in data[per1] or data[per1][movie]==0:
                totals.setdefault(movie,0)
                totals[movie]+=data[other][movie]*simm
                simsum.setdefault(movie,0)
                simsum[movie]+=simm

    #Ranking
    ranking = [(totals[movie]/simsum[movie],movie) for movie in totals]
    ranking.sort(reverse = True)
    return ranking
