import unittest
from unittest.mock import patch, Mock
import lib.ecs as target
from lib.get_boto3_client import get_client


class EcsModuleTest(unittest.TestCase):

    @patch('lib.ecs.get_client')
    def test_get_service_arns(self, mocked_get_client):
        service_arns = ['dummyservice-arn1', 'dummyservice-arn2']
        mocked_get_client('ecs').list_services.return_value = {
            'serviceArns': service_arns
        }
        response = target.get_service_arns(cluster_name='dummy-cluster')

        mocked_get_client.assert_called_with('ecs')
        args, kwargs = mocked_get_client('ecs').list_services.call_args
        self.assertEqual('dummy-cluster', kwargs['cluster'])
        self.assertEqual(service_arns, response)

    @patch('lib.ecs.get_client')
    def test_get_describe_services(self, mocked_get_client):
        service_arns = ['dummyservice-arn1', 'dummyservice-arn2']
        mocked_get_client('ecs').describe_services.return_value = {
            'services': ['dummmy-service1', 'dummmy-service2']
        }

        response = target.get_describe_services(
            cluster_name='dummy-cluster',
            service_arns=service_arns
        )

        mocked_get_client.assert_called_with('ecs')
        args, kwargs = mocked_get_client('ecs').describe_services.call_args
        self.assertEqual('dummy-cluster', kwargs['cluster'])
        self.assertEqual(['dummmy-service1', 'dummmy-service2'], response)

