# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001

# out
# 9.000000

num = float(input('Enter a real number: '))

_, accu = input("Enter the required accuracy '0.0001': ").split(".")
print(f"{num:.{len(accu)}f}")

# задачу сделал после семинара не понял сначала как это работает