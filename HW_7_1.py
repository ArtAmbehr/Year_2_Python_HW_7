import os


def group_rename_files(dest_name, num_digits, src_ext, dest_ext, name_range=None):
    
    files = os.listdir()
    
    files = [f for f in files if os.path.isfile(f) and f.endswith(src_ext)]

    if name_range:
        files = [f[name_range[0] - 1:name_range[1]] for f in files]

    count = 1

    
    for file in files:
        
        new_file_name = dest_name + str(count).zfill(num_digits) + dest_ext
        os.rename(file, new_file_name)
        count += 1


group_rename_files("new_file_", 4, ".txt", ".jpg", [3, 6])