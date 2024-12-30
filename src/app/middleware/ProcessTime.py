from fastapi import Request
import time

class ProcessTimeMiddleware:
    def __init__(self, header_key: str):
        self.header_key = header_key

    async def __call__(self, request: Request, call_next):
        start_time = time.time()
        print(request.__dir__())
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers[self.header_key] = str(process_time)
        print(response.__dir__())
        return response