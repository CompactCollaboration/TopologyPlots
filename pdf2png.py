from pdf2image import convert_from_path

for topology in [
	"E1", "E2", "E3", "E4", "E5", "E6",
	"E7", "E8","E9", "E10", "E11", "E12",
	"E13", "E14", "E15", "E16i", "E17", "E18",
]:
	try:
		image = convert_from_path(f"./{topology}/{topology}.pdf")

		for page in image:
			page.save(f"./{topology}/{topology}.png", "PNG")
	except:
		pass
