import threading


START = "start"
END = "end"


def work(event, index):
    print(START + ": " + str(index))
    event.wait()
    print(END)


def threading_main():
    event = threading.Event()
    for i in range(5):
        t = threading.Thread(target=work, args=(event, i))
        t.start()

    # stop all thread
    event.clear()
    start_flag = input("Want end thread?")
    # print(start_flag)
    if start_flag:
        event.set()


if __name__ == '__main__':
    threading_main()

