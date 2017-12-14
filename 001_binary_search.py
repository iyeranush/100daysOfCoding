# Given a weight range scale which is sorted in asc order, I wish to see which range does my weight belong to.

weight_range = [(x, x+10) for x in range(200) if x%10 == 0]
my_weight = 145
