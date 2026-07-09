marks=[85,90,76,95,88,91,67,99]
maximum=marks[0]
minimum=marks[0]
for i in marks:
    if(i>maximum):
        maximum=i
    if(i<minimum):
        minimum=i
print(f"Maximun: {maximum}")
print(f"Minimum: {minimum}")