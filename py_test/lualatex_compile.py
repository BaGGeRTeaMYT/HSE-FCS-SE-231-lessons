import subprocess

def run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed

with open("D:\\HSE git\\MatStat\\sem.tex", "r", encoding='utf-8') as input_file:
    file = input_file.read().strip().split('\n')

file[19] = r"\usepackage{fontspec}"
file[20] = r"\setmainfont{Times New Roman}"
    
str_ = ""
for i in file:
    str_ += i + '\n'

with open("D:\\HSE git\\py_test\\text.tex", "w", encoding='utf-8') as input_file:
    input_file.write(str_)


run("cd \"d:/HSE git/py_test\" ; lualatex text.tex ; echo \"Compiled file\"")

for i in range(19, 21):
        file[i] = "%" + file[i]
str_ = ""
for i in file:
    str_ += i + '\n'
 
with open("D:\\HSE git\\py_test\\text.tex", "w", encoding='utf-8') as input_file:
    input_file.write(str_)

print("Finished")