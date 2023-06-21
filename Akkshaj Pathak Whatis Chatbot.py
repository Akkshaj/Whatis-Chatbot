#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#This is the main code of the chatbot named Whatis
#This chatbot has been developed by Akkshaj Pathak(akkshajpathak@gmail.com)
#This chatbot uses wikipedia libraries to answer any Whatis question of the user
#To use this chatbot, the following command should be used:
#  Whatis <User's query>
#For example : Whatis India?

print(" Hi!")
print(" I am Whatis chatbot")
print(" What can I do for you?")
print(" Please use this chatbot by asking question in this format 'whatis <user query>' ")
print(" For Ex.")
print(" whatis India democracy")
print("*********************************************************************************")
print("*********************************************************************************")
print("*********************************************************************************")



import wikipedia
#Using while loop for the chatbot to keep running
while True:

            print("****USE *quit* TO QUIT THE CHATBOT****")

            #Taking user input below
            x=  str(input("Enter your question - "))

            #Using if statement for ending of program
            if x == "*quit*":
                print("Quiting Chatbot!")
                break


            #splitting the user input(x) to different words. To check whatis command  
            sp= x.split()

            # Checking if whatis command is used in the chatbot or not. If its not whatis then report to user
            if sp[0].lower() != ("whatis") :
                print()
                print("******************************************************")
                print("Please use keywork (Whatis) before your quiry as below")
                print("Whatis <Your question>")
                print("******************************************************")
                print()
                print()
            # if whatis command is used then use users query/question to search in wikipedia and get the summary of the response and print it on the command prompt   
            elif sp[0].lower() == ("whatis"):
                # print("ok")
                whatisthis = x[7:]
                print("******************************************************")
                print("Summary response of: ",whatisthis)
                print("******************************************************")
                print("******************************************************")
                print("******************************************************")
                try:
                    print(wikipedia.summary(whatisthis))
                except Exception as e:
                    print("******************************************************")
                    print("I don't know about it. I am sorry!")
                    print(" Please try with another question!")
                    print("******************************************************")
                    
                
# End of the wqhatis chatbot program. This chatbot program uses wikipedia libraries to generate response for user query
# wikipedia library installation is requirement prior to running this program.
# Use the following command on a python prompt to install wikipedia library as below
# pip install wikipedia


# In[ ]:





# In[ ]:




