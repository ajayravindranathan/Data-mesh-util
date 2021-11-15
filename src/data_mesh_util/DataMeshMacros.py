from data_mesh_util.lib.constants import *
from data_mesh_util import DataMeshAdmin as data_mesh_admin


class DataMeshMacros:
    _data_mesh_account_id = None
    _region = None
    _log_level = None

    def __init__(self, data_mesh_account_id: str, region_name: str, log_level: str):
        self._data_mesh_account_id = data_mesh_account_id
        self._region = region_name
        self._log_level = log_level

    def bootstrap_account(self, account_type: str, mesh_credentials, account_credentials):
        # create a data mesh admin for the mesh account
        mesh_admin = data_mesh_admin.DataMeshAdmin(
            data_mesh_account_id=self._data_mesh_account_id,
            region_name=self._region,
            log_level=self._log_level,
            use_creds=mesh_credentials
        )

        # create a data mesh admin for the target account
        account_admin = data_mesh_admin.DataMeshAdmin(
            data_mesh_account_id=self._data_mesh_account_id,
            region_name=self._region,
            log_level=self._log_level,
            use_creds=account_credentials
        )

        if account_type == PRODUCER:
            account_admin.initialize_producer_account()
            mesh_admin.enable_account_as_producer(account_credentials.get('AccountId'))
        elif account_type == CONSUMER:
            account_admin.initialize_consumer_account()
            mesh_admin.enable_account_as_consumer(account_credentials.get('AccountId'))
