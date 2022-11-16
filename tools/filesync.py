from doctest import ELLIPSIS_MARKER
import os


def get_folder_content(folder_dir: str, include_folder = False):
    try:
        content = os.listdir(folder_dir)
    except:
        return -1
    relevant_content = []
    if "ignore.filesync" in content:
        return -1
    include = "include.filesync" in content or include_folder
    for c in content:
        if os.path.isdir(folder_dir + "\\" + c):
            sub_content = get_folder_content(folder_dir + "\\" + c, include)
            if not sub_content == -1:
                relevant_content.append((c, sub_content))
                pass
            pass
        elif include and not c == "include.filesync":
            relevant_content.append(c)
    if not relevant_content == []:
        return relevant_content
    else:
        return -1

if __name__ == "__main__":
    work_dir = os.getcwd()
    print(get_folder_content(work_dir + "\\documents"))
    pass

input()