#find the longest and shortest meaning in a dictionary
dict1={'piece':'portion of an object or of material,produced by cutting',
       'patch':'a piece of cloth or other material used to mend or strengthen a torn or weak point',
       'area':'a region or part of a town,a country,or the world',
       'visit':'go to see and spend time with (someone)',
       'with':'having or possessing',
       'small':'less than normal'}
keys=list(dict1.keys())
values=list(dict1.values())

lengths=[len(x) for x in values]
max_len=max(lengths)
min_len=min(lengths)

max_index=lengths.index(max_len)
min_index=lengths.index(min_len)

print('max',keys[max_index],values[max_index])
print('min',keys[min_index],values[min_index])
