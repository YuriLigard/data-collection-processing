import requests


class RequestsWithCaching:


    def __init__(self, baseUrl: str, params: dict, dbcache: object) -> None:
        
        self.baseUrl = baseUrl
        self.params = params
        self.dbcache = dbcache

    
    def get(self):

        keycache = self.baseUrl+"_".join([str(self.params[key]) for key in self.params if key != "api_key"])

        incache = self.dbcache.seach(keycache)

        if incache == None:
            try:
                resp = requests.get(self.baseUrl, self.params)
                value = resp.text
                self.dbcache.add(keycache, value)
                print("----->  ",resp.url)
            except requests.exceptions.ConnectionError as err:   # Montar conjunto de ex...
                print('\n requests: {0} \n'.format(err)) # subs por geração de logs 
        else:
            print("cache....")
            value = incache

        return value
    
    def post(self):

        keycache = self.baseUrl+"_".join([str(self.params[key]) for key in self.params if key != "api_key"])

        incache = self.dbcache.seach(keycache)

        if incache == None:
            try:
                resp = requests.post(self.baseUrl, headers=self.params['headers'], data=self.params['data'])
                value = resp.text
                self.dbcache.add(keycache, value)
                print("----->  ",resp.url)
            except requests.exceptions.ConnectionError as err:   # Montar conjunto de ex...
                print('\n requests: {0} \n'.format(err)) # subs por geração de logs 
        else:
            print("cache....")
            value = incache

        return value
    