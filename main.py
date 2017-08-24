from menu import Menu

ciphers = ["caesar / vignerere"]

menuObj = Menu(ciphers)
# få modus, metode, nøkkel og melding
menuObj.main()
# utfør operasjon
if menuObj.cipher == "caesar / vignerere":
    from caesar_vignerere import Caesar_Vignerere
    cipher = Caesar_Vignerere(msg=menuObj.msg , key=menuObj.key , mode=menuObj.mode)
    cipher.excecute()

