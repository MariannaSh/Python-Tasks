array=[[-38, 19],[5,40],[-7,11],[29,16]]


max_array=0
min_array=0
count_max=0
count_min=0
for i in range(len(array)):
    if max(array[i])>max_array:
        max_array=max(array[i])
        count_max=i
for i in range(len(array)):
    if min(array[i])<min_array:
        min_array=min(array[i])
        count_min=i
print('Max: ',max_array,count_max)
print('Min:', min_array,count_min)
