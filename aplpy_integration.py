import aplpy
import cartavis
import astroquery as aq
# Bring in unit definitions.
import astropy.units as u


# Find an object that could be in the data.
target = aq.Simbad.query_object('NGC2024')

# Borrowed from: http://aplpy.readthedocs.org/en/stable/slicing.html

f = aplpy.FITSFigure('L1448_13CO.fits.gz', slices=[222],
                     figsize=(5,5))
f.show_colorscale()
f.add_grid()
f.tick_labels.set_font(size='xx-small')
f.axis_labels.set_font(size='x-small')
f.save('slicing_1.png')

# this grabs information from aplpy object and launches viewer as appropriate.
v = cartavis.from_aplpy(f)
v.launch()

######################################################
# Alternatively, grab a chunk of data out of core with image and WCS info
img1 = cartavis.openFile("casa1.img")
img1.extractSpatial(center=[target.ra,target.dec],size=1*u.deg)
img1.extractSpectral(center = 1.3*u.GHz, size=20*u.MHz)
img1.extractStokes('LR')
img1.extract()

f = aplpy.CARTAFigure(img1)
f.show_colorscale()
f.add_grid()
f.tick_labels.set_font(size='xx-small')
f.axis_labels.set_font(size='x-small')
f.save('STOKES.png')
