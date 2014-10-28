import cartavis

# https://github.com/astropy/astroquery
import astroquery as aq

# Bring in unit definitions.
import astropy.units as u

# Find an object that could be in the data.
target = aq.Simbad.query_object('NGC2024')

# Apply vs. set vs. show syntax.  Layer sets plot order.  
# Default to the call order in the script.

v = cartavis.start()
v.openFile("1.fits",layer=0)

# Select a clip value and a colour map.
v.applyAutoClip(95)
v.applyColormap( "helix1",layer=0)
v.applyType("raster",layer=0)

# Select a file to contour as an overlay.
v.openFile("2.fits",layer=1)
v.applyType("contour")
v.applyContours(percentile_range=95,Ncontour=5,layer=1)

# This plots a single contour at a level of 0 in the data.
v.openFile("3.fits",layer=2)
v.applyType("contour")
v.applyContours(values=np.array([0]),layer=2)

# Picking a coordinate system by default labels the coordinates 
# in the right system.
v.applyCoordinates(system='Galactic')

# Set the image to centre on a specific coordinate in the data.
v.applyCenter(target.ra,target.dec)
v.applySize(2*u.deg)

# Integrate over a specific velocity range of a data cube
v.applyIntegration( min=-20*u.km/u.s, \
					max=20*u.km/u.s, \
					restfrequency=115.271204*u.GHz)


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

# Load a DS9 region file and overlay it on the file.
reg = cartavis.loadRegions('ngc2024_objects.reg')
reg.overlay()

# snapshot to PNG
v.setResolution( 1000, 1000)
v.saveScreenshot( "/scratch/1.png")

# render to PDF for publication quality file.
# Ignores resolution?
# File size figures in inches?
v.saveRender("/scratch/1.pdf",size=(5,5))

# Launch an interactive viewer with the same view.
v.launch()