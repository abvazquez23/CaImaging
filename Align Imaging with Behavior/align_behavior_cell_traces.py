import pandas as pd
from numpy import *
from operantanalysis import *
from tkinter import filedialog, Tk


def choose_file():
    project = Tk()
    project.filename = filedialog.askopenfilename(initialdir="/", title="Choose an IDPS CSV file",
                                                  filetypes=[("CSV", "*.csv")])
    file = project.filename
    print("IDPS File:" + file)
    return file


def parse_csv():
    csv_file = open(choose_file())

    return csv_file


def load_operant_file():
    project = Tk()
    project.filename = filedialog.askopenfilename(initialdir="/", title="Choose a Behavioral Operant File",
                                                  filetypes=[("all files", "*.")])
    operant_file = project.filename
    print("Operant File:" + operant_file)
    file = load_file(operant_file)
    file_info = extract_info_from_file(file, 500)
    return file_info


def align_lists():
    behavior_file = array(load_operant_file())
    event_detection_file = parse_csv()
    time_codes = list(map(float, behavior_file[0]))
    behaviors = list(behavior_file[1])
    df = pd.read_csv(event_detection_file, low_memory=False)
    df2 = pd.DataFrame(list(zip(time_codes, behaviors)), columns=['Time Codes', 'Behavior'])
    with pd.option_context('display.max_rows', 795, 'display.max_columns', 2):
        print(df2)

    df.columns = df.columns.astype(str)
    df.insert(df.shape[1], 'Raw Behavioral Codes', NaN)
    df.insert(df.shape[1], 'Reward Presentation', NaN)
    df.insert(df.shape[1], 'Head In', NaN)
    df.insert(df.shape[1], 'Reward Retrieval', NaN)
    df.insert(df.shape[1], 'ITI', 1)
    df.insert(df.shape[1], 'Lever Press', NaN)
    df.insert(df.shape[1], 'Go Trial', NaN)
    df.insert(df.shape[1], 'Successful Go Trial', NaN)
    df.insert(df.shape[1], 'No Go Trial', NaN)
    df.insert(df.shape[1], 'Successful No Go Trial', NaN)
    df.insert(df.shape[1], 'Unsuccessful No Go Trial', NaN)
    df.insert(df.shape[1], 'Unsuccessful Go Trial', NaN)

    cell_times = list(map(float, df[' '][1:]))
    print(cell_times)
    print(time_codes)
    print(behaviors)

    for index, value in enumerate(cell_times):  # raw behavioral codes
        for index_2, value_2 in enumerate(time_codes):
            if round(value_2, 1) == value:
                df.iloc[index + 1, [-12]] = behaviors[index_2]

    for index, value in enumerate(cell_times):  # raw behavioral codes
        for index_2, value_2 in enumerate(time_codes):
            if round(value_2, 1) == value:

                if behaviors[index_2] == 'EndSession':
                    break

                if round(time_codes[index_2], 1) == round(time_codes[index_2 + 1], 1):
                    x = 1
                    n = [behaviors[index_2]]
                    print(True)
                    while True:

                        print(n)
                        n.append(behaviors[index_2 + x])
                        separator = ','
                        df.iloc[index + 1, [-12]] = separator.join(n)
                        print(separator.join(n))
                        print(x)
                        x += 1
                        print(x)
                        print(round(time_codes[index_2], 1))
                        if behaviors[index_2 + 1] == 'EndSession':
                            break
                        if round(time_codes[index_2], 1) != round(time_codes[index_2 + x], 1):
                            break
                        print(x)

    for index, value in enumerate(cell_times):  # raw behavioral codes
        for index_2, value_2 in enumerate(time_codes):
            if round(value_2, 1) == value:

                if behaviors[index_2 + 1] == 'EndSession':
                    break

                if round(time_codes[index_2], 1) == round(time_codes[index_2 + 2], 1):
                    x = 1
                    n = [behaviors[index_2]]
                    print(True)
                    while True:

                        print(n)
                        n.append(behaviors[index_2 + x])
                        separator = ','
                        df.iloc[index + 1, [-12]] = separator.join(n)
                        print(separator.join(n))
                        print(x)
                        x += 1
                        print(x)
                        print(round(time_codes[index_2], 1))
                        if round(time_codes[index_2], 1) != round(time_codes[index_2 + x], 1):
                            break
                        print(x)

    for index, value in enumerate(cell_times):
        for index_2, value_2 in enumerate(time_codes):
            if round(value_2, 1) == value:
                if behaviors[index_2] == 'DipOn':  # reward presentation
                    df.iloc[index + 1, [-11]] = 1
                    x = 1
                    n = []
                    while True:
                        df.iloc[index + x, [-11]] = 1
                        x += 1
                        t = round(float(df2.iat[index_2 + x, 0]), 1)
                        try:
                            n.append(cell_times.index(t))
                        except ValueError:
                            pass
                        try:
                            for y in list(range(n[0], n[-1] + 1)):
                                df.iloc[y + 1, [-11]] = 1
                            df.iloc[n[-1] + 1, [-11]] = 1
                        except ValueError:
                            pass
                        if behaviors[index_2 + x] == 'DipOff':
                            break

                    if behaviors[index_2] == 'DipOn' and behaviors[index_2 + 1] != 'DipOff' \
                            and behaviors[index_2 - 1] != 'PokeOn1':  # reward retrieval
                        x = 1
                        n = []
                        while True:
                            x += 1
                            t = round(float(df2.iat[index_2 + x, 0]), 1)
                            try:
                                n.append(cell_times.index(t))
                            except ValueError:
                                pass
                            try:
                                for y in list(range(n[0], n[-1] + 1)):
                                    df.iloc[y + 1, [-9]] = 0
                                df.iloc[n[-1] + 1, [-9]] = 1
                            except ValueError:
                                pass
                            if behaviors[index_2 + x] == 'PokeOn1':
                                break

    for index, value in enumerate(cell_times):
        for index_2, value_2 in enumerate(time_codes):
            if round(value_2, 1) == value:
                if behaviors[index_2] == 'SuccessfulNoGoTrial':  # Successful No Go  Trial
                    df.iloc[index + 1, [-3]] = 1

    for index, value in enumerate(cell_times):
        for index_2, value_2 in enumerate(time_codes):
            if round(value_2, 1) == value:
                if behaviors[index_2] == 'SuccessfulGoTrial':  # Successful Go Trial
                    df.iloc[index + 1, [-5]] = 1

    for index, value in enumerate(cell_times):
        for index_2, value_2 in enumerate(time_codes):
            if round(value_2, 1) == value:
                if behaviors[index_2] == 'LPressOn':  # lever press
                    df.iloc[index + 1, [-7]] = 1

    for index, value in enumerate(cell_times):
        for index_2, value_2 in enumerate(time_codes):
            if round(value_2, 1) == value:
                if behaviors[index_2] == 'PokeOn1' and behaviors[index_2 + 1] == 'DipOn':  # reward retrieval
                    i = cell_times.index(round(float(df2.iat[index_2 + 3, 0]), 1))
                    df.iloc[i, [-9]] = 1

    for index, value in enumerate(cell_times):
        for index_2, value_2 in enumerate(time_codes):
            if round(value_2, 1) == value:
                if behaviors[index_2] == 'PokeOn1':  # head in
                    x = 0
                    n = [cell_times.index(round(float(df2.iat[index_2, 0]), 1))]
                    while True:
                        x += 1
                        t = round(float(df2.iat[index_2 + x, 0]), 1)
                        try:
                            n.append(cell_times.index(t))
                            for y in list(range(n[0] + 1, n[-1] + 1)):
                                df.iloc[y, [-10]] = 1
                            df.iloc[n[-1] + 1, [-10]] = 1
                        except ValueError:
                            pass
                        if behaviors[index_2 + x] == 'PokeOff1' or behaviors[index_2 + x] == 'EndSession':
                            break

    for index, value in enumerate(cell_times):
        for index_2, value_2 in enumerate(time_codes):
            if round(value_2, 1) == value:
                if behaviors[index_2] == 'LLeverOn':  # ITI
                    df.iloc[index + 1, [-8]] = 0
                    x = 0
                    n = [cell_times.index(round(float(df2.iat[index_2, 0]), 1))]
                    while True:
                        x += 1
                        t = round(float(df2.iat[index_2 + x, 0]), 1)
                        try:
                            n.append(cell_times.index(t))
                            for y in list(range(n[0] + 1, n[-1] + 1)):
                                df.iloc[y + 1, [-8]] = 0
                            df.iloc[n[-1] + 1, [-8]] = 0
                        except ValueError:
                            pass
                        if behaviors[index_2 + x] == 'LLeverOff':
                            break

    for index, value in enumerate(cell_times):
        for index_2, value_2 in enumerate(time_codes):
            if round(value_2, 1) == value:
                if behaviors[index_2] == 'DipOn':  # ITI
                    df.iloc[index + 1, [-8]] = 0
                    x = 1
                    n = []
                    while True:
                        df.iloc[index + x, [-8]] = 0
                        x += 1
                        t = round(float(df2.iat[index_2 + x, 0]), 1)
                        try:
                            n.append(cell_times.index(t))
                        except ValueError:
                            pass
                        try:
                            for y in list(range(n[0], n[-1] + 1)):
                                df.iloc[y + 1, [-8]] = 0
                            df.iloc[n[-1] + 1, [-8]] = 0
                        except ValueError:
                            pass
                        if behaviors[index_2 + x] == 'DipOff':
                            break

    for index, value in enumerate(cell_times):
        for index_2, value_2 in enumerate(time_codes):
            if round(value_2, 1) == value:
                if behaviors[index_2] == 'HouseLightOff' and behaviors[index_2 + 1] == 'LPressOn':  # Unsuccessful No Go Trial
                    df.iloc[index + 1, [-2]] = 1

    for index, value in enumerate(cell_times):
        for index_2, value_2 in enumerate(time_codes):
            if round(value_2, 1) == value:
                if behaviors[index_2] == 'LLeverOn' and behaviors[index_2 + 1] == 'LLeverOff':  # Unsuccessful Go Trial
                    df.iloc[index + 1, [-1]] = 1

    for index, value in enumerate(cell_times):
        for index_2, value_2 in enumerate(time_codes):
            if round(value_2, 1) == value:
                if behaviors[index_2] == 'LightOn1' and behaviors[index_2 - 1] == 'LLeverOn' \
                        and behaviors[index_2 + 1] == 'HouseLightOff':  # No Go Trial
                    x = 0
                    n = [cell_times.index(round(float(df2.iat[index_2, 0]), 1))]
                    while True:
                        x += 1
                        t = round(float(df2.iat[index_2 + x, 0]), 1)
                        try:
                            n.append(cell_times.index(t))
                            for y in list(range(n[0] + 1, n[-1] + 1)):
                                df.iloc[y + 1, [-4]] = 1
                            df.iloc[n[-1] + 1, [-4]] = 1
                        except ValueError:
                            pass
                        if behaviors[index_2 + x] == 'LLeverOff':
                            break

    for index, value in enumerate(cell_times):
        for index_2, value_2 in enumerate(time_codes):
            if round(value_2, 1) == value:
                if behaviors[index_2] == 'LLeverOn' and behaviors[index_2 + 1] != 'LightOn1':  # Go Trial
                    df.iloc[index + 1, [-6]] = 1
                    x = 0
                    n = [cell_times.index(round(float(df2.iat[index_2, 0]), 1))]
                    while True:
                        x += 1
                        t = round(float(df2.iat[index_2 + x, 0]), 1)
                        try:
                            n.append(cell_times.index(t))
                            for y in list(range(n[0] + 1, n[-1] + 1)):
                                df.iloc[y + 1, [-6]] = 1
                            df.iloc[n[-1] + 1, [-6]] = 1
                        except ValueError:
                            pass
                        if behaviors[index_2 + x] == 'LLeverOff':
                            break

    df.fillna(0, inplace=True)

    with pd.option_context('display.max_rows', 200, 'display.max_columns', 50):
        print(df)

    return df


def output_csv_file():
    df = align_lists()
    project = Tk()
    project.directory = filedialog.askdirectory(initialdir="/", title="Choose an Output Directory")
    output_path = project.directory
    print('File Output:' + output_path)
    df.to_csv(output_path + '/aligned_cell_operant_behavior_df.csv')


output_csv_file()
