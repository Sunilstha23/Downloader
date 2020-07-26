from urllib import request
from tqdm import tqdm


def obtain_data_from_bensound(remotefile):
    with request.urlopen(remotefile) as handler:
        return handler.read()

def save_to_disk(data, filename, directory=".", extension="txt"):
    with open(filename + extension, "wb") as handler:
        handler.write(data)

    print("download completed")
   


