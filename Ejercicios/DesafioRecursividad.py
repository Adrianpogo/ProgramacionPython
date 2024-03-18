def visualizar_estructura(estructura, nivel=0, index=1):
    for elemento in estructura:
        if isinstance(elemento, list):
            print("  " * nivel + f"{index}: -> <class 'list'>")
            visualizar_estructura(elemento, nivel + 1, 1)
        elif isinstance(elemento, dict):
            print("  " * nivel + f"{index}: -> <class 'dict'>")
            for key, value in elemento.items():
                if isinstance(value, (list, dict, tuple, set)):
                    print("  " * (nivel + 1) + f"{index}:", end="")
                    visualizar_estructura([value], nivel + 1, 1)
                else:
                    print("  " * (nivel + 1) + f"{index}: {key} --> {value}")
        elif isinstance(elemento, tuple):
            print("  " * nivel + f"{index}: -> <class 'tuple'>")
            for i, item in enumerate(elemento):
                print("  " * (nivel + 1) + f"{index}: {i}: _> {item}")
        elif isinstance(elemento, set):
            print("  " * nivel + f"{index}: -> <class 'set'>")
            for i, item in enumerate(elemento):
                print("  " * (nivel + 1) + f"{index}: {i}: => {item}")
        else:
            print("  " * nivel + f"{index}: -> {elemento}")
        index += 1

estructura = [1,2,3,(1,2,3),4,5,6,[1,{"key1":1,"key2":2,"key3":{"Alumno1","Alumno2",True}},{1,2,3}]]

visualizar_estructura(estructura)


