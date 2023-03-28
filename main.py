from PyPDF2 import PdfFileWriter,PdfFileReader

#creation de l'objet d'ecriture du fichier
fusion_rapport_recap=PdfFileWriter()

#Ouverture des fichiers à fusionner
rapport=open("Rapport.pdf","rb")
recap=open("recap.pdf","rb")

#lecture des données des fichiers à fussionner grace à l'objet PdfFileReader  
rapportlu=PdfFileReader(rapport)
recaplu=PdfFileReader(recap)

#recuperation des données des pages à fusionner
fusion_rapport_recap.addPage(recaplu.getPage(0))
fusion_rapport_recap.addPage(rapportlu.getPage(0))

#creation du fichier contenant les fichier à fusionner
RapportFinals=open("RapportFinales.pdf","wb")
fusion_rapport_recap.write(RapportFinals)

RapportFinals.close()
rapport.close()
recap.close()