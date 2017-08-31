import geoplotlib
from geoplotlib.utils import read_csv, BoundingBox

thedata = geoplotlib.utils.read_csv('kurj_log.csv')
geoplotlib.hist(thedata, colorscale='sqrt', binsize=4, scalemin=0, scalemax=100)
# geoplotlib.set_bbox(BoundingBox.DK)
geoplotlib.show()