def rearrange_in_place(arr):
    i = 0
    while i < len(arr):
        # The correct value for index i should be i
        # If the current value is not in its correct spot, swap it
        correct_index = arr[i]

        if arr[i] != arr[correct_index]:
            # Manual swap: move arr[i] to its correct home
            arr[i], arr[correct_index] = arr[correct_index], arr[i]
        else:
            # If it's already correct, move to the next index
            i += 1
    return arr


# Input
my_array = [3, 0, 1, 2, 4, 8, 5, 7, 6]

# Execution
rearrange_in_place(my_array)
print(f"Result: {my_array}")
