# Market Scheduling

I had use the Stochastic hill climbing algorithm approach to solve the given problem.
It has been done in the following steps:
1.First I had generated the shops id after taking the given inputs(has formed both the distance,d and similarity,s matrix at the beginning)
2.Then doing the calculation of the goodness for the respective schedule using the formula given as:
	G(Schedule) = s(1,2) + s(1,3) + s(1,4) + s(2,3) + s(2,4) + s(3,4) + s(5,6) + s(5,7) + s(5,8)
	+ s(6,7) + s(6,8) + s(7,8) + ……. + s(13,14) + …. + s(21,22) + …..
	+ C x [d(1,13) + d(1,14)… d(2,13) + d(2,14) + … + d(5,17) + d(5,18) + …]
3.Then assuming it as a best schedule and considering it till we didn't get the next best schedule.
4.Now I will iterate the above to increase the chances of getting efficient schedule.
5.Again form the shop id's matrix but this time randomly allot id's to rach row and column of the shops matrix.
6.Repeat the step 2 for the above shop matrix.
7.If the current schedule has a better goodness score than the one assumed as current(as max. goodness), stored it in max variable.S
And considered this as a best schedule till we didn't get any better schedule than this.
8.Now repeat this process for 1000 times(or any no. of times),each time choosing randomly shop id's to increase the probability of getting best schedule.
9.At last iteration we will have aur best schedule of shops to deal with the current Covid situation and generate it as output.

