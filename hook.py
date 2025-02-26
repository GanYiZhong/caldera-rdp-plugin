from aiohttp import web
from aiohttp_jinja2 import template

class Hook:
    def __init__(self, services):
        self.auth_svc = services.get('auth_svc')
        self.data_svc = services.get('data_svc')
        self.rest_svc = services.get('rest_api_svc')
        self.template = 'rdp_plugin/templates/rdp_screens.html'

    @template('rdp_screens.html')
    async def splash(self, request):
        try:
            abilities = await self.data_svc.locate('abilities', match=dict(ability_id='T1021.001'))
            results = []
            for ability in abilities:
                links = await self.data_svc.locate('links', match=dict(ability=ability.ability_id))
                for link in links:
                    result = {
                        'agent_id': link.paw,
                        'target': link.host,
                        'status': link.status,
                        'message': link.output.get('message', 'No message available'),
                    }
                    results.append(result)
            return {
                'results': results																													
            }
        except Exception as e:
            return web.Response(text=f'Error loading RDP results: {str(e)}', status=500)

    async def enable(self):
        app = web.Application()
        app.router.add_route('GET', '/plugin/rdp/results', self.splash)
        return app

