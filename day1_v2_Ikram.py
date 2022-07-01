# open the input file
inputFile = open('day1_Ikram.txt', 'r')
# create a list of the data within the file
depths = list(map(int, inputFile.read().splitlines()))
result = 0
size = len(depths)
# create a variable containing the sum of the first three-measurement sliding window
prev_window = sum(depths[:3])
# iterate over the size of the depths file 
for i in range(3, size):
    # calculate the current three-measurement sliding window
        # for the first iteration this would be:
        # curr = [depths 0 + 1 + 2] + [depth 3] - [depth 0] --> curr = depths 1 + 2 + 3
    curr_sum = prev_window + depths[i] - depths[i-3]
    # check if the previous value is lower than the current value and if it is increase count by 1
    if prev_window < curr_sum:
        result += 1 
    # update the prev_window for the next iteration 
    prev_window = curr_sum
# print the count and close the file
print(result)
inputFile.close()

