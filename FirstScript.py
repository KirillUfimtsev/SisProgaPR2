while True:
    try:
        name: str = input("Введите название файла: ")
        if name == 'end':
            break
        if len(name)<=3:
            print("Длина названия должна быть более 3 символов")
            continue
        if not name.isalpha():
            print("Строка не должна содержать символы или цифры")
            continue
        with open(name + ".txt","w"):
            pass
        print("Файл удачно создан")
    except KeyboardInterrupt:
        exit()
    except:
        print("Ошибка")