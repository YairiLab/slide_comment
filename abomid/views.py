from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

@view_config(route_name='login', renderer='templates/login.pt')
def login(request):
    if request.method == 'GET':
        return {}
    else:
        session = request.session
        session['id'] = request.params.get('id')
        session['name'] = request.params.get('name')
        print('start: ' + session['id'] + ' - ' + session['name'])
        raise HTTPFound(request.route_url('slide', page=1))

slides = [
    ('slide1.jpg', 'slide 1'),
    ('slide2.jpg', 'slide 2'),
    ('slide3.jpg', 'slide 3')
]

@view_config(route_name='slide', renderer='templates/slide.pt')
def slide(request):
    page = int(request.matchdict['page'])
    name = request.session['name']
    if request.method == 'GET':
        if page <= len(slides):
            slide = slides[page-1]
            return { 'name': name, 'imgsrc': slide[0], 'imgalt': slide[1], 'page': page}
        else:
            raise HTTPFound(request.route_url('end'))
    else:
        text = request.params.get('text1')
        print(name + ": " + text)
        raise HTTPFound(request.route_url('slide', page=page+1))

@view_config(route_name='end', renderer='json')
def end(request):
    return 'end'
