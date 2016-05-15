worlds["lastingland"] = "/home/minecraft/mc/lastingland"
texturepath = "/home/minecraft/textures"
outputdir = "/var/www/html/overviewer-test"
processes = 1

def playerIcons(poi):
    if poi['id'] == 'Player':
        poi['icon'] = "http://overviewer.org/avatar/%s" % poi['EntityId']
        return "%s" % poi['EntityId']

def signFilter(poi):
	# Return (hover text, window content text)
	if poi['id'] == 'Sign':
		# Signs have Text1 - Text4
		if (poi['Text1'].startswith("[home]")):
			poi["icon"] = "marker_tower.png"
			return "\n".join([poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']])
		if (poi['Text1'].startswith("[farm]")):
			poi["icon"] = "marker_factory_red.png"
			return "\n".join([poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']])
		if (poi['Text1'].startswith("[claim]")):
			poi["icon"] = "marker_mine_red.png"
			return "\n".join([poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']])
		if (poi['Text1'].startswith("[waypoint]")):
#			poi["icon"] = ""
			return "\n".join([poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']])
		if (poi['Text1'].startswith("[city]")):
			poi["icon"] = "marker_town.png"
			return "\n".join([poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']])
		return None

end_lighting = [Base(), EdgeLines(), Lighting(strength=0.5)]
end_smooth_lighting = [Base(), EdgeLines(), SmoothLighting(strength=0.5)]

renders["end"] = {
	"world": "lastingland",
	"title": "End",
	"rendermode": end_smooth_lighting,
	"dimension": "end",
	"markers": [
		dict(name="Signs", filterFunction=signFilter, createInfoWindow=False, checked=True),
		dict(name="Players", filterFunction=playerIcons, createInfoWindow=False, checked=True),
	],
	"poititle": "Overlays",
	"showspawn": False,
	"defaultzoom": 1, # 0-8
}


#renders["nether"] = {
#	"world": "lastingland",
#	"title": "Nether",
#	"rendermode": nether_smooth_lighting,
#	"dimension": "overworld",
#	"markers": [
#		dict(name="Signs", filterFunction=signFilter, createInfoWindow=False, checked=True),
#		dict(name="Players", filterFunction=playerIcons, createInfoWindow=False, checked=True),
#	],
#	"poititle": "Overlays",
#	"showspawn": False,
#}

