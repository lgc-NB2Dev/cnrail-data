import json

from ..base.const import ALIAS_FILE, TRAIN_DATA_FILE


def update_alias():
    train_data_lines = TRAIN_DATA_FILE.read_text("UTF-8").splitlines()
    train_no_lists = [line.split("\t")[6] for line in train_data_lines]
    train_alias = []
    for item in train_no_lists:
        for sth in item.split("#"):
            if len(splits := sth.split("/")) <= 1:
                continue
            train_alias.append({splits[0][: -(len(splits[1]))] + splits[1]: splits[0]})
    ALIAS_FILE.write_text(
        json.dumps(train_alias, ensure_ascii=False, indent=4),
        "UTF-8",
    )
