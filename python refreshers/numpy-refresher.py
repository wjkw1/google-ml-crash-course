import numpy as np

def print_var(var):
    for var_name in globals():
        if globals()[var_name] is var:
            print(f"{var_name}: ")
            print(var)
            print() # newline for better readability
            return
    print("Variable not found in globals.")

## Example usages of numpy to create arrays and perform operations

one_dimensional_array = np.array([1.2, 2.4, 3.5, 4.7, 6.1, 7.2, 8.3, 9.5])
print_var(one_dimensional_array)

two_dimensional_array = np.array([[6, 5], [11, 7], [4, 8]])
print_var(two_dimensional_array)

sequence_of_integers = np.arange(5, 12)
print_var(sequence_of_integers)

random_integers_between_50_and_100 = np.random.randint(low=50, high=101, size=(6,))
print_var(random_integers_between_50_and_100)

random_floats_between_0_and_1 = np.random.random((6,))
print_var(random_floats_between_0_and_1)

random_floats_between_2_and_3 = random_floats_between_0_and_1 + 2.0
print_var(random_floats_between_2_and_3)

random_integers_between_150_and_300 = random_integers_between_50_and_100 * 3
print_var(random_integers_between_150_and_300)


## Task 1: Create a Linear Dataset
#Your goal is to create a simple dataset consisting of a single feature and a label as follows:
# - Assign a sequence of integers from 6 to 20 (inclusive) to a NumPy array named feature.
# - Assign 15 values to a NumPy array named label such that:
feature = np.arange(6, 21)
print_var(feature)

label = feature * 3 + 4
print_var(label)
label2 = feature + 1
print_var(label2)
label3 = (label2 + 1) * 10
print_var(label3)

# Generate one random float uniformly distributed over the range[0, 1)]
# Multiply this value by 4, then subtract 2 to produce noise in the range[-2, 2].
noise = (np.random.random([len(label)]) * 4) - 2
print_var(noise)
label = label + noise
print_var(label)
