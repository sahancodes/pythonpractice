# seq[start:stop:step]
# seq[::]   -> shallow copy of the whole sequence
# seq[::2]  -> every second element
# seq[::-1] -> reverse the sequence
# seq[a:]   -> all elements starting from a
# seq[:b]   -> all elements until b

# for list, tuple, and string, slicing returns a new object

# nums[::2] = [...] This notation is explained below
# nums[::2] selects the even positions (0,2,4,…).
# nums[::2] = [...] fills those positions with your new values.
# The number of new values must match how many positions you’re filling.

# select 20 40 and 60 from the list and create a new list
nums1 = [10,20,30,40,50,60]
every_other = nums1[1::2]
print(every_other)

# reverse the nums list
reversed = nums1[::-1]
print(reversed)

# Put values at even indices in ascending order, and values at odd indices in descending order — without building a new list.
nums2 = [7, 4, 9, 2, 6, 5, 3, 8, 1]

nums2[::2] = sorted(nums2[::2])
nums2[1::2] = sorted(nums2[1::2])
print(nums2)

# Reverse the subsequence at even indices but leave odd indices as-is.
nums3 = [10, 20, 30, 40, 50, 60, 70]
# nums3s = nums3[::2]
# nums3[::2] = nums3s[::-1]

# also similar to
nums3[::2] = nums3[::2][::-1]
print(nums3)

# Split a list into k sequences subsequences using slicing, process them, then reconstruct by slice assignment.
nums4 = [7, 4, 9, 2, 6, 5, 3, 8, 1]
k = 3  #The above list is separated into three groups
# lane1 selects 7,2,3 in steps of three and reverse the order
lane1 = nums4[::3][::-1]
# lane2 selects 4,6,8 starting from first index in steps of three
# Then its sorted in the decending order
lane2 = nums4[1::3]
lane2[::2] = sorted(lane2[::2], reverse=True)
# lane3 selects 9,5,1 in steps of three starting from index 2
# Then rotate lane1 once in the left direction and order must change to 5,1,9
lane3 = nums4[2::3]
print(lane3[:1], lane3[1:])
lane3 =  lane3[1:] + lane3[:1]

print(lane1, lane2, lane3)

nums4[::3] = lane1
nums4[1::3] = lane2
nums4[2::3] = lane3

print(nums4)