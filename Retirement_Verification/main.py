import pandas as pd
from datetime import datetime


def main():

    #User input filename
    print("ВВЕДИТЕ НАЗВАНИЕ EXCEL-ФАЙЛА: ")
    file_name = input()
    df = pd.read_excel(file_name, sheet_name=0)

    # Get the current date
    now = datetime.now()

    # Add a column with the age of each person and round it
    df['Возраст'] = ((now - pd.to_datetime(df['Дата рождения'], format='%d.%m.%Y')).dt.days / 365.25)
    df['Возраст'] = [round(v, 2) for v in df['Возраст']]

    # Set age limit for each gender and disability combination
    age_limits = {('мужской', 'нет'): 63, ('мужской', 'да'): 58, ('женский', 'нет'): 58, ('женский', 'да'): 53}

    # Create filtered dataframe
    df.sort_values(by='Возраст')
    filtered_df_greater = df.loc[df.apply(lambda x: x['Возраст'] >= age_limits[(x['Пол'], x['Инвалидность'])], axis=1)]
    filtered_df_less = df.loc[df.apply(lambda x: x['Возраст'] <= age_limits[(x['Пол'], x['Инвалидность'])], axis=1)]

    # Write our results in file
    with open("Пенсионеры_Список.txt", "w") as file:
        file.write("Список составлене на: " + str(now) + "\n")
        for index, row in filtered_df_greater.iterrows():
            file.write(f"ФИО: {row['ФИО']}, Возраст: {row['Возраст']}, Пол: {row['Пол']}, Инвалидность: {row['Инвалидность']}\n")

    with open("Надо_Оформить_Список.txt", "w") as file:
        file.write("Список составлен на: " + str(now) + "\n")
        for index, row in filtered_df_less.iterrows():
            file.write(f"ФИО: {row['ФИО']}, Возраст: {row['Возраст']}, Пол: {row['Пол']}, Инвалидность: {row['Инвалидность']}\n")

    # Print the name, age, gender and disability of each person
    print(f"\n\t--- ЛЮДИ, КОТОРЫЕ УЖЕ НА ПЕНСИИ ---")
    for index, row in filtered_df_greater.iterrows():
        print(f"ФИО: {row['ФИО']}, Возраст: {row['Возраст']}, Пол: {row['Пол']}, Инвалидность: {row['Инвалидность']}")

    print(f"\n\t--- ЛЮДИ, КОТОРЫХ НАДО ОФОРМИТЬ ---")
    for index, row in filtered_df_less.iterrows():
        print(f"ФИО: {row['ФИО']}, Возраст: {row['Возраст']}, Пол: {row['Пол']}, Инвалидность: {row['Инвалидность']}")

    input("\nЧТОБЫ ВЫЙТИ НАЖМИТЕ ЛЮБУЮ КНОПКУ")

if __name__ == '__main__':
    main()
