from .data_ready import ready
from .update_alias import update_alias
from .update_trains import convert_trains

if __name__ == "__main__":
    ready()
    convert_trains()
    update_alias()
