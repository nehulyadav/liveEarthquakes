import re
import json

with open ("latitude.txt") as f:
	with open ("longitude.txt") as f1:
		with open ("mag.txt") as f2:
			with open('input.json', 'w') as outfile:
				d = f.readlines()
				d1 = f1.readlines()
				d2 = f2.readlines()
				json.dump('[', outfile)
				for i in range (1,4):
					pos = d1[i].find(',')
					posM = d2[i].find(',' '')
					num = ['', '"1"', '"2"', '"3"']
					s = '[' + num[i] + ', ' + '[' + re.sub('0Z,' , '', d[i]) + d1[i][pos:d1[i].find(',', pos+1)] + d2[i][posM:d2[i].find(',' '', posM+1)] + ']]' + ', '
					json.dump(s[2:], outfile)
				json.dump("]", outfile)
				