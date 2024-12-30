import app.bootstrap.init as bootstrap
from app.config.api import api

'''
|--------------------------------------------------------------------------
| Dynamically load all the endpoints for each API version
|--------------------------------------------------------------------------
| This function dynamically import all the endpoints files for each API 
| version and includes them in the router. API versions are prefixed
| automatically. i.e. /api, /api/v1, /api/v2, /api/latest
|
'''
def load_all():

    # A list of all the available endpoints for each API version
    endpoints_by_api_version = api["endpoints"]

    # We'll use the latest API version to also create /api and /api/latest endpoints
    latest_version = list(endpoints_by_api_version.keys())[0]

    # Loop through each API version in the dictionary (v1, v2)
    for version_prefix in endpoints_by_api_version:

        # Loop through each endpoint for this API version
        for endpoint in endpoints_by_api_version[version_prefix]:

            # Create the import name. i.e. app.api.v1.orders
            dynamic_import_name = "app.api." + version_prefix + "." + endpoint

            # Import the endpoint
            # This is equivalent to:
            # From app.api.v1 import orders
            dynamic_import = __import__(
                dynamic_import_name, fromlist=[endpoint])

            # Check if this version is the latest version
            if version_prefix == latest_version:
                # reset the versions list and include the latest version prefixes
                versions = ["/api/latest", "/api"]
            else:
                # reset the versions list
                versions = []

            # Create the prefix for this version of the API
            path_prefix = "/api/" + version_prefix

            # Add the prefix to the versions list
            versions.append(path_prefix)

            for api_prefix in versions:

                print(api_prefix + "/" + endpoint)

                # Add the dynamic import to the router
                bootstrap.app.include_router(
                    dynamic_import.router, prefix=api_prefix, tags=[endpoint])
