from SearchEngine.quickSortMultiList import quickSort
from SearchEngine.parserGraph.Parser import Parser
from SearchEngine.set import Set
import time

# def brojPonavaljanjaReciuDatoteci(datoteka, unesene_reci):
#     parser = Parser()
#     parser.parse(datoteka)
#     brojPonavljanja = 0
#
#     for word in parser.words:
#         for ureci in unesene_reci:
#             if ureci.lower() not in ['and', 'or', 'not']:
#                 if ureci.lower() == word.lower():
#                     brojPonavljanja = brojPonavljanja + 1
#     return brojPonavljanja

brojPonavljanjaUnetihReci = {}
def brojPonavaljanjaReciuDatoteci(globalResultSet, unesene_reci, recnikStranicaReci):
    start = time.time()
    for datoteka in globalResultSet:
        #print("DATOTEKA: " + datoteka)
        #print(recnikStranicaReci[datoteka])
        #parser = Parser()
        #parser.parse(datoteka)
        reci = recnikStranicaReci[datoteka]

        brojPonavljanja = 0

        #for word in parser.words:
        for word in reci:
            for ureci in unesene_reci:
                if ureci.lower() not in ['and', 'or', 'not']:
                    if ureci.lower() == word.lower():
                        brojPonavljanja = brojPonavljanja + 1
        brojPonavljanjaUnetihReci[datoteka] = brojPonavljanja
    end = time.time()
    #print("Ovo kosta " + str((end - start).__round__(4))+" sekundi.")
    return brojPonavljanjaUnetihReci


# RANGIRANJE PRETRAGE
def rangiranjePretrage(setSvihDatoteka,globalResultSet,dokumentiKojiImajuLinkKaDokumentu,bekLinkovi, unesene_reci,recnikStranicaReci):
    rankedStructure = [] #[ [elementizPretrage1, poeni1], [elementizPretrage2, poeni2]....]
    brojPonavljanjaUnetihReciDict = brojPonavaljanjaReciuDatoteci(setSvihDatoteka, unesene_reci,recnikStranicaReci)

    for element in iter(globalResultSet):
        brojponavljanjaReciuDatotekamaKojeLinkuju = 0

        # print("U RANGIRANJU SMO")
        # print(element)
        # print("clanovi dokumenata..")
        # for dok in dokumentiKojiImajuLinkKaDokumentu:
        #     print(dok)
        # #print(dokumentiKojiImajuLinkKaDokumentu)
        #
        # print(dokumentiKojiImajuLinkKaDokumentu[element])
        # print("\n")


        for z in dokumentiKojiImajuLinkKaDokumentu[element]:
            brojponavljanjaReciuDatotekamaKojeLinkuju = brojponavljanjaReciuDatotekamaKojeLinkuju + brojPonavljanjaUnetihReciDict[z]

        brojponavljanjaReci = brojPonavljanjaUnetihReciDict[element]
        rank = [element, bekLinkovi[element] + (brojponavljanjaReci*0.7) + (brojponavljanjaReciuDatotekamaKojeLinkuju*0.4)]
        rankedStructure.append(rank)

    #Samostalna implementacija algoritma za sortiranje u metodi quickSort)
    n = len(rankedStructure)
    quickSort(rankedStructure, 0, n - 1)

    povratniSet = Set('')
    for element in rankedStructure:
        povratniSet.elements.append(element[0])
        povratniSet.listaPoena.append(element[1])

    return povratniSet
