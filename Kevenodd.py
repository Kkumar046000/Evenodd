import random

while True:
    print("\033[{}m{}Created by Karan".format(random.randint(31, 36), ""))
    print("\033[{}m{}⊛✴✹❋❀✿✽❁✺✻✼✾".format(random.randint(31, 36), ""))
    print("\033[{}m{}Hello Guys, I'm Karan & This is my Second Project in Python, I Hope you Like it...!!!".format(random.randint(31, 36), ""))
    print("\033[{}\nConnect with me:\n".format(random.randint(31, 36)))
    print("\033[{}m{}Instagram: https://www.instagram.com/kkumar04600/".format(random.randint(31, 36), ""))
    print("\033[{}m{}Facebook: https://www.facebook.com/kkumar04600/".format(random.randint(31, 36), ""))
    print("\033[{}m{}Github: https://github.com/kkumar046000\n".format(random.randint(31, 36), ""))
    num = int(input("\033[{}mEnter any No. : ".format(random.randint(31, 36))))
    if num == 0:
        break
    if num % 2 == 0:
        print("\033[{}m{} is an Even No.".format(random.randint(31, 36), num))
    else:
        print("\033[{}m{} is an Odd No.".format(random.randint(31, 36), num))
