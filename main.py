# OUR MAIN FILE

from critics import critics
from euclid import euclid_sim
from pearson import pearson_sim
from ranking import rank
from math import sqrt

print(rank(critics,"Siddharth",pearson_sim))
print(rank(critics,"Siddharth",euclid_sim))



