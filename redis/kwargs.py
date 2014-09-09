def kwfunc(posi,**kwargs):
    print posi
    if "key" in kwargs:
        print kwargs["key"]

if __name__ == "__main__":
    kwar = {"key":"va"}
    kwfunc("posi1",**kwar)
