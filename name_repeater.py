# Először a nevedet kéri
# megkérdezi hányszor írja ki
# írja ki ennyiszer a nevedet
# szorgalmi: írd ki a név elé, hogy éppen hanyadjára kerül kiírásra és ne nullától számoljon

name = input("Kérem a nevedet:")
count = int(input("Hányszor írjam ki?"))
for i in range(1, count + 1):
    print(str(i) + " " + name)

