$(document).ready(function() {
   var onCountryClick = function(target) {
      window.location='/list/'+target.iso2+"/";
   };
   $(function() {
        window.map = $K.map('#map');
        map.loadMap('/site_media/eu.svg', function(map) {
            map
                .addLayer('eu', 'bgback')
                .addLayer('eu', 'bg')
                .addLayer('eu', 'bgstroke')
                .addLayer({'id': 'countries', 'className': 'context'})
                .addLayer('graticule')
                .addLayer({'id': 'eu',
                           'className': 'fg',
                           'tooltip': {
                              content: function(obj,foo) {
                                 var count=0;
                                 if(data) {
                                    for(var i=0;i<data.length;i++) {
                                       if(data[i].iso2==foo.data.iso2) {
                                          count=data[i].w;
                                          break;
                                       }
                                    }
                                 }
                                 if(count>0) {
                                    return foo.data.name+"<br />"+count+" reported cases";
                                 } else {
                                    return foo.data.name;
                                 }
                              }
                           },
                           'key': "iso2"
                          });

            map.onLayerEvent('click', onCountryClick, 'fg')

            map.addFilter('oglow', 'glow', { size: 3, color: '#988', strength: 1, inner: false });
            map.getLayer('bgback').applyFilter('oglow');

            map.addFilter('myglow', 'glow', { size: 2, color: '#945C1B', inner: true });
            map.getLayer('bg').applyFilter('myglow');

				colorscale = new chroma.ColorScale({
					colors: chroma.brewer.YlGnBu,
					limits: chroma.limits(data, 'q', 6, 'w')
				});

            if(data) {
               map.choropleth({
                  data: data,
                  layer: 'fg',
                  key: 'iso2',
                  colors: function(d) {
                     if (d == null) return '#fff';
                     return colorscale.getColor(d['w']);
                  },
                  duration: 0
               });
            } 
        });
    });
});
