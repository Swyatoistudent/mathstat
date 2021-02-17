result_file = open("result.txt","w")
file_path = "1.txt"
file = open(file_path)
for line in file:
    x = line.split('	')
    print(x)
    for i in x:
        if '\n' not in i:
            result_file.write(i + '\n')
        else:
            result_file.write(i)
result_file.close()
