messages = ["Привет", "Давай", "До свидания"]
sent_messages = []


def show_messages(mes):
    for val in mes:
        print(val)


show_messages(messages)


def send_messages(mes):
    mes.reverse()
    while mes:
        tmp = mes.pop()
        sent_messages.append(tmp)
        print(tmp)


print(messages)
print(sent_messages)
send_messages(messages[:])
print(messages)
print(sent_messages)
