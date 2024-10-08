caracteres_seguros = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZñÑáéíóú0123456789"
top_not_heros = {
      "John Constantine" :"a fictional superhero, appearing in comic books, film, and television. He is played by Keanu Reeves in the 2005 film Constantine and by Matt Ryan in the CW series Legends of Tomorrow and Constantine. ",
      "Death" : "a fictional character from the DC comic book series, The Sandman. The character first appeared in The Sandman vol. 2, #8, and was created by Neil Gaiman and Mike Dringenberg. In the stories, Death is both the end of life and a psychopomp. Like most anthropomorphic personifications of death, Death meets with the recently deceased and guides them into their new existence. However, unlike most personifications of death, she also visits people as they are born, according to Destruction in the Sandman Special: The Song of Orpheus. Evidently, only she seems to remember these encounters.",
      "Hellboy" : "a fictional character created by writer-artist Mike Mignola. The character first appeared in San Diego Comic-Con Comics #2, and has since appeared in various eponymous miniseries,  one-shots and intercompany crossovers. The character has been adapted into two live-action feature films in 2004 and 2008  that starred Ron Perlman in the title role, and two straight-to-DVD animated films, as well as two video games – Asylum Seeker and The Science of Evil. A well-meaning demon whose true name is Anung Un Rama, Hellboy was summoned from Hell to Earth as an infant demon on December 23, 1944 by Nazi occultists. He was discovered by the Allied Forces; amongst them, Professor Trevor: 1964",
      "Dream" : "a fictional character and the protagonist of DC Comics' Vertigo comic book series The Sandman, written by Neil Gaiman. One of the seven Endless, inconceivably powerful beings older and greater than gods, Dream is both lord and personification of all dreams and stories, all that is not in reality. He has taken many names, including Morpheus and Oneiros, and his appearance can change  depending on the person who is seeing him. Dream was named the sixth-greatest comic book character by Empire Magazine. He was also named fifteenth in IGN's 100 Top Comic Book Heroes list",
      "Crow" : "a fictional character and the protagonist of The Crow comic book series, originally created by American artist James O'Barr in 1989. The titular character is an undead vigilante brought back to life by a supernatural crow to avenge his murder and that of his fiancée. The character has subsequently appeared in several feature films, a television series, and spin-off novels and cs. In the various incarnations, films, and spin-offs, many people have taken on the Crow persona in order to avenge their own wrongful deaths. In 2011, IGN ranked the Crow 37th in the Top 100 Comic Book Heroes ",
      "Alfred Pennyworth" : "Alfred Thaddeus Crane Pennyworth is a fictional character who appears throughout the DC Universe. The character first appears in Batman #16, and was created by writers Bob Kane and Bill Finger, and artist Jerry Robinson. Alfred serves as a loyal, tireless butler who assists his employer's secret life as Batman. In modern interpretations, he is depicted as Bruce Wayne's butler, legal guardian, best friend, aide-de-camp, and surrogate parent following the murders of Thomas Wayne and Martha Wayne. He has sometimes been called Batman's batman. He also provides comic relief, as his sometimes sarcastic and cynical attitude often adds humor to dialogue occurring between himself",
      "Lucifer" : "Lucifer Morningstar is a DC Comics character appearing primarily as a supporting character in the comic book series The Sandman and as the title character of a spin-off, both published under the Vertigo imprint. Though various depictions of Lucifer – the Biblical fallen angel and Devil of the Abrahamic religions – have been presented by DC Comics in their run, this interpretation by Neil Gaiman debuted in The Sandman in 1989. Like many modern interpretations of Satan, DC's Lucifer owes much to the character's portrayal in John Milton's epic poem Paradise Lost, though Gaiman adapts the character to fit the fictional DC Universe where their comics are set, where the character exists",
      "Swamp Thing" : "a fictional character in the DC Comics Universe. He is a humanoid/plant elemental creature, created by writer Len Wein and artist Berni Wrightson. Swamp Thing has had several humanoid or monster incarnations in various different storylines. He first appeared in House of Secrets #92 in a stand-alone horror story set in the early 20th century. The character then returned in a solo series, set in the contemporary world and in the general DC continuity. The character is a humanoid mass of vegetable matter who fights to protect his swamp home, the environment in general, and humanity from various supernatural or terrorist threats. The character found perhaps his greatest",
      "James Gordon" : "Commissioner James (Jim) W. Gordon, Senior is a fictional character, an ally of Batman who appears in comic books published by DC Comics. The character first appeared in Detective Comics #27, and was created by Bill Finger and Bob Kane. Gordon made his debut in the first panel of this comic, making him the first Batman supporting character to be introduced. In most incarnations of the Batman mythos, James Gordon is the Police Commissioner of Gotham City. He shares Batman's deep commitment to ridding the city of crime. In Golden and Silver age comics and on the 1960s Batman television show, Gordon fully trusts, and is even somewhat dependent on Batman. In most modern stories"
    }

a_friend_like_me = """
Well, Ali Baba had them forty thieves
Sheherezade had a thousand tales
But, master, you in luck 'cause up your sleeves
You got a brand of magic never fails
You got some power in your corner now
Some heavy ammunition in your camp
You got some punch, pizazz, yahoo and how
All you gotta do is rub that lamp
And I'll say
Mister Aladdin, sir
What will your pleasure be?
Let me take your order
Jot it down
You ain't never had a friend like me
No no no
Life is your restaurant
And I'm your maître d’
C'mon whisper what it is you want
You ain't never had a friend like me
Yes sir, we pride ourselves on service
You're the boss, the king, the shah
Say what you wish, it's yours!
True dish, how about a little more baklava?
Have some of column A
Try all of column B
I'm in the mood to help you though
You ain't never had a friend like me
Can your friends do this?
Can your friends do that?
Can your friends pull this out their little hat?
Can you friends go, poof!
So don't ya sit there slack-jawed, buggy-eyed
I'm here to answer all your midday prayers
You got me bona fide and certified
You got a genie for your charge d'affaires
I got a powerful urge to help you out
So whatcha wish? I really wanna know
You got a list that's three miles long, no doubt
Well, all you gotta do is rub like so oh oh
Mister Aladdin, sir, have a wish or two or three
I'm on the job, you big nabob
You ain't never had a friend, never had a friend
You ain't never had a friend, never had a friend
You ain't never (never) had (had) a friend like me
You ain't never had a friend like me"""

def obten_estrofa(cancion, linea):
    global caracteres_seguros
    
    linea = limpia_cadena(caracteres_seguros, linea)
    cancion = cancion.split("\n")
    for y in cancion:
        cancion[cancion.index(y)] = limpia_cadena(caracteres_seguros, y)
    for y in cancion:
        if linea in y:
            x = cancion.index(y)
            if x + 1 <= len(cancion) - 1:
                a = cancion[x + 1]
                if x + 2 <= len(cancion) - 1:
                    b = cancion[x + 2]
                else:
                    b = ""
            else:
                a = ""
                b = ""
            c = [a, b]
            d = "\n".join(c)
            return(d)
        else:
            pass

def limpia_cadena(caracteres_seguros,cadena):
    lista=[]
    for caracter in cadena:
        if caracter in caracteres_seguros:
            lista.append(caracter)
    return "".join(lista)

def encuentra_relaciones(diccionario, palabra):
    lista=[]
    palabra= palabra.lower()
    for x in diccionario.keys():
        if palabra in diccionario[x].lower():
            lista.append(x)
    lista.sort()
    return lista

opcion = int(input())
if opcion == 1:
    cadena = input()
    print(limpia_cadena(caracteres_seguros, cadena))
elif opcion == 2:
    palabra = input()
    print(encuentra_relaciones(top_not_heros, palabra))
elif opcion == 3:
    linea = input()
    print(obten_estrofa(a_friend_like_me, linea))
else:
    print("entrada no válida.")
