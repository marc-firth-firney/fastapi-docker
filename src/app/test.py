# hammerson-tenant-data-service-fastapi/src/app/test.py
import requests
from concurrent.futures import ThreadPoolExecutor

# Configuration
API_ENDPOINT = "https://hammerson.cdn.prismic.io/api/v2"
ACCESS_TOKEN = "MC5aM0hacmhJQUFDa0FHWGNL.77-9Fu-_vSTvv710WO-_vSXvv73vv70c77-9RDvvv71177-977-9Lu-_vQnvv73vv73vv73vv73vv71eL--_ve-_vXs"
DOCUMENT_TYPE = "shop"
LOCALE = "en"  # Specify the desired locale
FIELDS = ["uid", "name"]  # Specify the fields to extract
PAGE_SIZE = 100  # Number of documents to fetch per page
MAX_WORKERS = 5  # Number of concurrent threads

def fetch_page(page, ref, document_type, locale, fields, access_token):
    """Fetch a single page of documents from Prismic."""
    headers = {"Authorization": f"Token {access_token}"} if access_token else {}
    query_params = {
        "q": f'[[at(document.type, "{document_type}")]]',
        "lang": locale,
        "ref": ref,
        "pageSize": PAGE_SIZE,
        "page": page,
    }

    response = requests.get(
        API_ENDPOINT + "/documents/search", headers=headers, params=query_params
    )
    if response.status_code != 200:
        raise Exception(f"Error: {response.status_code} - {response.text}")

    data = response.json()
    results = data.get("results", [])

    # Extract specified fields
    documents = []
    for doc in results:
        extracted_fields = {
            "uid": doc.get("uid"),
            "name": doc.get("data", {}).get("name"),
        }
        documents.append(extracted_fields)
    return documents, data.get("next_page")


def get_master_ref(api_endpoint, access_token=None):
    """Fetch the master ref from the Prismic API."""
    headers = {"Authorization": f"Token {access_token}"} if access_token else {}
    response = requests.get(api_endpoint, headers=headers)

    if response.status_code != 200:
        raise Exception(
            f"Error fetching ref: {response.status_code} - {response.text}")

    data = response.json()
    # Get the first ref (usually the master ref)
    return data.get("refs")[0].get("ref")


def fetch_all_documents(ref, document_type, locale, fields, access_token):
    """Fetch all documents using pagination and multithreading."""
    documents = []
    page = 1
    next_page = True

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        while next_page:
            future = executor.submit(
                fetch_page, page, ref, document_type, locale, fields, access_token
            )
            page_documents, next_page_url = future.result()
            documents.extend(page_documents)
            next_page = next_page_url is not None
            page += 1

    return documents


# Main execution
try:
    # Get the master ref
    master_ref = get_master_ref(API_ENDPOINT, ACCESS_TOKEN)

    # Fetch all documents
    documents = fetch_all_documents(
        master_ref, DOCUMENT_TYPE, LOCALE, FIELDS, ACCESS_TOKEN
    )

    # Process documents as needed (e.g., save to a file)
    for doc in documents:
        print(doc)

except Exception as e:
    print(str(e))
