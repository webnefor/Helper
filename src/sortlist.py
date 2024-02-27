import os

PATH = str(os.path.dirname(__file__));

word        = [];
prnce       = [];
exmpl       = [];
trnslte     = [];

GetArray    = [];

def get(path) -> int:

    global GetArray;

    temp = []

    with open(PATH + path, "r") as fls:
        #
        if (not fls):
            return -1;

        reading = fls.read().strip();
        temp = reading.split(";");
        #
        for i in range(len(temp)-1):
            GetArray.append(temp[i]);

    return 0;


def spliter() -> int:

    global word, prnce, exmpl, trnslte, GetArray;
    global LenElemnt;
    LenElemnt = 4;
    for i in range(0, len(GetArray)):
        word.append(GetArray[i].split(",")[0].strip());
        prnce.append(GetArray[i].split(",")[1].strip());
        exmpl.append(GetArray[i].split(",")[2].strip());
        trnslte.append(GetArray[i].split(",")[3].strip());

    return 0;


def init(path=None) -> int:

    try:
        if (get(path) != 0):
            print("Check your config file");
        spliter();

    except Exception as ms:
        print(ms);

    return 0;
