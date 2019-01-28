import os

def get_file_extension(fileName):
    dummy, ext = os.path.splitext(fileName)
    return ext

if __name__ == "__main__":
    print(get_file_extension("a.b.c.e"))
    print(get_file_extension("a.b.c.xxx_yyy"))
    print(get_file_extension("a_b_c_d"))
