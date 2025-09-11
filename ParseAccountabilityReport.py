# Doing this first cause I don't know how to interact with Falconnet's API not trying to learn tonight
# I'm assuming this is meant part is meant to be a function call later on for the rest of the file
import pandas as pd

#Dunno if it should be a single file at time or not, shouldn't be hard change either way
def ParseAccountabilityReport(filenmame):
    try:
        dataframe = pd.read_excel(filenmame)
    except Exception as e:
        print(f"Error Reading File: {e}")
    
    print("hi")
    #split between accounted, excused, and missing, not sure if this the goal, just made the most sense to me
    accounted = []
    excused = []
    missing = []
    
    
    for index, row in dataframe.iterrows():
            #print("hi")
            status = row.get("Status")
            
            #print(status)


            if(status == "Signed" || status == "Out"):
                print("hi")
                accounted.append([row.get("Name"),row.get("Room"),row.get("Email")])
            elif(status == "Excused"):
                excused.append([row.get("Name"),row.get("Room"),row.get("Email")])
            else:
                missing.append([row.get("Name"),row.get("Room"),row.get("Email")])
    
    print(missing)

ParseAccountabilityReport("test.xlsx")