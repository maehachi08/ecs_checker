from lib.get_boto3_client import get_client


def get_describe_execution(execution_arn: str) -> dict:
    client = get_client('stepfunctions')
    return client.describe_execution(
        executionArn=execution_arn
    )


def get_step_names(execution_arn: str) -> list:
    input_data = json.loads(get_describe_execution(execution_arn=execution_arn)['input'])
    return [step.name for step in input_data['steps']]


def get_execution_status(execution_arn: str) -> str:
    return get_describe_execution(execution_arn=execution_arn)['status']

