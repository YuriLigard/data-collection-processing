import requests


class Requests:


    def __init__(self, baseUrl: str, params: dict, headers: dict) -> None:
        
        self.baseUrl = baseUrl
        self.params = params
        self.headers = headers

    
    def get(self) -> object | None:
        
        try:
            resp = requests.get(self.baseUrl, headers=self.headers, params=self.params)
            return resp

        except requests.exceptions.ConnectionError as cr: 
            print("\n An error occurred while attempting to connect to the server. Please check your internet connection and try again. If the issue persists, contact technical support for assistance. {0} \n".format(cr)) 
            return None
        
        except requests.exceptions.HTTPError as httpe:
            print("\n An HTTP error occurred while making the request to the server. Please review your request and try again. If the issue persists, contact technical support for assistance. {0} \n".format(httpe))
            return None
    
    def post(self) -> object | None:
        
        try:
            resp = requests.post(self.baseUrl, headers=self.headers, data=self.params)
            return resp
        
        except requests.exceptions.ConnectionError as cr: 
            print("\n An error occurred while attempting to connect to the server. Please check your internet connection and try again. If the issue persists, contact technical support for assistance. {0} \n".format(cr)) 
            return None
        
        except requests.exceptions.HTTPError as httpe:
            print("\n An HTTP error occurred while making the request to the server. Please review your request and try again. If the issue persists, contact technical support for assistance. {0} \n".format(httpe))
            return None