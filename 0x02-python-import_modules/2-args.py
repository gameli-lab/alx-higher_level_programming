#!/usr/bin/python3
    def main():
    import sys
    num_args = len(sys.argv) - 1
    if num_args == 0:
        print("{} arguments.".format("0"))
    elif num_args == 1:
        print("{} argumemt".format("1"))
    else:
        print("{} arguments:".format(num_args))
        for i, arg in enumerate(sys.argv[1:], 1):
            print("{}: {}".format(i, arg))


if __name__ == "__main__":                            main():
