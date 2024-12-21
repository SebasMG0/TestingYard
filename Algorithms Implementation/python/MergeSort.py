def merge_sort(array:list)->list:
	if len(array) == 1: return array

	elif len(array) == 2:
		if array[0]>array[1]:
			temp= array[0]
			array[0]= array[1]
			array[1]= temp

		return array

	else:
		mid= len(array)//2
		return merge (merge_sort(array[0:mid]), merge_sort(array[mid:]))

def merge(left_list:list, right_list:list)->list:
	combined_list= []
	i, j= 0, 0
	final_size = len(left_list) + len(right_list) 

	while i < len(left_list) and j < len(right_list):
		if left_list[i] <= right_list[j]:
			combined_list.append(left_list[i])
			i+=1
		else:
			combined_list.append(right_list[j])
			j+=1

	if i == len(left_list):
			combined_list.extend(right_list[j:])
	elif j == len(right_list):
		combined_list.extend(left_list[i:])
	return combined_list


print(merge_sort(array= [5, 2, 8, 9, 0, 3]))