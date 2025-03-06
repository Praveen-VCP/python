import gc



class Demo:
    def __del__(self):
        print(f"Object {self} is being destroyed")



def create_objects():
    obj8 = Demo()
    obj7 = Demo()



    obj8.ref = obj8
    obj7.ref = obj7

    del obj8
    del obj7

    print("Running garbage collector...")
    gc.collect()


gc.disable()

create_objects()

gc.enable()