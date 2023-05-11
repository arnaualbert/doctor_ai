import os


def create_directory(path: str):
    """
    Create a directory with the given path if it doesn't already exist
    """
    if not os.path.isdir(path):
        os.mkdir(path)

def create_tools_directory():
    create_directory(TOOLS_PATH)
    create_directory(CDSEXT)
    create_directory(GB2FASTA)
    create_directory(GBLALIGN)
    create_directory(LCLALIGN)
    create_directory(AIPICS)
    create_directory(DNATORNA)
    create_directory(DNATORNA)
    create_directory(RANDOM_SEQ)
    create_directory(SPLIT_FASTA)
    create_directory(COMPLEMENTARY_FASTA)


path = os.getcwd()
TOOLS_DIRNAME = "tools_files"
TOOLS_PATH = os.path.join(path, TOOLS_DIRNAME)

COMPLEMENTARY_FASTA = os.path.join(TOOLS_PATH, "complementary_one")
GB2FASTA     = os.path.join(TOOLS_PATH, "gb2fasta")
LCLALIGN     = os.path.join(TOOLS_PATH, "localAlign")
AIPICS       = os.path.join(TOOLS_PATH, "pics")
GBLALIGN     = os.path.join(TOOLS_PATH, "globalAlign")
DNATORNA     = os.path.join(TOOLS_PATH, "dnatorna")
DNATOPROTEIN = os.path.join(TOOLS_PATH, "dnaprotein")
RANDOM_SEQ   = os.path.join(TOOLS_PATH, "randomseqs")
SPLIT_FASTA  = os.path.join(TOOLS_PATH, "splits")
CDSEXT       = os.path.join(TOOLS_PATH, "cdsext")
