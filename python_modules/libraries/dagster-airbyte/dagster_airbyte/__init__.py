from dagster._core.libraries import DagsterLibraryRegistry

try:
    from dagster_airbyte.managed import (
        AirbyteConnection as AirbyteConnection,
        AirbyteDestination as AirbyteDestination,
        AirbyteDestinationNamespace as AirbyteDestinationNamespace,
        AirbyteManagedElementReconciler as AirbyteManagedElementReconciler,
        AirbyteSource as AirbyteSource,
        AirbyteSyncMode as AirbyteSyncMode,
        load_assets_from_connections as load_assets_from_connections,
    )

except ImportError:
    pass

from dagster_airbyte.asset_defs import (
    build_airbyte_assets as build_airbyte_assets,
    load_assets_from_airbyte_instance as load_assets_from_airbyte_instance,
)
from dagster_airbyte.ops import airbyte_sync_op as airbyte_sync_op
from dagster_airbyte.resources import (
    AirbyteCloudResource as AirbyteCloudResource,
    AirbyteCloudWorkspace as AirbyteCloudWorkspace,
    AirbyteResource as AirbyteResource,
    AirbyteState as AirbyteState,
    airbyte_cloud_resource as airbyte_cloud_resource,
    airbyte_resource as airbyte_resource,
    load_airbyte_cloud_asset_specs as load_airbyte_cloud_asset_specs,
)
from dagster_airbyte.translator import DagsterAirbyteTranslator as DagsterAirbyteTranslator
from dagster_airbyte.types import AirbyteOutput as AirbyteOutput
from dagster_airbyte.version import __version__ as __version__

DagsterLibraryRegistry.register("dagster-airbyte", __version__)
