import boto3


def get_client(resource_name='ecs', region='ap-northeast-1'):
    return boto3.client(resource_name, region_name=region)
