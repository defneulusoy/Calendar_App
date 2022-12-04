# 6X7 grid


def print_whole_calendar():
    x = header()
    y = body()
    for ele in y:
        x.append(ele)
    return x

def header():
    row = "-"*148
    middle = "|       Sunday       |       Monday       |       Tuesday      |      Wednesday     |      Thursday      |       Friday       |      Saturday      |"
    whole_header = [row, middle, row]


    return(whole_header)

def body():
    row = "-"*148
    # 20 character limit
    midddle = ["                    ", "|"]
    middddle = ["|", midddle, midddle, midddle, midddle, midddle, midddle, midddle]
    one_section = [middddle,middddle,middddle,middddle,middddle,middddle,row]
    whole_body = one_section*6
    return(whole_body)




z = print_whole_calendar()
for ele in z:
    if isinstance(ele, list):
        for item in ele:
            for thing in item:
                print(thing, end="")
        print("")
    else:
        print(ele)
