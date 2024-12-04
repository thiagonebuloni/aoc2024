def file_reaper(file_name: str):
    for line in open(file_name, "r"):
        yield line
