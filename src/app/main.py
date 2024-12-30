from app.bootstrap import init

'''
|--------------------------------------------------------------------------
| Initialize The Application
|--------------------------------------------------------------------------
| The first thing we will do is create a new FastAPI application instance.
| This will be used throughout the entire application lifecycle, and is
| used when registering API endpoints.
|
'''
init.run()


'''
|--------------------------------------------------------------------------
| Register The Initalised Application
|--------------------------------------------------------------------------
| The FastAPI ASGI app requires a variable named "app" to be set in the
| main.py file (this script). This is the variable that will be used 
| by uvicorn to run the application.
|
'''
app = init.app

