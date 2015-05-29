i = 0
j = 0
k = 0
ite = 0

STEPVAL = 128
for x in range (0, 3) :
	j = 0
	for y in range (0, 3) :
		k = 0
		for z in range (0, 3) :
			if i == 256 :
				i = 255
			if j == 256 :
				j = 255
			if k == 256 :
				k = 255
			print ("\"c64col[%d] = vec3(%d.0,%d.0,%d.0);\"," % (ite, i, j, k))
			k = k + STEPVAL
			ite = ite + 1
		j = j + STEPVAL
	i = i + STEPVAL