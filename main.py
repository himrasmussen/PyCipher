from menu import Menu

ciphers = ["caesar / vignerere", "homophonic substitution"]

menuObj = Menu(ciphers)
# få modus, metode, nøkkel og melding
menuObj.main()
# utfør operasjon
if menuObj.cipher == "caesar / vignerere":
    from vignerere import Vignerere
    cipher = Vignerere(msg=menuObj.msg , key=menuObj.key , mode=menuObj.mode)
    cipher.excecute()
elif menuObj.cipher == "homophonic substitution":
    from homophonic.homophonic_cipher import HomophonicCipher
    from homophonic.table_getter import TableGetter
    
    tablegetter = TableGetter()
    # get table from user or make one
    tablegetter.does_user_have_the_table()
    tablegetter.get_or_make_table() 
    cipher = HomophonicCipher(msg=menuObj.msg, key='',  key_file=tablegetter.key_file, mode=menuObj.mode)
    cipher.import_substitution_table()
    cipher.excecute(menuObj.mode)
