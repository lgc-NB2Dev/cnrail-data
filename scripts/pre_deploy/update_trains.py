import json

from ..base.const import ADMINISTRATOR_DATA_FILE, TRAIN_DATA_FILE, TRAIN_FILE


def convert_trains():
    train_data_lines = TRAIN_DATA_FILE.read_text("UTF-8").splitlines()
    train_data = []
    administrator_data = {
        item["k"].lower(): item["v"]
        for item in json.loads(ADMINISTRATOR_DATA_FILE.read_text("utf-8-sig"))
    }
    for train in train_data_lines:
        train_datas = train.split("\t")
        # train_ids = train_datas[6].split("#")
        # train_no = []
        # for train_id in train_ids:
        #     train_id_split = train_id.split("/")
        #     train_no.append(train_id_split[0])
        #     if len(train_id_split) > 1:
        #         train_no.append(
        #             train_id_split[0][: -(len(train_id_split[1]))] + train_id_split[1],
        #         )
        # train_data.append(
        #     {
        #         "running_start": train_datas[0],
        #         "running_end": train_datas[1],
        #         "emu_note": train_datas[4],
        #         "administrator": administrator_data[train_datas[5].lower()],
        #         "train_no": train_no,
        #     },
        # )
        train_data.append(
            {
                "running_start": train_datas[0],
                "running_end": train_datas[1],
                "emu_note": train_datas[4],
                "administrator": administrator_data[train_datas[5].lower()],
                "train_no": train_datas[6],
            },
        )
    TRAIN_FILE.write_text(json.dumps(train_data, ensure_ascii=False), "UTF-8")
