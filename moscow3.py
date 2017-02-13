def plus(n):
	otvet1 =str()
	for i in range (n):
		otvet1+="+"
	otvet1+="p"
	return(otvet1)
def minus(m):
	otvet2 =str()
	for i in range (m):
		 otvet2+="-"
	otvet2+="p"
	return(otvet2)
otvet = str()
f = open("1c.txt")
Numbers = f.read().split()
shesterenki=[]
for i in range (20):
	shesterenki.append(int(0))
position = int(0)
for i in range (len(Numbers)):
	if position + 1 > 19:
		position = 0
	if position + 2 > 19:
		position = 2 - (19 - position) - 1
	if position + 3 > 19:
		position = 3 - (19 - position) - 1
	if position + 4 > 19:
		position = 4 - (19 - position) - 1
	if position + 5 > 19:
		position = 5 - (19 - position) - 1
	here = min((abs(int(Numbers[i]) - int(shesterenki[position]))) ,abs(abs(0 - int(shesterenki[position])) + abs(int(Numbers[i]) -10 )))
	here1 = min((1 + abs(int(Numbers[i]) - int(shesterenki[position + 1]))) , 1 +  abs(abs(0 - int(shesterenki[position + 1])) + abs(int(Numbers[i]) -10 )))
	here2 = min((2 + abs(int(Numbers[i]) - int(shesterenki[position + 2]))) , 2 +  abs(abs(0 - int(shesterenki[position + 2])) + abs(int(Numbers[i]) -10 )))
	here3 = min((3 + abs(int(Numbers[i]) - int(shesterenki[position + 3]))) , 3 +  abs(abs(0 - int(shesterenki[position + 3])) + abs(int(Numbers[i]) -10 )))
	here4 = min((4 + abs(int(Numbers[i]) - int(shesterenki[position + 4]))) , 4 +  abs(abs(0 - int(shesterenki[position + 4])) + abs(int(Numbers[i]) -10 )))
	here5 = min((5 + abs(int(Numbers[i]) - int(shesterenki[position + 5]))) , 5 +  abs(abs(0 - int(shesterenki[position + 5])) + abs(int(Numbers[i]) -10 )))
	here_1 = min((1 + abs(int(Numbers[i]) - int(shesterenki[position - 1]))) , 1 +  abs(abs(0 - int(shesterenki[position - 1])) + abs(int(Numbers[i]) -10 )))
	here_2 = min((2 + abs(int(Numbers[i]) - int(shesterenki[position - 2]))) , 2 +  abs(abs(0 - int(shesterenki[position - 2])) + abs(int(Numbers[i]) -10 )))
	here_3 = min((3 + abs(int(Numbers[i]) - int(shesterenki[position - 3]))) , 3 +  abs(abs(0 - int(shesterenki[position - 3])) + abs(int(Numbers[i]) -10 )))
	here_4 = min((4 + abs(int(Numbers[i]) - int(shesterenki[position - 4]))) , 4 +  abs(abs(0 - int(shesterenki[position - 4])) + abs(int(Numbers[i]) -10 )))
	here_5 = min((5 + abs(int(Numbers[i]) - int(shesterenki[position - 5]))) , 5 +  abs(abs(0 - int(shesterenki[position - 5])) + abs(int(Numbers[i]) -10 )))
	choise = min(here, here1, here2, here3, here4, here5, here_1, here_2, here_3, here_4, here_5)
	if choise == here:
		minhere =(abs(int(Numbers[i]) - int(shesterenki[position])) ,abs(abs(0 - int(shesterenki[position])) + abs(int(Numbers[i]) -10 )))
		if minhere == abs(int(Numbers[i]) - int(shesterenki[position])):
			if (int(Numbers[i]) - int(shesterenki[position])) > 0:
				otvet+=plus(int((int(Numbers[i]) - int(shesterenki[position]))))
			else:
				otvet+=minus(int(abs((int(Numbers[i]) - int(shesterenki[position])))))
		else:
			otvet+=minus(abs(abs(0 - int(shesterenki[position])) + abs(int(Numbers[i]) -10 )))
		shesterenki[position]=Numbers[i]
		position = position
	if choise == here1:
		minhere1 = ( (1 + abs(int(Numbers[i]) - int(shesterenki[position + 1]))) , 1 +  abs(abs(0 - int(shesterenki[position + 1])) + abs(int(Numbers[i]) -10 )))
		otvet+=">"
		if minhere1 == 1 + abs(int(Numbers[i]) - int(shesterenki[position + 1])):
			if (int(Numbers[i]) - int(shesterenki[position + 1])) > 0:
				otvet+=plus(int((int(Numbers[i]) - int(shesterenki[position + 1]))))
			else:
				otvet+=minus(int(abs((int(Numbers[i]) - int(shesterenki[position + 1])))))
		else:
			otvet+=minus(abs(abs(0 - int(shesterenki[position + 1])) + abs(int(Numbers[i]) -10 )))
		shesterenki[position + 1]=Numbers[i]
		position+=1
	if choise == here2:
		minhere2 = ( (2 + abs(int(Numbers[i]) - int(shesterenki[position + 2]))) , 2 +  abs(abs(0 - int(shesterenki[position + 2])) + abs(int(Numbers[i]) -10 )))
		otvet+=">>"
		if minhere2 == abs(int(Numbers[i]) - int(shesterenki[position + 2])):
			if (int(Numbers[i]) - int(shesterenki[position + 2])) > 0:
				otvet+=plus(int((int(Numbers[i]) - int(shesterenki[position + 2]))))
			else:
				otvet+=minus(int(abs((int(Numbers[i]) - int(shesterenki[position + 2])))))
		else:
			otvet+=minus(abs(abs(0 - int(shesterenki[position + 2])) + abs(int(Numbers[i]) -10 )))
		shesterenki[position + 2]=Numbers[i]
		position+=2
	if choise == here3:
		minhere3 = ( (1 + abs(int(Numbers[i]) - int(shesterenki[position + 3]))) , 1 +  abs(abs(0 - int(shesterenki[position + 3])) + abs(int(Numbers[i]) -10 )))
		otvet+=">>>"
		if minhere3 == abs(int(Numbers[i]) - int(shesterenki[position + 3])):
			if (int(Numbers[i]) - int(shesterenki[position + 3])) > 0:
				otvet+=plus(int((int(Numbers[i]) - int(shesterenki[position + 3]))))
			else:
				otvet+=minus(int(abs((int(Numbers[i]) - int(shesterenki[position + 3])))))
		else:
			otvet+=minus(abs(abs(0 - int(shesterenki[position + 3])) + abs(int(Numbers[i]) -10 )))
		shesterenki[position + 3]=Numbers[i]
		position+=3
	if choise == here4:
		minhere4 = ( (1 + abs(int(Numbers[i]) - int(shesterenki[position + 4]))) , 1 +  abs(abs(0 - int(shesterenki[position + 4])) + abs(int(Numbers[i]) -10 )))
		otvet+= ">>>>"
		if minhere4 == abs(int(Numbers[i]) - int(shesterenki[position + 4])):
			if (int(Numbers[i]) - int(shesterenki[position + 4])) > 0:
				otvet+=plus(int((int(Numbers[i]) - int(shesterenki[position + 4]))))
			else:
				otvet+=minus(int(abs((int(Numbers[i]) - int(shesterenki[position + 4])))))
		else:
			otvet+=minus(abs(abs(int(0 - int(shesterenki[position +4]))) + abs(int(Numbers[i]) -10 )))
		shesterenki[position + 4]=Numbers[i]
		position+=4
	if choise == here5:
		minhere5 = ( (1 + abs(int(Numbers[i]) - int(shesterenki[position + 5]))) , 1 +  abs(abs(0 - int(shesterenki[position + 5])) + abs(int(Numbers[i]) -10 )))
		otvet+=">>>>>"
		if minhere5 == abs(int(Numbers[i]) - int(shesterenki[position + 5])):
			if (int(Numbers[i]) - int(shesterenki[position])) > 0:
				otvet+=plus(int((Numbers[i]) - int(shesterenki[position + 5])))
			else:
				otvet+=minus(int(abs((int(Numbers[i]) - int(shesterenki[position + 5])))))
		else:
			otvet+=minus(abs(abs(0 - int(shesterenki[position + 5])) + abs(int(Numbers[i]) -10 )))
		shesterenki[position + 5]=Numbers[i]
		position+=5
	if choise == here_1:
		minhere_1 = ( (1 + abs(int(Numbers[i]) - int(shesterenki[position - 1]))) , 1 +  abs(abs(0 - int(shesterenki[position - 1])) + abs(int(Numbers[i]) -10 )))
		otvet+= "<"
		if minhere_1 == abs(int(Numbers[i]) - int(shesterenki[position - 1])):
			if (int(Numbers[i]) - int(shesterenki[position - 1])) > 0:
				otvet+=plus(int((int(Numbers[i]) - int(shesterenki[position - 1]))))
			else:
				otvet+=minus(int(abs((int(Numbers[i]) - int(shesterenki[position - 1])))))
		else:
			otvet+=minus(abs(abs(0 - int(shesterenki[position - 1])) + abs(int(Numbers[i]) -10 )))
		shesterenki[position - 1]=Numbers[i]
		position-=1
	if choise == here_2:
		minhere_2 = ( (1 + abs(int(Numbers[i]) - int(shesterenki[position - 2]))) , 1 +  abs(abs(0 - int(shesterenki[position - 2])) + abs(int(Numbers[i]) -10 )))
		otvet+= "<<"
		if minhere_2 == abs(int(Numbers[i]) - int(shesterenki[position - 2])):
			if (int(Numbers[i]) - int(shesterenki[position - 2])) > 0:
				otvet+=plus(int((int(Numbers[i]) - int(shesterenki[position - 2]))))
			else:
				otvet+=minus(int(abs((int(Numbers[i]) - int(shesterenki[position - 2])))))
		else:
			otvet+=minus(abs(abs(0 - int(shesterenki[position - 2])) + abs(int(Numbers[i]) -10 )))
		shesterenki[position - 2]=Numbers[i]
		position-=2
	if choise == here_3:
		minhere_3 = ( (1 + abs(int(Numbers[i]) - int(shesterenki[position - 3]))) , 1 +  abs(abs(0 - int(shesterenki[position - 3])) + abs(int(Numbers[i]) -10 )))
		otvet+= "<<<"
		if minhere_3 == abs(int(Numbers[i]) - int(shesterenki[position - 3])):
			if (int(Numbers[i]) - int(shesterenki[position - 3])) > 0:
				otvet+=plus(int((int(Numbers[i]) - int(shesterenki[position - 3]))))
			else:
				otvet+=minus(int(abs((int(Numbers[i]) - int(shesterenki[position - 3])))))
		else:
			otvet+=minus(abs(abs(0 - int(shesterenki[position - 3])) + abs(int(Numbers[i]) -10 )))
		shesterenki[position - 3]=Numbers[i]
		position-=3
	if choise == here_4:
		minhere_4 = ( (1 + abs(int(Numbers[i]) - int(shesterenki[position - 4]))) , 1 +  abs(abs(0 - int(shesterenki[position - 4])) + abs(int(Numbers[i]) -10 )))
		otvet+="<<<<"
		if minhere_4 == abs(int(Numbers[i]) - int(shesterenki[position - 4])):
			if (int(Numbers[i]) - int(shesterenki[position - 4])) > 0:
				otvet+=plus(int((int(Numbers[i]) - int(shesterenki[position - 4]))))
			else:
				otvet+=minus(int(abs((int(Numbers[i]) - int(shesterenki[position - 4])))))
		else:
			otvet+=minus(abs(abs(0 - int(shesterenki[position - 4])) + abs(int(Numbers[i]) -10 )))
		shesterenki[position - 4]=Numbers[i]
		position-=4
	if choise == here_5:
		minhere_5 = ( (1 + abs(int(Numbers[i]) - int(int(shesterenki[position - 5])))) , 1 +  abs(abs(0 - int(int(shesterenki[position - 5]))) + abs(int(Numbers[i]) -10 )))
		otvet+="<<<<<"
		if minhere_5 == abs(int(Numbers[i]) - int(int(shesterenki[position - 5]))):
			if (int(Numbers[i]) - int(int(shesterenki[position - 5]))) > 0:
				otvet+=plus(int((int(Numbers[i]) - int(int(shesterenki[position - 5])))))
			else:
				otvet+=minus(int(abs((int(Numbers[i]) - int(int(shesterenki[position - 5]))))))
		else:
			otvet+=minus(abs(abs(0 - int(int(shesterenki[position - 5]))) + abs(int(Numbers[i]) -10 )))
		shesterenki[position - 5]=Numbers[i]
		position-=5
print(otvet)
