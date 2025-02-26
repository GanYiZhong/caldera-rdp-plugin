from app.objects.c_ability import Ability
from plugins.rdp_plugin.app.rdp_plugin.abilities.rdp_attack import RDPAttack

name = 'RDP Plugin'
description = 'A plugin for RDP attack simulation and screen capture'
address = '/plugin/rdp'

async def enable(services):
    rdp_attack = RDPAttack(services)
    																																									
    # 新版註冊方式
    await services.get('knowledge_svc').register_ability(
        ability=rdp_attack,
        payloads=[],
        requirements=[]
    )
    
    # 使用新版REST API服務註冊路由
    rest_api = services.get('rest_api_svc')
    rest_api.add_route('GET', '/plugin/rdp/screens/{agent_id}', rdp_attack.get_screen)
    rest_api.add_static('/rdp/screens', 'plugins/rdp_plugin/data/screens', append_version=True)

