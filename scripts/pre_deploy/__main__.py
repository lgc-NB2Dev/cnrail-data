from ..base.const import const_ready
from ._data_ready import ready
from .update_alias import update_alias
from .update_train_maintance import upd_train_maintance
from .update_trains import convert_trains

if __name__ == "__main__":
    # 异步不会写，未来再改好了
    const_ready()
    ready()
    convert_trains()
    update_alias()
    upd_train_maintance()
