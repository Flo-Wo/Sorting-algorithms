"""!/usr/bin/python
-*- coding: UTF-8 -*-
"""


#list to test the algorithms
liste = [3,2,9,6,4,235235,235,357135,568,23562,246,5468,246,2635782,2356246,458,1222,4,5,7,83,233,7,3]

def quicksort(liste):
	k = []
	g = []
	if len(liste) > 0:
		pivot = liste[0]
		for j in range(1, len(liste)):
			element = liste[j]
			if element >= pivot:
				g.append(element)
			else:
				k.append(element)
		ksortiert = quicksort(k)
		gsortiert = quicksort(g)
		lsortiert = ksortiert + [pivot] + gsortiert
	else:
		lsortiert = liste
	return(lsortiert)

def insertionsort(liste):
	sortiert = []
	sortiert.append(liste[0])
	unsorted = liste
	del unsorted[0]
	while len(unsorted)>0:
		element = unsorted[0]
		del unsorted[0]
		for j in range(0, len(sortiert)):
			vgl = sortiert[j]
			if element <= vgl:
				sortiert.insert(j, element)
				break
			elif j == (len(sortiert)-1):
				sortiert.append(element)
	return(sortiert)

def selectionsort(liste):
	unsorted = liste
	sortiert = []
	while len(unsorted) > 0:
		value = unsorted[0]
		for j in range(1, len(unsorted)):
			element = unsorted[j]
			if element < value:
				value = element
		sortiert.append(value)
		unsorted.remove(value)
	return(sortiert)

def bubblesort(liste):
	unsorted = liste
	n = len(unsorted)
	while n >=1:
		for x in range(0, len(unsorted)-1):
			if unsorted[x]>unsorted[x+1]:
				temp = unsorted[x]
				unsorted[x] = unsorted[x+1]
				unsorted[x+1] = temp
		n -= 1
	return(unsorted)

print(bubblesort(liste))
