def swap(num1, num2):
	num3 = num1
	num1 = num2
	num2 = num3
	return(num1, num2)

num1 = input("angka pertama : ")
num2 = input("angka kedua : ")

print("Angka pertama sebelum di Swap : ", num1)
print("Keluar kedua sebelum di swap : ", num2, "\n")

num1,num2 = swap(num1, num2)

print("Setelah di swap angka petama : ", num1)
print("Setelah di swap angka kedua : ", num2)
