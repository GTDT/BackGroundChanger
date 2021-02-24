try:
    import os, random, ctypes, threading, time

    os.system('cls')

    path = input("Type in path where your images are: ")
    files = os.listdir(path)

    def ChangeBackground():
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)

        index = random.randrange(0, len(files))
        RandomImage = path + "\\" + files[index]
        ctypes.windll.user32.SystemParametersInfoW(20, 0, RandomImage , 0)

        print(f"""

            Image = {files[index]}
            Path = {path}
            Time = {current_time}

                If you want to exit press [ CTRL+C ]
""")

    Delay = float(input("\n     Set delay between background changes [SECONDS]: "))
    T = True
    while T:
        threading.Thread(target=ChangeBackground).start()
        time.sleep(Delay)

    LoopForChanging()
except:
    pass