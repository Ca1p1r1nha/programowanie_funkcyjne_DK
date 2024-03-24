def CzyLista(obiekt):
    typ =  isinstance(obiekt,list)
    match typ:
        case True:
            return "lista"
        case False:
            test = isinstance(obiekt, tuple)
            if test == True: return "tupla"
            elif test == False: return "dict"






print(CzyLista([]))

