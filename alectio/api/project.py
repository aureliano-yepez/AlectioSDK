from alectio.client import AlectioClient
# do not expose pk and sk for projects

class Project:
    def __init__(self, user_id, project_id):
        self.project_id = project_id
        self.client = AlectioClient()
    
    def created_experiment(self):
        return 

    def upload_classes(self):
        """
        upload class labels to the user project 
        """
        return 

    def pending_labels(self):  
        """
        show all pending labels for a project 
        """
        return 


    # default function call if no function is called
    def info(self):
        """
        information on a project.
        """
        id_param = self.project_id
        query_str = """query project($%s: ID!)""" % (
            id_param)

        res = self.client.execute(
            query_str, {id_param: self.project_id})

        # should return json of the project info. 
        return res

        


        # need to convert to a list of iterable objects.








# alectio_client.create_project()
# returns a Project object 
