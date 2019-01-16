import random

studentID = int(input("Please enter your student ID: "))

categories = [
    'acidic',
    'alcohol',
    'aliphatic',
    'aromatic',
    'basic',
    'charged',
    'hydrophobic',
    'hydrophilic',
    'polar',
    'small',
    'tiny',
    'turnlike',
]
random.seed(studentID)
print(random.sample(categories, 1)[0])