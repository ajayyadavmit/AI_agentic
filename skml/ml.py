from sklearn.datasets import load_digits
# from mathplotlib.pyplot as pyp

# Now you can load the data
digits = load_digits()
print(digits.data.shape)  # This should print (1797, 64)