worlds["lastingland"] = "/home/minecraft/mc/lastingland"
texturepath = "/home/minecraft/textures"
outputdir = "/var/www/html/overviewer"
processes = 1

def signFilter(poi):
	# Return (hover text, window content text)
	if poi['id'] == 'Sign':
		# Signs have Text1 - Text4
		if (poi['Text1'].startswith("[home]")):
			poi["icon"] = "icons/marker_tower.png"
			return "\n".join([poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']])
		if (poi['Text1'].startswith("[farm]")):
			poi["icon"] = "icons/marker_factory_red.png"
			return "\n".join([poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']])
		if (poi['Text1'].startswith("[claim]")):
			poi["icon"] = "icons/marker_mine_red.png"
			return "\n".join([poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']])
		if (poi['Text1'].startswith("[waypoint]")):
#			poi["icon"] = ""
			return "\n".join([poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']])
		if (poi['Text1'].startswith("[city]")):
			poi["icon"] = "icons/marker_town.png"
			return "\n".join([poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']])
		return None

def playerIcons(poi):
	if poi['id'] == 'Player':
		poi['icon'] = "http://overviewer.org/avatar/%s" % poi['EntityId']
		return "%s" % poi['EntityId']

end_lighting = [Base(), EdgeLines(), Lighting(strength=0.5)]
end_smooth_lighting = [Base(), EdgeLines(), SmoothLighting(strength=0.5)]

renders["end"] = {
	"world": "lastingland",
	"title": "The End",
	"rendermode": end_smooth_lighting,
#	"rendermode": [ClearBase(), BiomeOverlay()],
	"dimension": "end",
	"markers": [
		dict(name="Signs", filterFunction=signFilter, createInfoWindow=False, checked=True),
		dict(name="Players", filterFunction=playerIcons, createInfoWindow=False, checked=True),
	],
#	"poititle": "Overlays",
	"showspawn": False,
}


renders["promisedland-day"] = {
	"world": "lastingland",
	"title": "Promised Land - Day",
	"rendermode": smooth_lighting,
	"dimension": "DIM20",
	"markers": [
		dict(name="Signs", filterFunction=signFilter, createInfoWindow=False, checked=True),
		dict(name="Players", filterFunction=playerIcons, createInfoWindow=False, checked=True),
	],
#	"poititle": "Overlays",
	"showspawn": False,
}
#renders["promisedland-night"] = {
#	"world": "lastingland",
#	"title": "Promised Land - Night",
#	"rendermode": smooth_night,
#	"dimension": "DIM20",
#	"markers": [
#		dict(name="Signs", filterFunction=signFilter, createInfoWindow=False, checked=True),
#		dict(name="Players", filterFunction=playerIcons, createInfoWindow=False, checked=True),
#	],
#	"poititle": "Overlays",
#	"showspawn": False,
#}

renders["overworld-day"] = {
	"world": "lastingland",
	"title": "Overworld - Day",
	"rendermode": smooth_lighting,
	"dimension": "overworld",
	"markers": [
		dict(name="Signs", filterFunction=signFilter, createInfoWindow=False, checked=True),
		dict(name="Players", filterFunction=playerIcons, createInfoWindow=False, checked=True),
	],
#	"poititle": "Overlays",
	"showspawn": True,
	"northdirection": "upper-left",
}

renders["overworld-day-2"] = {
	"world": "lastingland",
	"title": "Overworld - Day 2",
	"rendermode": smooth_lighting,
	"dimension": "overworld",
	"markers": [
		dict(name="Signs", filterFunction=signFilter, createInfoWindow=False, checked=True),
		dict(name="Players", filterFunction=playerIcons, createInfoWindow=False, checked=True),
	],
#	"poititle": "Overlays",
	"showspawn": True,
	"northdirection": "lower-right",
}

renders["nether"] = {
	"world": "lastingland",
	"title": "Nether",
	"rendermode": nether_smooth_lighting,
	"dimension": "nether",
	"markers": [
		dict(name="Signs", filterFunction=signFilter, createInfoWindow=False, checked=True),
		dict(name="Players", filterFunction=playerIcons, createInfoWindow=False, checked=True),
	],
#	"poititle": "Overlays",
	"showspawn": False,
}

