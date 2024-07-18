from fake_math import divide as fk_divide
from true_math import divide as tr_divide

result1 = fk_divide(69, 3)
result2 = fk_divide(3, 0)
result3 = tr_divide(49, 7)
result4 = tr_divide(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)