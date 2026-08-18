import pandas
import consts
from os.path import exists

file_name = consts.SAVE_FILE

def read_from_database():
    dataframe = pandas.read_csv(file_name,index_col='slot') #לקרוא בקובץ את העמודות לפי המספר של המקשים
    print(f"loaded {file_name}!")
    return dataframe


def create_database():
    dataframe = pandas.DataFrame(columns=['slot','game_data']) # אם אין את המקש, זה יצור שני עמודות חדשות אליו הוא יכניס את המידע החד ש
    dataframe.set_index('slot',inplace=True)
    dataframe.to_csv(file_name) # לשמור את המדיכ בתוך הקובץ
    print(f"Created New Dataframe")
    return dataframe


def load_game(slot):
    dataframe = read_from_database()

    if slot in dataframe.index: # אם אחד המקשים נמצא כבר
        data = dataframe.loc[slot, "game_data"] # שימצא את המידע
        print(f"loaded save from {slot}")
        data = eval(data) # לוקח סטרינג והופך אותו לפונקציה בפייתון
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