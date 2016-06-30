# -*- coding: UTF-8 -*-
# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
import json


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World! This is 25sprout!')

class ParkInfo(webapp2.RequestHandler):
	def handleProcedure(self) :
		error = self.request.get("error",'0')
		data = {}
		park = {}
		
		if int(error) != 1 :
			data['status'] = True
			data['error'] = ''
				
			park['title'] = '新芽動物園'
			park['description'] = '新芽動物園，這裏什麼都沒有，只有一群熱愛NBA的人 (三小！？)'
			park['address'] = '我已經建在大都這裏了，想要入園的話就來大都找我吧'
			park['tel'] = '你覺得大都會有電話嗎？    當然有：0936-882338'

		else:
			data['status'] = False
			data['error'] = 'Something goes wrong'
		

		data['park'] = park

		json_data = json.dumps(data)

		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write(json_data)

	def post(self):
		self.handleProcedure()

	def get(self) :
		self.handleProcedure()

class AreaList(webapp2.RequestHandler):

	def handleProcedure(self):
		error = self.request.get("error",'0')
		data = {}
		area_list = []
		
		if int(error) != 1 :
			data['status'] = True
			data['error'] = ''
				
			area1 = {}
			area1['ID'] = 0
			area1['title'] = '屍樂園'
			area1['description'] = '一群肚子很餓的傢伙們'
			area1['img'] = 'http://blogs-images.forbes.com/erikkain/files/2016/02/Amazon-Zombies-1200x801.jpg'

			area2 = {}
			area2['ID'] = 1
			area2['title'] = 'Mutant'
			area2['description'] = '一群身體很變異的傢伙們'
			area2['img'] = 'http://cdn.worldscreen.com.tw/uploadfile/201505/goods_007905_140502.jpg'

			area3 = {}
			area3['ID'] = 2
			area3['title'] = '25sprout'
			area3['description'] = 'sprouters'
			area3['img'] = 'https://scontent-tpe1-1.xx.fbcdn.net/v/t1.0-9/13087318_762220620581596_6311241624767418684_n.jpg?oh=eca7d704c8bfe2ee427a80112f1ece49&oe=57EE2F44'			

			area_list.append(area1)
			area_list.append(area2)
			area_list.append(area3)

		else:
			data['status'] = False
			data['error'] = 'Something goes wrong'
		

		data['area_list'] = area_list

		json_data = json.dumps(data)

		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write(json_data)

	def post(self):
		self.handleProcedure()

	def get(self) :
		self.handleProcedure()

class AreaInfo(webapp2.RequestHandler):
	def handleProcedure(self) :
		areaID = self.request.get("area_id",'-1')
		error = self.request.get("error",'0')
		data = {}
		area = {}
		
		if int(error) != 1 and int(areaID) >= 0 and int(areaID) <= 2:
			data['status'] = True
			data['error'] = ''
			animalsList = []

			if int(areaID) == 0 :
				area['ID'] = 0
				area['title'] = '屍樂園'
				area['description'] = '一群肚子很餓的傢伙們'
				area['img'] = 'http://blogs-images.forbes.com/erikkain/files/2016/02/Amazon-Zombies-1200x801.jpg'

				animal1 = {}
				animal1['ID'] = 0
				animal1['title'] = 'Weaking Dead'
				animal1['img'] = 'http://thebloodtheatre.com/wp-content/uploads/2013/02/the-walking-dead-3-the-walking-dead-24037474-500-333.jpg'

				animal2 = {}
				animal2['ID'] = 1
				animal2['title'] = 'Resident Evil'
				animal2['img'] = 'http://pic.pimg.tw/joeman/2399cfa5cab4aa78e8a56de98e939e88.jpg'

				animal3 = {}
				animal3['ID'] = 2
				animal3['title'] = 'World War Z'
				animal3['img'] = 'http://link.photo.pchome.com.tw/s13/hatsocks75/851/137195529019/'

				animalsList.append(animal1)
				animalsList.append(animal2)
				animalsList.append(animal3)

				area['animals_list'] = animalsList
			elif int(areaID) == 1:
				area['ID'] = 1
				area['title'] = 'Mutant'
				area['description'] = '一群身體很變異的傢伙們'
				area['img'] = 'http://cdn.worldscreen.com.tw/uploadfile/201505/goods_007905_140502.jpg'

				animal1 = {}
				animal1['ID'] = 10
				animal1['title'] = 'Magneto'
				animal1['img'] = 'http://vignette2.wikia.nocookie.net/marvelmovies/images/6/65/Magneto_-_Past.png/revision/latest?cb=20140219112937'

				animal2 = {}
				animal2['ID'] = 11
				animal2['title'] = 'Professor x'
				animal2['img'] = 'http://vignette4.wikia.nocookie.net/shipping/images/8/8c/~X-Men_$Charles_Xavier_*1.png/revision/latest?cb=20140531084805'

				animalsList.append(animal1)
				animalsList.append(animal2)
				area['animals_list'] = animalsList
			else :
				area['ID'] = 2
				area['title'] = '25sprout'
				area['description'] = 'sprouters'
				area['img'] = 'https://scontent-tpe1-1.xx.fbcdn.net/v/t1.0-9/13087318_762220620581596_6311241624767418684_n.jpg?oh=eca7d704c8bfe2ee427a80112f1ece49&oe=57EE2F44'

				animal1 = {}
				animal1['ID'] = 20
				animal1['title'] = 'Alex'
				animal1['img'] = 'https://scontent-tpe1-1.xx.fbcdn.net/v/t1.0-9/13124514_10153601676569677_2131607325507427168_n.jpg?oh=99b3e30c8279536fb0af2cd946a71475&oe=58345ED0'

				animal2 = {}
				animal2['ID'] = 21
				animal2['title'] = 'Thundersha'
				animal2['img'] = 'https://scontent-tpe1-1.xx.fbcdn.net/v/t1.0-9/12043051_10201501767903884_3444857786651760104_n.jpg?oh=afece1b2ce0e40661b2069eb4cdc0a70&oe=57ED3AAF'

				animalsList.append(animal1)
				animalsList.append(animal2)
				area['animals_list'] = animalsList
		else:
			data['status'] = False
			if int(areaID) == -1 :
				data['error'] = 'You have to give area_id'	
			else :
				data['error'] = 'Something goes wrong'
		

		data['area'] = area

		json_data = json.dumps(data)

		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write(json_data)

	def post(self):
		self.handleProcedure()

	def get(self) :
		self.handleProcedure()


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/park_info', ParkInfo),
    ('/area_list', AreaList),
    ('/area_info', AreaInfo),
], debug=True)
