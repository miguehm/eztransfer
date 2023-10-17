import sys

def test(name, *args):
    print(name)

    for i in args:
        print(i)

test(["hola", "que", "tal", "como", "estan?"], "hola")

# a = ["hola", "que", "tal"]
# print(type(a))
# print(type(sys.argv))
