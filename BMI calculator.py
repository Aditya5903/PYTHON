#First take height input and weight input
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
#Convert height and weight in float data type
S = float(height)
T = float(weight)
#Then we wil do simple calculation of Body mass index
BMI = (T/(S*S))
#we need our body mass index in integer then we cgange the data type float to integer
print(int(BMI))
