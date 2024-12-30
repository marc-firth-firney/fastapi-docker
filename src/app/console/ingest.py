# import sys
# import os

# # Add the parent directory to sys.path if the script is run directly
# if __name__ == "__main__" and __package__ is None:
#     sys.path.append(os.path.dirname(
#         os.path.dirname(os.path.abspath(__file__))))

from services.prismic import PrismicAdapter
import time
from app.bootstrap.log import log
import typer

class IngestCommand:
    def __init__(self, batch_size: int = 20, types: str = "all"):
        self.batch_size = batch_size
        self.content_types = ["shops"]
        self.prismic_adapter = PrismicAdapter()  # Use the updated adapter
        self.fields = ["uid", "name"]  # Fields to extract

    def run(self):
        # Fetch all documents using the updated adapter
        results = self.prismic_adapter.fetch_all(
            content_types=self.content_types,
            locale="en",  # Specify the locale
            fields=self.fields  # Specify fields to extract
        )

        # Print or process the results
        log.error(f"results: {results}")

        # Optional progress bar (if processing batches is needed)
        # batch_count = len(results) // self.batch_size
        # with typer.progressbar(length=batch_count) as progress:
        #     for _ in range(batch_count):
        #         # Simulate processing time
        #         time.sleep(1)
        #         # Increment progress by batch size
        #         progress.update(self.batch_size)
        # print(f"Processed {self.batch_size} items in {batch_count} batches.")


if __name__ == "__main__":
    def main(batch_size: int = 20, types: str = "all"):
        cmd = IngestCommand(batch_size=batch_size, types=types)
        cmd.run()

    typer.run(main)
