import cartavis

# https://github.com/astropy/astroquery
import astroquery as aq

# Bring in unit definitions.
import astropy.units as u

# Find an object that could be in the data.
target = aq.Simbad.query_object('NGC2024')


# This script uses a set of data objects and a plot container paradigm.
# apply methods act on data objects
# set methods act on the plot containers
# show methods control overlays.


v = cartavis.start()

# Select a clip value and a colour map.
img1 = cartavis.openFile("1.fits")
img1.applyAutoClip(95)
img1.applyColormap( "helix1",layer=0)
img1.applyType("raster",layer=0)

# Integrate over a specific velocity range of a data cube
img1.applyIntegration( min=-20*u.km/u.s, max=20*u.km/u.s,
	restfrequency=115.271204*u.GHz)



# Select a file to contour as an overlay.
img2 = cartavis.openFile("2.fits")
img2.applyType("contour")
img2.applyContours(percentile_range=95,Ncontour=5)

# This plots a single contour at a level of 0 in the data.
img3 = openFile("3.fits")
img3.applyType("contour")
img3.applyContours(values=np.array([0]))

# Compose a plot container
v.addLayer([img1,img2,img3])

# Load a DS9 region file and overlay it on the file.
reg = cartavis.loadRegions('ngc2024_objects.reg')
v.addLayer(reg)

# Picking a coordinate system by default labels the coordinates 
# in the right system.
v.setCoordinates(system='Galactic')

# Set the image to centre on a specific coordinate in the data.
v.setCenter(target.ra,target.dec)
v.setSize(2*u.deg)

# Add a custom annotation
v.addMarker(target.ra+0.235*u.deg, 
	target.dec-0.184*u.deg, marker = '+', label='Here there be dragons')

# Show a color bar.
v.showColorbar(title='Brightness (K)')

# Define a Scale Bar and set a position within the plot window (1 = upper left,
# 2 = upper middle, 3 = upper right, etc.)
v.showScalebar(length=2*u.AU,title='2 AU',pos=9)


# Pick plotting parameters
v.setFont(family='Times',size=14)
v.setTitle('NGC 2024 in Radiocontinuum')

# Show a beam and set a position within the plot window (1 = upper left,
# 2 = upper middle, 3 = upper right, etc.)
v.showBeam(pos=2)

# Display an overlaid grid?
v.showGrid(linestyle='--')

# snapshot to PNG
v.setResolution( 1000, 1000)
v.saveScreenshot( "/scratch/1.png")

# render to PDF for publication quality file.
# Ignores resolution?
# File size figures in inches?
v.saveRender("/scratch/1.pdf",size=(5,5))

# Launch an interactive viewer with the same view.
v.launch()