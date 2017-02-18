import copy

def det(matrix, d):
	if d == 1:
		return matrix[0][0]
	else:
		first = matrix.pop(0)
		subdet = 0
		for i in range(d):
			subn = copy.deepcopy(matrix)
			for j in subn:
				j.pop(i)
			if i % 2 != 0:
				subdet -= first[i] * det(subn, d - 1)
			else:
				subdet += first[i] * det(subn, d - 1)

		return subdet



if __name__ == "__main__":
	mat = []
	n = int(input("Please input the demension of the matrix."))
	for i in range(n):
		mat.append([])
	for i in range(n):
		for j in range(n):
			entry = int(input('Please input an entry.'))
			mat[i].append(entry)
	print(mat)

	d = det(mat, n)
	print(d)
