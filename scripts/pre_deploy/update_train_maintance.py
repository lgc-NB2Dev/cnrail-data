import json

from ..base.const import ADMINISTRATOR_DATA_FILE, MAINTANCE_FILE, TRAIN_DATA_FILE


def upd_train_maintance():
    train_data_lines = TRAIN_DATA_FILE.read_text("UTF-8").splitlines()
    maintance_data = {}
    administrator_data = {
        item["k"].lower(): item["v"]
        for item in json.loads(ADMINISTRATOR_DATA_FILE.read_text("utf-8-sig"))
    }
    for train in train_data_lines:
        train_datas = train.split("\t")
        train_ids = train_datas[6].split("#")
        for train_id in train_ids:
            train_id_split = train_id.split("/")
            maintance_data[train_id_split[0]] = administrator_data[
                train_datas[5].lower()
            ]
    MAINTANCE_FILE.write_text(json.dumps(maintance_data, ensure_ascii=False), "UTF-8")
