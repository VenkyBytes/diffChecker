import boto3


class AWSService:
    def __init__(self):
        self.ecs_client = boto3.client('ecs')

    def get_task_definition(self, cluster_name, task_definition_arn):
        response = self.ecs_client.describe_task_definition(
            cluster=cluster_name,
            taskDefinition=task_definition_arn
        )
        return response['taskDefinition']
