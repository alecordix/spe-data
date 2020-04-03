# #!/usr/bin/python3
# # -*- coding: UTF-8 -*-
# valeur1= int(input("Valeur 1 : "))
# valeur2= int(input("Valeur 2 : "))
# if valeur1 < valeur2  :
#     print("Valeur la plus petite :", valeur1)
# else:
#     print("Valeur la plus petite :", valeur2)

# #!/usr/bin/python3
# # -*- coding: UTF-8 -*-
# str_fumeur = input ("Fumeur (oui / non) : ")
# age_fumeur = int (input ("Age du fumeur : "))
# print()
# if (str_fumeur == "oui"):
#     facteur_f = 2
# else :
#     facteur_f = 0
# if (age_fumeur > 20):
#     facteur_a = 1
#     niveau_de_risque = facteur_f + facteur_a
# else :
#     facteur_a = 0
#     niveau_de_risque = facteur_f + facteur_a
# if niveau_de_risque >= 0:
#     print ("Le risque est nul ! Mais commence pas ok ?!")
# if niveau_de_risque >= 2:
#     print ("Tu vas crever ! Arrête de cloper connard")

# def greet(name,msg):
#    """This function greets to
#    the person with the provided message"""
#    print("Hello",name + ', ' + msg)
#
# greet("Andrea","have a good day!")
# print()
# def greet(*names):
#    """This function greets all
#    the person in the names tuple."""
#
#    # names is a tuple with arguments
#    for name in names:
#        print("Hello",name)
#
# greet("Monica","Luke","Steve","John")
#
# def how(*ages):
#     for age in ages:
#         print("I'm",age)
# how("21","28","24","22")
#
# Taking kilometers input from the user
kilometers = float(input("Entrez un nombre de kilomètres : "))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print('%0.2f kilomètres est égal à %0.2f miles' %(kilometers,miles))