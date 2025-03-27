# This is a configuration file for Houdini it runs whenever houdini launches or a scene is loaded.
import os
import hou

# Hide the TaleSpire Shared Data node from users, it is best if this node is handled by the system.
# To make this node available set an environment variable HTTGT_DEV = 1
dev_mode = os.getenv("HTTGT_DEV", "0") == "1"

hidden_node_types = ["Object/TaleSpire_Shared_Data", "Object/TaleSpire_Proxy_Object"]

for node_type in hidden_node_types:
    node_type = hou.nodeType(node_type)
    node_type.setHidden(not dev_mode)
