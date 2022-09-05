import cgi
import cgitb
cgitb.enable()
# print('Content-Type: text/plain')
print('')
# print('Hello World!')

# print("This line will be printed.")
# import cgi
# import cgitb
# cgitb.enable()
# print('Content-Type: text/plain')
# print('')
# print('Hello World!')

# print("This line will be printed.")

filepath = './microhobby/code1.mh'

with open('./index.html', 'r') as file :
    filedata = file.read()
    filedata = filedata.replace(' active', '')
with open('./index.html', 'w') as file:
    file.write(filedata)
    print("index.html reset to no active option")
    # print(lines)

cnt = 1
with open(filepath) as file:
    for line in file:
        print(line.rstrip())
        line = line.replace(";", "")
        lines = line.split()
        print(lines)
        # for x in lines:
        #     print(x)
        # blink_input = "blink = 1"
        if lines[2] == '1':
            # print("blink = 1")
            with open('./index.html', 'r') as file :
                filedata = file.read()
                filedata = filedata.replace('class="myButton1"', 'class="myButton1 active"')
            with open('./index.html', 'w') as file:
                file.write(filedata)
            print("index.html modified with respect to blink = 1")
            cnt += 1
        elif lines[2] == '2':
            # print("blink = 2")
            with open('./index.html', 'r') as file :
                filedata = file.read()
                filedata = filedata.replace('class="myButton2"', 'class="myButton2 active"')
            with open('./index.html', 'w') as file:
                file.write(filedata)
            print("index.html modified with respect to blink = 2")
            cnt += 1
        elif lines[2] == '3':
            # print("blink = 3")
            with open('./index.html', 'r') as file :
                filedata = file.read()
                filedata = filedata.replace('class="myButton3"', 'class="myButton3 active"')
            with open('./index.html', 'w') as file:
                file.write(filedata)
            print("index.html modified with respect to blink = 3")
            cnt += 1
        elif lines[2] == '4':
            # print("blink = 4")
            with open('./index.html', 'r') as file :
                filedata = file.read()
                filedata = filedata.replace('class="myButton4"', 'class="myButton4 active"')
            with open('./index.html', 'w') as file:
                file.write(filedata)
            print("index.html modified with respect to blink = 4")
            cnt += 1
        elif lines[2] == '5':
            # print("blink = 5")
            with open('./index.html', 'r') as file :
                filedata = file.read()
                filedata = filedata.replace('class="myButton5"', 'class="myButton5 active"')
            with open('./index.html', 'w') as file:
                file.write(filedata)
            print("index.html modified with respect to blink = 5")
            cnt += 1
        else:
            print("blink number not available!")
        

# filepath = 'code1.mh'
# with open(filepath) as fp:
#   line = fp.readline()
#   cnt = 1
#   while line:
#       print("Line {}: {}".format(cnt, line.strip()))
#       line = fp.readline()
#       if line in "blink = 1;":
#           print(line)
#           lines = line.split()
#           print(lines)
#           if lines[2] == 1:
#               # Read in the file
#               with open('index.html', 'r') as file :
#                   filedata = file.read()
#
#               # Replace the target string
#               filedata = filedata.replace('class="myButton1"', 'class="myButton1 active"')
# 
#               # Write the file out again
#               with open('index.html', 'w') as file:
#                   file.write(filedata)
#           print("blink = 1 found")
#           cnt += 1
#       else:
#           print("Not found!")
print("Number of lines executed: ", cnt - 1)
