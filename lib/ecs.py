import json

from lib.get_boto3_client import get_client


def get_service_arns(cluster_name: str) -> list:
    client = get_client('ecs')
    response = client.list_services(
        cluster=cluster_name,
        launchType='FARGATE',
    )

    return [service_arn for service_arn in response['serviceArns']]


def get_describe_services(cluster_name: str, service_arns: list) -> list:
    client = get_client('ecs')
    response = client.describe_services(
        cluster=cluster_name,
        services=service_arns,
    )

    return response['services']


def get_service_desired_count(cluster_name: str, service_arn: str) -> str:
    response = _get_describe_services(cluster_name=cluster_name, service_arn=service_arn)
    return response[0]['desiredCount']


def get_service_running_count(cluster_name: str, service_arn: str) -> str:
    response = _get_describe_services(cluster_name=cluster_name, service_arn=service_arn)
    return response[0]['runningCount']


def get_service_taskdefinition(cluster_name: str, service_arn: str) -> str:
    response = _get_describe_services(cluster_name=cluster_name, service_arn=service_arn)
    return response[0]['taskDefinition']


def get_taskdefinition_image(task_definition: str) -> str:
    response = _get_describe_services(cluster_name=cluster_name, service_arn=service_arn)
    return response[0]['taskDefinition']


def _get_describe_services(cluster_name: str, service_arn: str):
    return get_describe_services(cluster_name=cluster_name, service_arns=[service_arn])

