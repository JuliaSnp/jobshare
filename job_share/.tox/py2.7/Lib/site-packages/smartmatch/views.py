from django.shortcuts import render
#from accounts.models import UserProfile
from django.contrib.auth.decorators import login_required


#SPACY library was used: https://spacy.io/usage/
#Script was modified to suit this application, as tutorial only provides for a single comparison

#I chose this model as it has been pre-trained and has 685k keys, 20k unique vectors (300 dimensions)
#python -m spacy download en_core_web_md

#needs to be downloaded for the file to run


import spacy

nlp = spacy.load('en_core_web_md')

#the first in the list is a target_partner of the user performing a search
#the following ones are personal summaries of users being searched for

doc1 = nlp("good childminder is working")
doc2 = nlp("Bad childminder resigned")
doc3 = nlp("Good engineer looking for job")

#creating a list to loop through
doc_list = [doc1, doc2, doc3]

for doc in doc_list:
    i=0
    print(doc, doc.similarity(doc_list[i]))
    i+=1


# The following solutions could have been an alternative

#summaries = UserProfile.objects(pk=userprofile.pk).values_list('pers_summary')
#target_partners = UserProfile.objects.exclude(id=request.user.id).values_list('target_partner')

#concatenate the 2 and use new list for similarities search

#doc_list = target_partners + summaries

#The problem here is that since .similarity() can only hold 2 arguments at the time
#Triple nested for loop will need to be used, which will be extremely inefficient

# An optimal solution is working directly with vector representations of the strings using a matrix
# This solution will be implemented in production, but will require more time, as more studies will be needed
