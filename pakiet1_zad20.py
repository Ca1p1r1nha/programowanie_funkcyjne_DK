def CzyLista(arg):
    typ =  isinstance(arg,list)
    match typ:
        case True:
            return "lista"
        case False:
            if isinstance(arg, tuple) == True: return "tupla"
            elif isinstance(arg, dict) == True: return "dict"
            else: return None
            






print(CzyLista([]))

