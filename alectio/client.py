import requests
import os 
import json

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

        # cli user settings
        self.settings = {
            'git_remote': "origin",
            'ignore_globs': [],
            'base_url': "https://api.alectio.com"
        }

        self.endpoint = f'{self.settings["base_url"]}/graphql'

        self.headers = {'Accept': 'application/json',
                        'Content-Type': 'application/json',
                        'Authorization': 'Bearer %s' % self.api_key}



    def execute(self, query, params):
        """
        execute graphql query
        """

        data = json.dumps(
            {'query': query, 'variables': params}).encode('utf-8')

        try:
            response = requests.post(self.endpoint, data=data)

            # logger.debug("Response: %s", response.text)
        except RuntimeError:
            # logger.debug("Response: %s", response.text
            pass
        return 1


    # user need to be authenticated somehow
    def user(self): 

        return 

    def projects(self):
        # given a user search through all the projects 
        return 

    def experiments(self, project_id):
        # given a project object search through all the experiments. 
        return 

    def models(self):
        # get all the models the user is associated with
        return 

    def project(self, project_id):
        # get project information 
        return 

    def experiment(self):
        # get experiment information
        return 

    def model(self, model_id):
        # get model information
        return 

    def create_project(self):
        # create a project either through command line 
        return 

    def create_experiment(self):
        # create an experiment given a project item 
        return 
