def Average(L):
    try:
       moy= sum(L)/len(L)
    except ZeroDivisionError as error:
        print (" The list is empty")
    else:
        return moy

students = [
  { "name": "Jose", "marks": [56, 77, 97] },
  { "name": "Rolf", "marks": [45, 80] },
  { "name": "Anna", "marks": [87, 75, 100, 95, 98] },
  { "name": "Mary", "marks": [67, 70, 80] },
  { "name": "Stuart", "marks": [44, 55] },
  { "name": "Sophie", "marks": [86, 90, 100, 100] },
]
L= [  Average(student['marks']) for student in students]

print( Average(L))


