import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data.csv", delimiter = ",", skiprows = 1)

#a)
print("Broj ispitanika: ", data.shape[0])
print("\n")

#b)
persons_height = data[:,1]
persons_weight = data[:,2]
plt.scatter(persons_height, persons_weight, marker = ".")
plt.xlabel("height")
plt.ylabel("weight")
plt.title("b) zadatak")
plt.show()

#c)
persons_height_50 = data[::50,1]
persons_weight_50 = data[::50,2]
plt.scatter(persons_height_50, persons_weight_50, marker = ".")
plt.xlabel("height")
plt.ylabel("weight")
plt.title("c) zadatak")
plt.show()

#d)
print("Minimalna visina skupa: ", persons_height_50.min())
print("Maksimalna visina skupa: ", persons_height_50.max())
print("Prosjecna visina skupa: ", persons_height_50.mean())
print("\n")

#e)
male = (data[:,0] == 1)
female = (data[:,0] == 0)
print("Men")
print(min(data[male,1]))
print(max(data[male,1]))
print(np.mean(data[male,1]))

print("Women")
print(min(data[female,1]))
print(max(data[female,1]))
print(np.mean(data[female,1]))
