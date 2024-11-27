
my_dict = {'banana': 3, 'apple': 1, 'cherry': 2, 'date': 4}
print("Original dictionary:", my_dict)
asc_sorted_dict = dict(sorted(my_dict.items()))
print("Ascending order:", asc_sorted_dict)
desc_sorted_dict = dict(sorted(my_dict.items(), reverse=True))
print("Descending order:", desc_sorted_dict)
