import atb.ont.models.lan
  
  
def test_lan_vlan_config(web):
    # Create a new Lan Vlan object
    lan_vlan_config = atb.ont.models.lan.LanVlanSetting(lan_port='eth1', enable_vlan_mode=True,
                                                        vlans={'2': '2', '3': '3'})
    # Pass the object to the edit function (which will return the newly configured object)
    new = web.edit_lan_vlan_config(lan_vlan_config)[0]
    # Check that they are the same
    assert new == lan_vlan_config, "LAN VLAN config in GUI (%s) does not match the desired config " \
                                   "(%s)" % (new.__dict__, lan_vlan_config.__dict__)
 
    # Repeat the above steps with different options
    lan_vlan_config = atb.ont.models.lan.LanVlanSetting(lan_port='eth1', enable_vlan_mode=False,
                                                        vlans={'4': '4', '5': '5', '7': '8'})
    new = web.edit_lan_vlan_config(lan_vlan_config)[0]
    assert new == lan_vlan_config, "LAN VLAN config in GUI (%s) does not match the desired config " \
                                   "(%s)" % (new.__dict__, lan_vlan_config.__dict__)