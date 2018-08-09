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

#This is who the user is looking for
doc1 = nlp("Experienced supply chain manager working in retail sector.")

#these are the users available for matching
doc2 = nlp("A person with experience in freight forwarding and supply chain")
doc3 = nlp("A person educated to bachelor level and currently employed in Finance or Accounting sector.")
doc4 = nlp("Accountant, possible graduate who would like to share the existing  job or apply for position jointly")
doc5 = nlp("A person with a Degree in Architecture or Design to work together on a part time basis.")


#creating a list to loop through
doc_list = [doc1, doc2, doc3, doc4, doc5]

for doc in doc_list:
    i=0
    print(doc, doc.similarity(doc_list[i]))
    i+=1


# The following solutions could have been an alternative

#summary= UserProfile.objects(pk=userprofile.pk).values_list('pers_summary')
#target_partners = UserProfile.objects.exclude(id=request.user.id).values_list('target_partner')

#merge the 2 and use new list for similarities search

#doc_dict = summary + target_partners


#The problem here is that since .similarity() can only hold 2 arguments at the time
#In addition summaries and target_partners are producing distionaries, while lists are required
#Triple nested for loop will need to be used, which will be extremely inefficient

# An optimal solution is working directly with vector representations of the strings using a matrix
# This solution will be implemented in production, but will require more time, as more studies will be needed
