# 1.
# (A)
s = "junyiacademy"
print(s[::-1])

# (B)

# 2.
x = input()
for i in range(1, int(x)+1):
    if (i % 3 != 0 and i % 5 != 0 or i % 15 == 0):
        print(i)

# 3.
"""
作法：三袋個拿三十次，所以每袋拿三十次的筆。
解釋：因中大數法則中央極限定理，超過三十次逼近。
"""

# 4.
"""
三個人個拿三十塊，但是錢本身是這三個人出的，所以不應該再讓每個人多扣三十元。
"""