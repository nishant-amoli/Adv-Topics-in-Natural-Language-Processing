#!/local/bin/python3
import sys

#html = input()
html = sys.stdin.read()

htmlStack = []
htmlChList = [char for char in html]
openFlag = 0
commentFlag = 0
buffer = []
closeBuffer = []
flagTemp = 0
prev = ""
cur = ""
index = 0
commentLen = 0

inComment = 0
for i in htmlChList:
    cur = i
    if i == "<":
        if not htmlStack:
            htmlStack.append(i)
            print("<", end="")
        else:
            if htmlStack[-1] == "<":
                print(".", end="")
                openFlag = 1
            else:
                print("<", end="")

    elif i == ">":
        if not htmlStack:
            print(">", end="")
        else:
            if htmlStack[-1] == "<" and commentFlag == 0:
                print(">", end="")
                openFlag = 0
                htmlStack = []
            if commentFlag == 1:
                print(".", end="")

    elif i == "\n":
        print("\n", end="")

    else:
        if not htmlStack:
            print(i, end="")
        else:
            if i == "!":
                if prev == "<" and commentFlag == 0 and openFlag == 0 and htmlChList[index + 1] == "-" \
                        and htmlChList[index + 2] == "-":
                    buffer.append(i)
                elif prev == "<" and commentFlag == 0 and openFlag == 1 and htmlChList[index + 1] == "-" \
                        and htmlChList[index + 2] == "-":
                    print(".", end="")
                    inComment = 1
                else:
                    print(".", end="")
            elif i == "-":
                if buffer:
                    if len(buffer) == 1 and prev == "!" and commentFlag == 0:
                        buffer.append("-")
                    elif len(buffer) == 2 and prev == "-" and commentFlag == 0:
                        buffer.append("-")
                        for j in buffer:
                            print(j, end="")
                        buffer = []
                        commentFlag = 1
                    else:
                        print(".", end="")
                        buffer = []
                else:
                    if htmlChList[index + 1] == "-" and htmlChList[index + 2] == ">":
                        pass
                    elif htmlChList[index - 1] == "-" and htmlChList[index + 1] == ">" and inComment == 0 and commentFlag == 1:
                        print("--", end="")
                        commentFlag = 0
                    else:
                        if inComment == 1:
                            print("..", end="")
                            inComment = 0
                            commentFlag == 0
                        else:
                            print(".", end="")

            elif i == "/":
                if not htmlStack:
                    print("/", end="")
                else:
                    print(".", end="")
            else:
                print(".", end="")
    prev = cur
    index += 1
