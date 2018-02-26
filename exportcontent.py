#!/usr/bin/python3

import sys, getopt, csv

from datetime import datetime
from classes.content import Content

def main(argv):
    
    apikey = "fb78e8c7-16df-4240-a1b1-ac5ddd267d0e"
    exportpath = "/alice/desafio2/csv_files/"
    
    fromdate = ''
    todate = ''
    
    try:
          opts, args = getopt.getopt(argv,"h", ["from=","to="])
    except getopt.GetoptError:
        print ('invalid arguments. try:')
        customExit()
    if not opts:
        print ('missing arguments. try:')
        customExit()
    for opt, arg in opts:
        if opt == '-h':
            customExit()            
        elif opt in ("--from"):            
            fromdate = validateDate("from", arg)                         
        elif opt in ("--to"):
            todate = validateDate("to", arg) 
    
    print ("It will get content searching for 'education' from",  datetime.strftime(fromdate, '%d/%m/%Y'), " to", datetime.strftime(todate, '%d/%m/%Y'))
    inscontent = Content(apikey)    
    content = inscontent.getContent("education", "50", fromdate, todate)

    if content != "":
        if inscontent.status == "ok":
            print ("The search returned", inscontent.total, "results")
        else:
            print ("Failed to receive searching results")
            sys.exit()
    else:
        print("Failed while searching for results")
        sys.exit()
        
    if inscontent.total > 0:       
        filename = "content_f_" + datetime.strftime(fromdate, '%d%m%Y') + "_t_" + datetime.strftime(todate, '%d%m%Y')
        filename = filename + "__" + datetime.strftime(datetime.now(), '%d%m%Y_%H%M%S') + ".csv"
        
        csvfile = exportpath + filename
        
        print("It will export searching results to file '", csvfile, "'. Page {1} of {", inscontent.pages, "}...")
        
        exportResultsToFile(content, csvfile, "y")
        
        for x in range(1, inscontent.pages):            
            x += 1
            print("Exporting content from page {", x, "} of {", inscontent.pages, "}...")
            content = inscontent.getContent("education", 50, fromdate, todate, x)
            exportResultsToFile(content, csvfile, "n")
            
        print("Finished exporting content to file")
        
    else:
        print("Exiting..there are no results to export")
        sys.exit()
    
def customExit():
    print ('exportcontent.py --from <mm/dd/YYYY> --to <mm/dd/YYYY>')
    sys.exit()    

def validateDate(argname, argvalue):
    try:
        date = datetime.strptime(argvalue, '%d/%m/%Y')
    except:
        print ('argument --', argname ,'{', argvalue , '} is invalid. try:')
        customExit()
    return date
            
def exportResultsToFile(content, csvfile, header):   
        content = content["response"]        
        results = content["results"]
        
        with open(csvfile, 'a', newline='') as ocsvfile:
            output = csv.writer(ocsvfile)
             
            if header == "y":
                output.writerow(results[0].keys())  # header row            

            for result in results:
                output.writerow(result.values())
    

if __name__ == "__main__":
   main(sys.argv[1:])
