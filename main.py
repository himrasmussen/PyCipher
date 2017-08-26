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
    from homophonic_cipher import HomophonicCipher
    cipher = HomophonicCipher(msg=menuObj.msg, key="", mode=menuObj.mode)
    cipher.does_user_have_the_table()
    cipher.get_or_make_table()
    cipher.import_substitution_table()
    cipher.excecute(menuObj.mode)
