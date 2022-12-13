from os import path

from fastapi.responses import FileResponse, HTMLResponse
from kh_common.server import ServerApp
from kh_common.exceptions.http_error import NotFound


app = ServerApp(auth=False)


@app.get('{uri:path}')
async def all_routes(uri: str) :
	local_uri = uri.strip('\./')

	if not local_uri :
		return FileResponse('index.html')

	if path.isfile(local_uri) :
		return FileResponse(local_uri)

	if '.' not in local_uri and path.isfile(local_uri + '/index.html') :
		return FileResponse(local_uri + '/index.html')

	raise NotFound('the requested resource does not exist')


if __name__ == '__main__' :
	from uvicorn.main import run
	run(app, host='0.0.0.0', port=3000)
