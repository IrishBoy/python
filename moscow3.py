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
f1 = open("3ans.txt",'w')
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
	spisok = [here, here1, here2, here3, here4, here5, here_1, here_2, here_3, here_4, here_5]
	choise = spisok.index(min(spisok))
	if choise == 0:
		H =[abs(int(Numbers[i]) - int(shesterenki[position])) ,abs(abs(0 - int(shesterenki[position])) + abs(int(Numbers[i]) -10 ))]
		minhere = H.index(min(H))
		if minhere == 0:
			if (int(Numbers[i]) - int(shesterenki[position])) > 0:
				otvet+=plus(int((int(Numbers[i]) - int(shesterenki[position]))))
			else:
				otvet+=minus(int(abs((int(Numbers[i]) - int(shesterenki[position])))))
		else:
			otvet+=minus(abs(abs(0 - int(shesterenki[position])) + abs(int(Numbers[i]) -10 )))
		shesterenki[position]=Numbers[i]
		position = position
	if choise == 1:
		H1 = [1 + abs(int(Numbers[i]) - int(shesterenki[position + 1])) , 1 +  abs(abs(0 - int(shesterenki[position + 1])) + abs(int(Numbers[i]) -10 ))]
		minhere1 = H1.index(min(H1))
		otvet+=">"
		if minhere1 == 0:
			if (int(Numbers[i]) - int(shesterenki[position + 1])) > 0:
				otvet+=plus(int((int(Numbers[i]) - int(shesterenki[position + 1]))))
			else:
				otvet+=minus(int(abs((int(Numbers[i]) - int(shesterenki[position + 1])))))
		else:
			otvet+=minus(abs(abs(0 - int(shesterenki[position + 1])) + abs(int(Numbers[i]) -10 )))
		shesterenki[position + 1]=Numbers[i]
		position+=1
	if choise == 2:
		H2 = [2 + abs(int(Numbers[i]) - int(shesterenki[position + 2])) , 2 +  abs(abs(0 - int(shesterenki[position + 2])) + abs(int(Numbers[i]) -10 ))]
		minhere2 = H2.index(min(H2))
		otvet+=">>"
		if minhere2 == 0:
			if (int(Numbers[i]) - int(shesterenki[position + 2])) > 0:
				otvet+=plus(int((int(Numbers[i]) - int(shesterenki[position + 2]))))
			else:
				otvet+=minus(int(abs((int(Numbers[i]) - int(shesterenki[position + 2])))))
		else:
			otvet+=minus(abs(abs(0 - int(shesterenki[position + 2])) + abs(int(Numbers[i]) -10 )))
		shesterenki[position + 2]=Numbers[i]
		position+=2
	if choise == 3:
		H3=[(1 + abs(int(Numbers[i]) - int(shesterenki[position + 3]))) , 1 +  abs(abs(0 - int(shesterenki[position + 3])) + abs(int(Numbers[i]) -10 ))]
		minhere3 = H3.index(min(H3))
		otvet+=">>>"
		if minhere3 == 0:
			if (int(Numbers[i]) - int(shesterenki[position + 3])) > 0:
				otvet+=plus(int((int(Numbers[i]) - int(shesterenki[position + 3]))))
			else:
				otvet+=minus(int(abs((int(Numbers[i]) - int(shesterenki[position + 3])))))
		else:
			otvet+=minus(abs(abs(0 - int(shesterenki[position + 3])) + abs(int(Numbers[i]) -10 )))
		shesterenki[position + 3]=Numbers[i]
		position+=3
	if choise == 4:
		H4 = [1 + abs(int(Numbers[i]) - int(shesterenki[position + 4])) , 1 +  abs(abs(0 - int(shesterenki[position + 4])) + abs(int(Numbers[i]) -10 ))]
		minhere4 = H4.index(min(H4))
		otvet+= ">>>>"
		if minhere4 == 0:
			if (int(Numbers[i]) - int(shesterenki[position + 4])) > 0:
				otvet+=plus(int((int(Numbers[i]) - int(shesterenki[position + 4]))))
			else:
				otvet+=minus(int(abs((int(Numbers[i]) - int(shesterenki[position + 4])))))
		else:
			otvet+=minus(abs(abs(int(0 - int(shesterenki[position +4]))) + abs(int(Numbers[i]) -10 )))
		shesterenki[position + 4]=Numbers[i]
		position+=4
	if choise == 5:
		H5=[1 + abs(int(Numbers[i]) - int(shesterenki[position + 5])) , 1 +  abs(abs(0 - int(shesterenki[position + 5])) + abs(int(Numbers[i]) -10 ))]
		minhere5 = H5.index(min(H5))
		otvet+=">>>>>"
		if minhere5 == 0:
			if (int(Numbers[i]) - int(shesterenki[position])) > 0:
				otvet+=plus(int((Numbers[i]) - int(shesterenki[position + 5])))
			else:
				otvet+=minus(int(abs((int(Numbers[i]) - int(shesterenki[position + 5])))))
		else:
			otvet+=minus(abs(abs(0 - int(shesterenki[position + 5])) + abs(int(Numbers[i]) -10 )))
		shesterenki[position + 5]=Numbers[i]
		position+=5
	if choise == 6:
		H_1 =[1 + abs(int(Numbers[i]) - int(shesterenki[position - 1])) , 1 +  abs(abs(0 - int(shesterenki[position - 1])) + abs(int(Numbers[i]) -10 ))]
		minhere_1 = H_1.index(min(H_1))
		otvet+= "<"
		if minhere_1 == 0:
			if (int(Numbers[i]) - int(shesterenki[position - 1])) > 0:
				otvet+=plus(int((int(Numbers[i]) - int(shesterenki[position - 1]))))
			else:
				otvet+=minus(int(abs((int(Numbers[i]) - int(shesterenki[position - 1])))))
		else:
			otvet+=minus(abs(abs(0 - int(shesterenki[position - 1])) + abs(int(Numbers[i]) -10 )))
		shesterenki[position - 1]=Numbers[i]
		position-=1
	if choise == 7:
		H_2 =[1 + abs(int(Numbers[i]) - int(shesterenki[position - 2])) , 1 +  abs(abs(0 - int(shesterenki[position - 2])) + abs(int(Numbers[i]) -10 ))]
		minhere_2 = H_2.index(min(H_2))
		otvet+= "<<"
		if minhere_2 == 0:
			if (int(Numbers[i]) - int(shesterenki[position - 2])) > 0:
				otvet+=plus(int((int(Numbers[i]) - int(shesterenki[position - 2]))))
			else:
				otvet+=minus(int(abs((int(Numbers[i]) - int(shesterenki[position - 2])))))
		else:
			otvet+=minus(abs(abs(0 - int(shesterenki[position - 2])) + abs(int(Numbers[i]) -10 )))
		shesterenki[position - 2]=Numbers[i]
		position-=2
	if choise == 8:
		H_3=[1 + abs(int(Numbers[i]) - int(shesterenki[position - 3])) , 1 +  abs(abs(0 - int(shesterenki[position - 3])) + abs(int(Numbers[i]) -10 ))]
		minhere_3 = H_3.index(min(H_3))
		otvet+= "<<<"
		if minhere_3 == 0:
			if (int(Numbers[i]) - int(shesterenki[position - 3])) > 0:
				otvet+=plus(int((int(Numbers[i]) - int(shesterenki[position - 3]))))
			else:
				otvet+=minus(int(abs((int(Numbers[i]) - int(shesterenki[position - 3])))))
		else:
			otvet+=minus(abs(abs(0 - int(shesterenki[position - 3])) + abs(int(Numbers[i]) -10 )))
		shesterenki[position - 3]=Numbers[i]
		position-=3
	if choise == 9:
		H_4=[1 + abs(int(Numbers[i]) - int(shesterenki[position - 4])) , 1 +  abs(abs(0 - int(shesterenki[position - 4])) + abs(int(Numbers[i]) -10 ))]
		minhere_4 = H_4.index(min(H_4))
		otvet+="<<<<"
		if minhere_4 == 0:
			if (int(Numbers[i]) - int(shesterenki[position - 4])) > 0:
				otvet+=plus(int((int(Numbers[i]) - int(shesterenki[position - 4]))))
			else:
				otvet+=minus(int(abs((int(Numbers[i]) - int(shesterenki[position - 4])))))
		else:
			otvet+=minus(abs(abs(0 - int(shesterenki[position - 4])) + abs(int(Numbers[i]) -10 )))
		shesterenki[position - 4]=Numbers[i]
		position-=4
	if choise == 10:
		H_5=[1 + abs(int(Numbers[i]) - int(int(shesterenki[position - 5]))) , 1 +  abs(abs(0 - int(int(shesterenki[position - 5]))) + abs(int(Numbers[i]) -10 ))]
		minhere_5 = H_5.index(min(H_5))
		otvet+="<<<<<"
		if minhere_5 == 0:
			if (int(Numbers[i]) - int(int(shesterenki[position - 5]))) > 0:
				otvet+=plus(int((int(Numbers[i]) - int(int(shesterenki[position - 5])))))
			else:
				otvet+=minus(int(abs((int(Numbers[i]) - int(int(shesterenki[position - 5]))))))
		else:
			otvet+=minus(abs(abs(0 - int(int(shesterenki[position - 5]))) + abs(int(Numbers[i]) -10 )))
		shesterenki[position - 5]=Numbers[i]
		position-=5
f1.write(otvet)
f1.close()
