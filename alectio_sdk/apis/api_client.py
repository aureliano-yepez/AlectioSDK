import requests
import os 

from gql import Client, gql
from gql.client import RetryError
from gql.transport.requests import RequestsHTTPTransport

# connect to backend. 

class AlectioClient:
    def __init__(self, environ=os.environ):
        self._environ = environ


        if 'ALECTIO_API_KEY' not in self._environ:
            return 


        self.api_key = self._environ['ALECTIO_API_KEY']

        self.settings = {
            'section': "default",
            'git_remote': "origin",
            'ignore_globs': [],
            'base_url': "https://api.alectio.com"
        }

        self.endpoint = f'{self.settings["base_url"]}/graphql'

        self.headers = {'Accept': 'application/json',
                        'Content-Type': 'application/json',
                        'Authorization': 'Bearer %s' % self.api_key}






    def execute(self):
        """
        execute graphql query
        """

        # make post request to query
        return 


    # user need to be authenticated somehow
    def get_user(self):
        return 

    def get_user_project(self):
        return 

    def get_user_project_experiment(self):
        return 

    def get_company_models(self):
        return

    def create_experiment(self):
        return 


    def create_project(self):
        return 






        


        
