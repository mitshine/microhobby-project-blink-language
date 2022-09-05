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