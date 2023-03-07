# Find out the mean value of subject marks of student
input_num = int(input())
subject_marks = {}
for num in range(input_num):
  name, *line = input().split()
  scores = list(map(float, line))
  subject_marks[name] = scores
query = input()
mean_value = sum(subject_marks[query]) / len(subject_marks[query])
print(print(f"{mean_value:.2f}"))
