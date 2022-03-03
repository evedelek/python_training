

year = int(input("Kérem a születési éved"))
if (year <1900 or year >2022):
    print("Helytelen születési év")
else:
    print("Az életkorod " + str(2022 -year) + "év")