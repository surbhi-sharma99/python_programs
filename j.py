


table = [ [ j * i for j in range(1,11) ]  for i in range(1,11)  ]


for i in table:

	for j in i:

		print(str(j).zfill(2)   , end=" ")

	print("")
