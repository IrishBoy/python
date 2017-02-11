def plus(n):
	for i in range (n):
		position+="+"
	position+="p"
def minus(m):
	for i in range (m):
		position+="-"
	position+="p"

otvet = str()
shest =input()
Numbers = [int(i) for i in shest.split(' ') if i.isdigit()]
shesterenki=[]
for i in range (20):
	shesterenki.append(int(0))
position = int(0)
for i in range(1,6):
	if position + i > 19:
		position=i-(19 - position)

for i in range (10000):
	Numbers[i]	
	here = min(abs(Numbers[i] - shesterenki[position]) ,abs(abs(0 - shesterenki[position]) + abs(Numbers[i] -10 )))
	here1 = min( (1 + abs(Numbers[i] - shesterenki[position + 1])) , 1 +  abs(abs(0 - shesterenki[position + 1]) + abs(Numbers[i] -10 )))
	here2 = min( (2 + abs(Numbers[i] - shesterenki[position + 2])) , 2 +  abs(abs(0 - shesterenki[position + 2]) + abs(Numbers[i] -10 )))
	here3 = min( (3 + abs(Numbers[i] - shesterenki[position + 3])) , 3 +  abs(abs(0 - shesterenki[position + 3]) + abs(Numbers[i] -10 )))
	here4 = min( (4 + abs(Numbers[i] - shesterenki[position + 4])) , 4 +  abs(abs(0 - shesterenki[position + 4]) + abs(Numbers[i] -10 )))
	here5 = min( (5 + abs(Numbers[i] - shesterenki[position + 5])) , 5 +  abs(abs(0 - shesterenki[position + 5]) + abs(Numbers[i] -10 )))
	here_1 = min( (1 + abs(Numbers[i] - shesterenki[position - 1])) , 1 +  abs(abs(0 - shesterenki[position - 1]) + abs(Numbers[i] -10 )))
	here_2 = min( (2 + abs(Numbers[i] - shesterenki[position - 2])) , 2 +  abs(abs(0 - shesterenki[position - 2]) + abs(Numbers[i] -10 )))
	here_3 = min( (3 + abs(Numbers[i] - shesterenki[position - 3])) , 3 +  abs(abs(0 - shesterenki[position - 3]) + abs(Numbers[i] -10 )))
	here_4 = min( (4 + abs(Numbers[i] - shesterenki[position - 4])) , 4 +  abs(abs(0 - shesterenki[position - 4]) + abs(Numbers[i] -10 )))
	here_5 = min( (5 + abs(Numbers[i] - shesterenki[position - 5])) , 5 +  abs(abs(0 - shesterenki[position - 5]) + abs(Numbers[i] -10 )))
	choise = min (here, here1, here2, here3, here4, here5, here_1, here_2, here_3, here_4, here_5)
