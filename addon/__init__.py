# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "ScenePopulator",
    "author" : "yacine_Bu",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Object"
}

import bpy
from . Operator import Operator_OT_
from . Panel import Panel_PT_

classes = (Operator_OT_, Panel_PT_)
props = bpy.props
myProps = (
    ("quantity", props.IntProperty(name="quantity")),
    ("xCenter", props.IntProperty(name="X Center")),
    ("yCenter", props.IntProperty(name="Y Center")),
    ("radius", props.FloatProperty(name="radius"))
)

def register():
    for c in classes:
        bpy.utils.register_class(c)

    for (propName, propValue) in myProps:
        setattr(bpy.types.Scene, propName, propValue)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    
    for (propName, osef) in myProps:
        delattr(bpy.types.Scene, propName)

if __name__ == '__main__':
    pass