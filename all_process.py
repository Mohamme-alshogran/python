# input 3 numbers
# ouput sum sub devied mult


# input num1 num2 num3 ... done
# cast num1 num2 num3 to float ... done
# caluclate sum .. done
# culcalte sub ... done
# caluclate multi ... done
# culcalte devied .. done
# print sum,sub,multi,devied

print("please input first number")
num1 = input()
print("please input second number")
num2 = input()
print("please input thaird number")
num3 = input()

num1 = float(num1)
num2 = float(num2)
num3 = float(num3)

sum = num1 + num2 + num3
sub = num1 - num2 - num3
multi = num1 * num2 * num3
devid = num1 / num2 / num3

print("your sum is = " + str(sum))
print("your sub is = " + str(sub))
print("your multi is = " + str(multi))
print("your devid is = " + str(devid))
