import matplotlib.pyplot as plt
import ast

f = open('data.txt')
data = f.read()
new_data = ast.literal_eval(data)
for el in new_data:
    labels = [i for i in new_data[el]]
    vals = [new_data[el][i] for i in new_data[el]]
    fi1, ax1 = plt.subplots()
    ax1.set_title(el)
    ax1.pie(vals, labels=labels)
    ax1.axis('equal')
    plt.show()

