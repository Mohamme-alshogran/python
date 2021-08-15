the_file = None
the_tries = 5
while the_tries > 0 :
    try :
        print("enter yhe file name withe absolut : ")
        print(f" you have{the_tries}tries left")
        print("example : E:\ALAA")
        file_name_and_path = input( "file name :  ")
        the_file= open(file_name_and_path)
        print(the_file.read())
        break
    except FileNotFoundError:
        print("file not found")
        the_tries -= 1
    except :
        print("error")
    finally:
        if the_file is not  None :
            the_file.close()
            print("file close")

