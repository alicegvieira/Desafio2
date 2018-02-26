import json, requests
from datetime import datetime

class Content:
    
    def __init__(self, apikey):        
        self.apikey = apikey
        self.url = "https://content.guardianapis.com/search" 
        self.url = self.url + "?api-key=" + self.apikey
    
    def getContent(self, filter, pagesize, fromdate, todate, page=None):
        try:
            content = ""
            self.url = self.url + "&q=" + filter
            
            self.url = self.url + "&page-size=" + str(pagesize)
   
            if page != None:
                self.url = self.url + "&page=" + str(page)
            
            fromdate = datetime.strftime(fromdate, '%Y-%m-%d')
            self.url = self.url + "&from-date=" + fromdate

            todate = datetime.strftime(todate, '%Y-%m-%d')
            self.url = self.url + "&to-date=" + todate            
           
            response = requests.get(self.url)            
           
            str_content = response.content.decode('utf-8')
            content = json.loads(str_content)
            
            self.status = content["response"]["status"]
            self.total = content["response"]["total"]
            self.pages = content["response"]["pages"]
                                   
        except Exception as e:
            print("ERROR:", str(e))
        return content
        
        
#http://content.guardianapis.com/search?from-date=2000-04-01&to-date=2000-04-01&q=education&api-key=test