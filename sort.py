students = (("Squiward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr Krabs", "C", 78))

#sort method only works for lists.
#sort function works for tuples

age = lambda ages:ages[2]

sorted_students = sorted(students, key = age)

for i in sorted_students:
    print(i)