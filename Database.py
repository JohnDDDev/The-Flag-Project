import pandas
import consts
from os.path import exists

file_name = consts.SAVE_FILE

def read_from_database():
    dataframe = pandas.read_csv(file_name,index_col='slot')
    print(f"loaded {file_name}!")
    return dataframe


def create_database():
    dataframe = pandas.DataFrame(columns=['slot','game_data'])
    dataframe.set_index('slot',inplace=True)
    dataframe.to_csv(file_name)
    print(f"Created New Dataframe")
    return dataframe


def load_game(slot):
    dataframe = read_from_database()

    if slot in dataframe.index:
        data = dataframe.loc[slot, "game_data"]
        print(f"loaded save from {slot}")
        data = eval(data)
        return data
    else:
        print(f"no save founded on slot {slot}")
        return None

def save_game(slot, data):
    dataframe = read_from_database()

    dataframe.loc[slot] = str(data)
    dataframe.to_csv(file_name)
    print(slot)

if not exists(file_name):
    create_database()