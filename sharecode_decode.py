from steam.client import SteamClient
from steam.steamid import SteamID
from csgo.client import CSGOClient
from csgo.sharecode import decode

client = SteamClient()
cs = CSGOClient(client)

@client.on('logged_on')
def start_csgo():
    cs.launch()

@cs.on('ready')
def gc_ready():
    share_code = # https://developer.valvesoftware.com/wiki/Counter-Strike:_Global_Offensive_Access_Match_History, loop until HTTP CODE 202 for the last sharecode, rate limitations apply.
    decoded = decode(share_code)
    matchID = decoded['matchid']
    outcomeID = decoded['outcomeid']
    token = decoded['token']
    cs.request_full_match_info(matchID, outcomeID, token)
    response, = cs.wait_event("full_match_info")
    print(response)
    pass

client.cli_login(username="", password="")
client.run_forever()
