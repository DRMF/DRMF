# Example Modules

## test.click

```js
/*
	example1.js - An example module for JOBAD. 
	A Testing module, colors <p>s in the color given as first parameter. 
	
	Copyright (C) 2013 KWARC Group <kwarc.info>
	
	This file is part of JOBAD.
	
	JOBAD is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.
	
	JOBAD is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.
	
	You should have received a copy of the GNU General Public License
	along with JOBAD.  If not, see <http://www.gnu.org/licenses/>.	
*/
(function($){
	JOBAD.modules.register({
		info:{
			'identifier':	'test.click',
			'title':	'Click testing module',
			'author':	'Tom Wiesing',
			'description':	'A Testing module, colors <p>s in the color given as first parameter. ',
			'hasCleanNamespace': false
		},
		init: function(JOBADInstance, color){
			this.localStore.set("color", color); //Store the color setting
		},
		leftClick: function(target, JOBADInstance){
			if(target.is("p")){
				this.colorize(target); //Color the target
			}
		},
		colorize: function(target){
			target.css("color", this.localStore.get("color")); //get the color setting and apply it. 
		}
	});
})(JOBAD.refs.$);
```

## test.menu1

```js
/*
	example2.js - An example module for JOBAD. 
	Provides a context menu entry which checks if the clicked element is a <p>. 
	
	Copyright (C) 2013 KWARC Group <kwarc.info>
	
	This file is part of JOBAD.
	
	JOBAD is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.
	
	JOBAD is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.
	
	You should have received a copy of the GNU General Public License
	along with JOBAD.  If not, see <http://www.gnu.org/licenses/>.
*/
(function($){
	JOBAD.modules.register({
		info:{
			'identifier':	'test.menu1',
			'title':	'Paragraphs Module',
			'author':	'Tom Wiesing',
			'description':	'Provides a context menu entry which checks if the clicked element is a <p>. '
		},
		globalinit: function(){
			//source: http://openiconlibrary.sourceforge.net/gallery2/?./Icons/status/dialog-declare.png (license: GPLv2)
			JOBAD.resources.provide("icon", "test.question", "data:image/png;base64,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etv/2tGmz21zv3Usl7MPV2o17ovk+O8AEqnJMVF8CJhxDK2Stk1CTNc4GkUTZdbD6m/f295YXvvrmyv+L9H6u9ZBGB92uEvu6vx2bhL3I8/7VCFnz1TrVRZKxFvEFOjMh1IHXFq/rvcV36d+/HlT55gqWSizHlauXGot3/rwtfb25t96N/9+fZx1HpUAgKuitfK1dXvi3mbUbR/OO/psrV7lTNMRRBJqcKa5Pxp8BOTAQiNWyls6ZiomCrKDld9e2lm/ufwahdrfrLz3izt4yAPAR3zAcTFsr31xtVRtfdjrtBsaovlGtWzk8zkoxJsXRVmRYvWTqpJRfwjcNjQ0iiZmChyyuaY+uvL+8tqd1Veb6L2++u6rDwX/OxAAgHfD5trXVoy6eyX0miLc250rWFqxPlFihZwFztlgQ98nwFjK95xB4wyGxlGwdDSKFqaLGnKig+3bV72Prn3wbnN952e31nr/4P3Xz1ceZJuMUI9OYEh6dvb7M9pROlfMF8+XGvXnyzOH6061oQndgS85Qhl3aaKh6pbO4RgctkawmIBw29TeXPN3Vldu7DXbb+757Jdr/7G+9Id+Spla553qGWe+YthnbCv/Yq5c+ROnPDFnl0qOlStommUzTTcYGAMnBSVCEn5Phd1O5LZau93W7lKv23k79K23P2zevobrb7bwezzw/kSe1M8/59Ys7i5K0o87ee2EbpiLnGt1phs5RsQAipSSrSiINkI/uiWF+oCHpRu3o9XNZDz433hSv29pwAUN2HAOHao5nrNZlLmqWQHQNgKpewi3ZkQX0ZKHixdDAOHHvN//rz+K9d9RpiYa4ycH5gAAAB10RVh0Q29tbWVudABDcmVhdGVkIHdpdGggVGhlIEdJTVDvZCVuAAAAJXRFWHRjcmVhdGUtZGF0ZQAyMDA5LTExLTE3VDIwOjA2OjU4LTA3OjAwOHFLewAAACV0RVh0ZGF0ZTpjcmVhdGUAMjAxMC0wMi0yMFQxOToyMjo0Mi0wNzowMMSpj+wAAAAldEVYdGRhdGU6bW9kaWZ5ADIwMTAtMDEtMTFUMTQ6MTk6NDYtMDc6MDA5MaJ3AAAANHRFWHRMaWNlbnNlAGh0dHA6Ly9jcmVhdGl2ZWNvbW1vbnMub3JnL2xpY2Vuc2VzL0dQTC8yLjAvbGoGqAAAACV0RVh0bW9kaWZ5LWRhdGUAMjAwOS0xMS0xN1QyMDowNjo1OC0wNzowMGfAPU8AAAAYdEVYdFNvdXJjZQBJbnRyaWd1ZSBJY29uIFNldK4noT8AAABGdEVYdFNvdXJjZV9VUkwAaHR0cDovL3NpbXBsZWlubm92YXRpb24ubmV0L2luZGV4LnBocD9wYWdlPTIyJnNvdXJjZT0yJmlkPTKVQfnGAAAAAElFTkSuQmCC")
		},
		contextMenuEntries: function(target){
			if(target.is('#nomenu,#nomenu *')){ //no menu for these elements
				return false;
			}
			return [
				["Am I a <p> ?", function(element){
					if(element.is("p")){
						alert("I am a <p> element. ");
					} else {
						alert("No I'm not. ");
					}
				}, "test.question"]
			];
		}
	});
})(JOBAD.refs.$);
```

## test.menu2

```js
/*
	example3.js - An example module for JOBAD. 
	Test the menu and adds several items. 
	
	Copyright (C) 2013 KWARC Group <kwarc.info>
	
	This file is part of JOBAD.
	
	JOBAD is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.
	
	JOBAD is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.
	
	You should have received a copy of the GNU General Public License
	along with JOBAD.  If not, see <http://www.gnu.org/licenses/>.
*/
(function($){
	JOBAD.modules.register({
		info:{
			'identifier':	'test.menu2',
			'title':	'Menu Testing module',
			'author':	'Tom Wiesing',
			'description':	'Test the menu and adds several items. '
		},
		globalinit: function(){
			//icon: http://openiconlibrary.sourceforge.net/gallery2/?./Icons/categories/applications-graphics-2.png (license: GPLv2)
			JOBAD.resources.provide("icon", "test.color", "data:image/png;base64,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")
		},
		contextMenuEntries: function(target, JOBADInstance){
			if(target.is('#nomenu,#nomenu *')){
				return false;
			}
			return [
				["Colors",  
					{
						"Make me orange": function(element){element.css("color", "orange");}, 
						"Highlight my background": function(element){
							element
							.stop().css("background-color", "#FFFF9C")
							.animate({ backgroundColor: "#FFFFFF"}, 1500);
						},
						"Revert": function(element){element.stop().css('color', '');}
					}, 
				"test.color"
				]
			];
		}
	});
})(JOBAD.refs.$);
```

## test.hover

```js
/*
	example4.js - An example module for JOBAD. 
	Counts the words in a paragraph and shows a tooltip. 
	
	Copyright (C) 2013 KWARC Group <kwarc.info>
	
	This file is part of JOBAD.
	
	JOBAD is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.
	
	JOBAD is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.
	
	You should have received a copy of the GNU General Public License
	along with JOBAD.  If not, see <http://www.gnu.org/licenses/>.
*/
(function($){
	JOBAD.modules.register({
		info:{
			'identifier':	'test.hover',
			'title':	'Hover Test menu',
			'author':	'Tom Wiesing',
			'description':	'Counts the words in a p element. ',
		},
		hoverText: function(target){
			if(target.is("p")){
				var wordCount = (target.text().split(" ").length+1).toString()
				return "I am a p element which contains "+wordCount+" words. ";
			}
		}
	});
})(JOBAD.refs.$);
```

## test.sidebar

```js
/*
	example5.js - An example module for JOBAD. 
	
	Counts the words in a paragraph and shows a tooltip in the sidebar. 
	Currently also serves as an example for UserConfig. 
	
	Copyright (C) 2013 KWARC Group <kwarc.info>
	
	This file is part of JOBAD.
	
	JOBAD is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.
	
	JOBAD is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.
	
	You should have received a copy of the GNU General Public License
	along with JOBAD.  If not, see <http://www.gnu.org/licenses/>.
*/
(function($){
	JOBAD.modules.register({
		info:{
			'identifier':	'test.sidebar',
			'title':	'Sidebar Test',
			'author':	'Tom Wiesing',
			'description':	'Displays the number of characters next to every p and clicking it trigger the original p. '
		},
		init: function(JOBADInstance){
			//add a bunch of notifications
			var classes = ["info", "warning", "error"];
			JOBADInstance.element.find("p")
			.each(function(i, target){
				var $target = $(target);
				JOBADInstance.Sidebar.registerNotification($target, {
					"text": $target.text().length.toString()+" Characters of text",
					"trace": true, 
					"class": classes[i % 3],
					"click": function(){
							JOBADInstance.Event.leftClick.trigger($target);
					},
					"menu": [["Remove this notification", function(element, JOBADInstance){
						JOBADInstance.Sidebar.removeNotification($(this));
					}]]
				});
				JOBADInstance.Sidebar.registerNotification($target, {
					"text": "A second something. ",
					"trace": true,
					"class": classes[(i+1) % 3],
					"click": function(){
							JOBADInstance.Event.leftClick.trigger($target);
					},
					"menu": [["Remove this notification", function(element, JOBADInstance){
						JOBADInstance.Sidebar.removeNotification($(this));
					}]]
				});
			})
		}
	});
})(JOBAD.refs.$);
```

## test.folding

```js
/*
	example6.js - An example module for JOBAD. 
	Tests folding an created some menu icons. 
	
	Copyright (C) 2013 KWARC Group <kwarc.info>
	
	This file is part of JOBAD.
	
	JOBAD is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.
	
	JOBAD is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.
	
	You should have received a copy of the GNU General Public License
	along with JOBAD.  If not, see <http://www.gnu.org/licenses/>.
*/
(function($){
	JOBAD.modules.register({
		info:{
			'identifier':	'test.folding',
			'title':	'Folding module',
			'author':	'Tom Wiesing',
			'description':	'This testing module tests folding. '
		},
		globalinit: function(){
			//icon source: http://openiconlibrary.sourceforge.net/gallery2/?./Icons/actions/view-sort-descending-2.png, license: lgpl
			JOBAD.resources.provide("icon", "test.folding", "data:image/png;base64,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");
		},
		contextMenuEntries: function(target, JOBADInstance){
			if(target.is('#nomenu,#nomenu *')){
				return false;
			}
			var entries = [
				["Folding",  {
					"Trigger on this JOBAD Instance": function(){
						if(JOBADInstance.Folding.isEnabled(JOBADInstance.element)){ //check if folding is enabled on the overall element
							JOBADInstance.Folding.disable(); 
						} else {
							JOBADInstance.Folding.enable(); 
						}
					},
					"Trigger on this element": function(element){
						if(JOBADInstance.Folding.isEnabled(element)){ //check if folding is enabled on the overall element
							JOBADInstance.Folding.disable(element); 
						} else {
							JOBADInstance.Folding.enable(element); 
						}
					}
				}, "test.folding"]
			];
			return entries; 
		}
	});
})(JOBAD.refs.$);
```

## test.config

```js
/*
	example7.js - An example module for JOBAD. 
	Shows several menu items for testing some of the features of JOBAD. 
	
	Copyright (C) 2013 KWARC Group <kwarc.info>
	
	This file is part of JOBAD.
	
	JOBAD is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.
	
	JOBAD is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.
	
	You should have received a copy of the GNU General Public License
	along with JOBAD.  If not, see <http://www.gnu.org/licenses/>.
*/
(function($){
	JOBAD.modules.register({
		info:{
			'identifier':	'test.config',
			'title':	'Config Tester',
			'author':	'Tom Wiesing',
			'description':	'This testing module tests the config dialog. '
		},
		config: {
			"test": ["string", function(x){return x[0] == "d";}, "default-value-goes-here", ["String", "Has to start with d"]],
			"bool": ["bool", false, ["Boolean", "Another awesome setting. "]],
			"num": ["number", [-10, 10], 0, ["Number", "An awesome number between -10 and 10. "]],
			"int": ["integer", [-10, 10], 0, ["Integer", "An awesome integer between -10 and 10. "]],
			"alist": ["list", [1, 2, 3, 4], 1, ["Select an option", "Auto", "Yes", "No", "Perhaps"]]
		},
		globalinit: function(){
			//icon source: http://openiconlibrary.sourceforge.net/gallery2/?./Icons/actions/configure-5.png, license: gplv2
			JOBAD.resources.provide("icon", "test.config", "data:image/png;base64,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")
		},
		contextMenuEntries: function(target, JOBADInstance){
			if(target.is('#nomenu,#nomenu *')){
				return false;
			}
			return [
				["Show Config UI", function(element){
					JOBADInstance.showConfigUI();
				}, "test.config"]
			];
		}
	});
})(JOBAD.refs.$);
```