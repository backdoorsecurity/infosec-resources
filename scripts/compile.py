# this runs on every commit ig, is cool

# we need yaml, cuz json is not very cool
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

comment = """<!---
        DO NOT EDIT THIS FILE!!!
    This file is statically generated by the scripts in the scripts/ folder!!!
    - If you want to add a youtube channel, edit the data/ytChannels.yml file!!!
-->\n"""

finalMD = ""
finalMD += comment
finalMD += "# InfoSec Resources\n\n"

# parts
ytChannelsMD = "## Youtube Channels\n\n"

with open("data/ytChannels.yml") as ytChans:
    ytChannels = load(ytChans.read(), Loader=Loader)
    for channel in ytChannels["ytChannels"]:
        ytChannelsMD += "- **{name}**: [link]({link}) {description}\n".format(name=channel["name"],link=channel["link"],description=channel["description"])

finalMD += ytChannelsMD

with open('readme.md', "w") as myfile:
    myfile.write(finalMD)
