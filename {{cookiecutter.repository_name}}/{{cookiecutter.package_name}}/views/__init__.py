from os.path import exists, join
from pyramid.response import FileResponse, Response
from pyramid.view import view_config


@view_config(route_name='index')
def index(request):
    data_folder = request.data_folder
    path = join(data_folder, 'index.html')
    if not exists(path):
        return Response('')
    return FileResponse(path, request)
