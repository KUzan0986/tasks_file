
dict_files = {}
for i in range(3):

    with open(f"{i+1}.txt", encoding="utf-8") as file:

        stri = f"{file.name}\n"
        for ic, l in enumerate(file):
            pass
        dict_files[file.name] = ic+1


sorted_values = sorted(dict_files.values())
sorted_dict = {}

for i in sorted_values:
    for k in dict_files.keys():
        if dict_files[k] == i:
            sorted_dict[k] = dict_files[k]
            break
print(sorted_dict)

f = open("result.txt", "w")
f.close()
for i in sorted_dict:
    with open("result.txt", "a") as result:
        with open(i, encoding="utf-8") as file:
            result.write(f"{i}\n{sorted_dict[i]} \n")
            result.write(f"{file.read()}".strip())
            result.write("\n")