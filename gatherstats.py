import pycurl
import certifi
import io
import json


#This URL is the URL for the API specific to the Avalanche Team
TEAM_URL = "https://statsapi.web.nhl.com/api/v1/teams/21"

#Modifiers are used to gather more specific information!
ACTIVE_ROSTER_MODIFIER = "?expand=team.roster"

buffer = io.BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, TEAM_URL+ACTIVE_ROSTER_MODIFIER)
c.setopt(c.WRITEDATA, buffer)
c.setopt(c.CAINFO, certifi.where())
c.perform()
c.close()
body = buffer.getvalue().decode('UTF-8')
body = json.loads(body)
print(json.dumps(body,indent=4,sort_keys=True))
