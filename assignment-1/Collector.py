class myCollector:
    myList = [];

    def add(self, x):
        myCollector.myList.append(x)
        print("Updated List:", myCollector.myList)

    def _init_(self, x):
        print("Hello World")


def main():
    print("python main function")
    col = myCollector
    col.add(col, 7)
    col.add(col, 9)
    col.add(col, 11)


if _name_ == '_main_':
    main()