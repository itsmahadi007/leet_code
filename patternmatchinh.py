from typing import List, Union, Any

name_list = []


# @[name]()


def main():
    message = "sa @ sdsaas @[name](1) kcnldsd @[name]() askjcasc"

    key = loop_count = 0
    name_list = []
    while key <= len(message) - 1:
        loop_count += 1
        # print("I " + str(key))
        if message[key] == "@" and message[key + 1] == "[":
            name = ""
            j_count: int = 0
            for j in range(key, len(message)):
                loop_count += 1
                j_count += 1
                # print("J " + str(j_count))
                if message[j] != ")":
                    name = name + message[j]
                else:
                    name = name + message[j]
                    name_list.append(name)

                    key = key + j_count

                    break

        key += 1

    print("len " + str(len(message)))
    print(message)
    print(loop_count)
    for e in name_list:
        print(e)
        message = message.replace(e, '')

    print(message)
    print(name_list)


main()
