const autodraw = require('autodraw')
const { pathDataToPolys } = require('svg-path-to-polygons');


const svgson = require('svgson');
 
// From .svg file 
const fs = require('fs');
fs.readFile('drawing.svg', 'utf-8', function(err, data) {

	//data = data.replace(/\sc\s/g, /\ss\s/); //the c command in inkscape paths is not yet supported

  svgson(data, {}, function(result) {
  	//console.log(result.childs)
	var shapes = objectsToShapes(result.childs)
	//console.log(shapes)

  	autodraw(shapes).then(results => {
  				console.log("position	item	confidence(closer to 0 == more confident)")
				for (var i = results.length - 1; i >= 0; i--) {
					result = results[i]
					console.log((i).toString() + "\t" + result.name + "\t" + result.confidence)
				};
				
			   // array of recognized objects:
			   // * [{
			   // *    name,
			   // *    confidence (closer to 0 == more confident),
			   // *    url (url to a svg representing the object),
			   // *    url_variant_1,
			   // *    url_variant_2
			   // * }]
			   
			})
  });
});

function objectsToShapes(object){
	var shapes = []
  	for (var i = object.length - 1; i >= 0; i--) {
  		element = object[i]

  		if(Array.isArray(element.childs)){ //if the element has sub objects
  			var childShapes = objectsToShapes(element.childs)
  			shapes = shapes.concat(childShapes);
  		}

  		if(element.name == 'path'){ //check every path in autodraw
  			var pointString = JSON.stringify(element.attrs.d)
  			pointString = pointString.substring(1,pointString.length-1)
  			//console.log(pointString)
  			var points = pathDataToPolys(pointString,{ decimals:2});

			//console.log(points);
			var shapesFromPath = shapesMaker(points)
			shapes = shapes.concat(shapesFromPath);
			//console.log(shapes)



  		}

  	};	
  	return shapes
}

function shapesMaker(points){
	var shapes = []
	for (var i = points.length - 1; i >= 0; i--) {
		var closedLine = points[i]
		var shape = [];
		for (var q = closedLine.length - 1; q >= 0; q--) {
			var item = closedLine[q]
			if(closedLine == 'closed'){ //if is end of item
				break;
			}
			var point = {x:item[0],y:item[1]}
				shape.push(point)
			
		};
		shapes.push(shape)
	};
	return shapes
}

// const shape1 = [
//   {
//     x: 10,
//     y: 5
//   },
//   {
//     x: 40,
//     y: 10
//   }
// ]

// const shapes = [
//   shape1
// ]

// autodraw(shapes).then(results => {
// 	console.log(results)
//    array of recognized objects:
//    * [{
//    *    name,
//    *    confidence (closer to 0 == more confident),
//    *    url (url to a svg representing the object),
//    *    url_variant_1,
//    *    url_variant_2
//    * }]
   
// })