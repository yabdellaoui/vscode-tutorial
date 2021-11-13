import os
from pprint import pprint

os.chdir(r"D:\Formation_Python\test_folder")
# print (os.getcwd())

# print (os.listdir(os.getcwd()))

for f in os.listdir(os.getcwd()):
    f_name, f_ext = os.path.splitext(f)
    f_title, f_desc, f_num = f_name.split("-")

    f_title = f_title.strip()
    f_desc  = f_desc.strip()
    f_num   = f_num.strip()[1:].zfill(2)

    new_name = "{}-{}{}".format(f_num,f_title,f_ext)
    os.rename(f, new_name)
    # print("{} - {}{}".format(f_num.split("#")[-1].zfill(2), title.strip(), f_ext))
# pprint(dir(os))

