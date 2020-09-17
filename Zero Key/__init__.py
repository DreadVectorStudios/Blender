# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	 See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


bl_info = {
    "name": "Zero Key",
    "author": "Brad Clark Rigging Dojo",
    "version": (1, 1),
    "blender": (2, 80, 0),
    "location": "",
    "description": "Maya and Motionbuilder toold,Must have tool to work with Animation NLA layers. Sets a zero key for the control to blend back to the sorce motion",
    "warning": "",
    "wiki_url": "",
    "category": "Animation",
}



import bpy

obj = bpy.context.active_object
selBones = bpy.context.selected_pose_bones


#insert keyframes on the selected bones on the current frame
if bpy.context.selected_pose_bones == None:
    print ("You must have a selection to keyframe")
    
else:
    
    for bone in bpy.context.selected_pose_bones: 
        bone.location = 0.0, 0.0, 0.0   
        bone.keyframe_insert(data_path="location", index=-1)
        
        bone.rotation_quaternion = 1.0, 0.0, 0.0, 0.0
        if bone.rotation_mode == 'QUATERNION':
            bone.keyframe_insert(data_path="rotation_quaternion", index=-1, options={'INSERTKEY_VISUAL'})
        else: 
            bone.rotation_euler = 0.0, 0.0, 0.0  
            bone.keyframe_insert(data_path="rotation_euler", index=-1, options={'INSERTKEY_VISUAL'})
            
  
bpy.context.view_layer.update()