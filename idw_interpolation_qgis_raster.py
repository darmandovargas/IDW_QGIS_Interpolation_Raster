# IDW QGIS Interpolation Raster Code
# author Diego Vargas <darmandovargas@gmail.com> <diego@thinkcloudgroup.com>
import qgis.analysis
from qgis.core import *

app = QgsApplication([],True)
QgsApplication.setPrefixPath(r"/Applications/QGIS.app/Contents/MacOS", True)
QgsApplication.initQgis()

uri = QgsDataSourceURI()
uri.setConnection("localhost", "5432", "dbname", "dbusername", "dbpassword")
uri.setDataSource ("schema", "table1", "columntb1")
layer = QgsVectorLayer(uri.uri() ,"layername","dbuser")

uri2 = QgsDataSourceURI()
uri2.setConnection("localhost", "5432", "dbname", "dbusername", "dbpassword")
uri2.setDataSource ("schema", "table2", "columntb2")
layer2 = QgsVectorLayer(uri2.uri() ,"layername","dbuser")

# Layer 2

ld1 = qgis.analysis.QgsInterpolator.LayerData()
ld1.vectorLayer = layer
ld1.zCoordInterpolation=False
ld1.InterpolationAttribute = 1 #column index, start with 0
ld1.mInputType = 1

ld2 = qgis.analysis.QgsInterpolator.LayerData()
ld2.vectorLayer = layer2
ld2.zCoordInterpolation=False
ld2.InterpolationAttribute = 5 #column index, start with 0
ld2.mInputType = 1

itp = qgis.analysis.QgsIDWInterpolator([ld1, ld2])

pathToAscFileSave = "/yourpath/idw_interpolation.asc"

rect = layer.extent()
test = qgis.analysis.QgsGridFileWriter(itp,pathToAscFileSave,rect,100,100,0.1,0.1)
test.writeFile(True) #Creating .asc raster
