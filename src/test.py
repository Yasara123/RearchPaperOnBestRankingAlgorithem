import numpy as np
from tabulate import tabulate
from operator import itemgetter, attrgetter
#a = np.array([1, 2, 6, 4, 2, 3, 2])
#u, indices = np.unique(a,  return_counts=True)
#print(u)
#print(indices)
#print(a[indices])

#table = [["Sun",696000,1989100000],["Earth",6371,5973.6],["Moon",1737,73.5],["Mars",3390,641.85]]

#print(tabulate(table))
#sorted()
'''
import operator

def sort_table(table, col=0):
    return sorted(table, key=operator.itemgetter(col))

if __name__ == '__main__':
    mytable = (
        ('Joe', 'Clark', '1989'),
        ('Charlie', 'Babbitt', '1988'),
        ('Frank', 'Abagnale', '2002'),
        ('Bill', 'Clark', '2009'),
        ('Alan', 'Clark', '1804'),
        )
    mytable..__new__('Toe', 'Clark', '2010')
    for row in sort_table(mytable, 2):
        print (row)
'''


student_tuples = [
    ('john', 'D', 15),
    ('jane', 'B', 12),
    ('dave', 'A', 10),
]
student_tuples.insert(3,('Tan', 'C', 25))

print(sorted(student_tuples, key=itemgetter(1)))
student_tuples=sorted(student_tuples, key=itemgetter(1))
print(student_tuples[2])

