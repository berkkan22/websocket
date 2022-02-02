from aiohttp import web
import socketio
import switchChannalScript as sw


sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

# driver = ''


async def index(request):
    """Serve the client-side application."""
    # with open('index.html') as f:
    #     return web.Response(text=f.read(), content_type='text/html')
    return web.Response(text="Hello World", content_type='text/html')


@sio.event
def connect(sid, environ):
    print("connect ", sid)
    sw.open()


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


@sio.on('switchChannal')
async def switchChannal(sid, data):
    print(data)
    sw.switchSelenium('test')
    # await sio.emit('event', {'data': 'foobar'})


# app.router.add_static('/static', 'static')
app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app)


##################################################

# def switchSelenium(channal):
#     driver.get(channal)
