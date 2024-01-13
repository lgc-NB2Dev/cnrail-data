from pathlib import Path

SCRIPT_PATH = Path(__file__).parent.parent
ROOT_PATH = SCRIPT_PATH.parent

TMP_PATH = ROOT_PATH / "tmp"
TMP_FILE = TMP_PATH / "data.zip"
TRAIN_DATA_FILE = TMP_PATH / "000_jlb.txt"
ADMINISTRATOR_DATA_FILE = TMP_PATH / "000_ddj.json"

DATA_PATH = ROOT_PATH / "data"
TRAIN_FILE = DATA_PATH / "train.json"
ALIAS_FILE = DATA_PATH / "alias.json"
