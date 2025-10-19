
import requests
import json 
import ast 


class PageRequester:
      def __init__(self, url: str):
            self.url = url 
      
      def get(self):
            result=requests.get(self.url).content
            content=result.decode('utf-8')
            #return ast.literal_eval(content)
            data=json.loads(content)
            return f"Joke: {data['setup']} :\nAnswer:  {data['punchline']}"
      @property
      def get_header(self):
            print("\n")
            print(f" *** HEADER Information***\n")
            result=requests.get(self.url)
            headers=result.headers
            
            for key,value in headers.items():
                  print(f"{key}: {value}")
                  

jokes=PageRequester("https://official-joke-api.appspot.com/random_joke")

print(jokes.get())


