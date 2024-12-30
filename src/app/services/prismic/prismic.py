import requests
from concurrent.futures import ThreadPoolExecutor
from app.bootstrap.log import log
from .credentials import PrismicCredentials

class PrismicAdapter:
    def __init__(self, max_workers=5, page_size=100):
        self.credentials = PrismicCredentials()
        self.api_url = self.credentials.api_url
        self.access_token = self.credentials.access_token
        self.max_workers = max_workers  # Number of threads for multithreading
        self.page_size = page_size  # Number of items per page

    def get_master_ref(self):
        """Fetch the master ref from the Prismic API."""
        headers = {
            "Authorization": f"Token {self.access_token}"} if self.access_token else {}

        response = requests.get(self.api_url, headers=headers)

        if response.status_code != 200:
            raise Exception(
                f"Error fetching ref: {response.status_code} - {response.text}")

        data = response.json()
        refs = data.get("refs", [])
        if not refs:
            raise Exception("No refs found in the Prismic API response.")

        # Get the master ref
        master_ref = next((ref["ref"]
                          for ref in refs if ref.get("isMasterRef")), None)
        if not master_ref:
            raise Exception(
                "Master ref not found in the Prismic API response.")

        return master_ref

    def fetch_page(self, content_type, page, ref, locale, fields):
        """
        Fetch a single page of documents from Prismic.
        :param content_type: The type of content to fetch.
        :param page: Page number to fetch.
        :param ref: The Prismic ref for the current version.
        :param locale: The desired locale (e.g., "en").
        :param fields: Fields to extract from each document.
        :return: A tuple of (results, next_page_flag).
        """
        headers = {
            "Authorization": f"Token {self.access_token}"
        } if self.access_token else {}

        query_params = {
            "q": f'[[at(document.type, "{content_type}")]]',
            "lang": locale,
            "ref": ref,
            "pageSize": self.page_size,
            "page": page,
        }

        print(headers)
        print(query_params)

        response = requests.get(
            f"{self.api_url}/documents/search",
            headers=headers,
            params=query_params
        )

        if response.status_code == 401:
            log.error(
                f"Unauthorized: Invalid or expired access token.")
            raise Exception(
                f"Invalid access token. Please update the token in PrismicCredentials."
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
                **{field: doc.get("data", {}).get(field) for field in fields if field != "uid"}
            }
            documents.append(extracted_fields)

        # Check if there's another page
        next_page = data.get("next_page") is not None
        return documents, next_page

    def fetch_all(self, content_types, locale="en", fields=None):
        """
        Fetch all documents using pagination and multithreading.
        :param content_types: A list of content types to fetch.
        :param locale: The desired locale (default is "en").
        :param fields: Fields to extract from each document.
        :return: A list of all documents.
        """
        documents = []
        ref = self.get_master_ref()

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            for content_type in content_types:
                page = 1
                next_page = True
                while next_page:
                    future = executor.submit(
                        self.fetch_page, content_type, page, ref, locale, fields)
                    page_documents, next_page = future.result()
                    documents.extend(page_documents)
                    page += 1

        return documents
