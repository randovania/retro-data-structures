meta:
  id: mlvl
  file-extension: MLVL
  endian: be
doc-ref: https://wiki.axiodl.com/w/MLVL_(File_Format)

seq:
  - id: magic
    contents: [0xDE, 0xAF, 0xBA, 0xBE]
    
  - id: version
    contents: [0x00, 0x00, 0x00, 0x19]
    
  - id: world_name_id
    type: asset_id
    doc: STRG
    
  - id: temple_key_world_index
    type: u4

  - id: world_save_info_id
    type: asset_id
    doc: SAVW

  - id: default_skybox_id
    type: asset_id
    doc: CMDL
    

  - id: area_count
    type: u4
    
  - id: areas
    type: mlvl_area
    repeat: expr
    repeat-expr: area_count
    
  - id: world_map_id
    type: asset_id
    doc: MAPW
    
  - type: u1
    doc: Unknown. This is presumably the same unknown value as at the beginning of the SCLY format. Always 0.
    
  - id: script_instance_count
    type: u4
    doc: The MLVL format embeds a script layer. This script layer is used in the MP1 demo for storing Dock instances, but it's unused in all retail builds, so this is always 0.
    
    
  # Area Layer Flags
  - id: area_layer_count
    type: u4
    doc: Always equal to area_count
  
  - id: area_layer_flags
    type: mlvl_area_layer_flags
    repeat: expr
    repeat-expr: area_layer_count
    
  # Layer Name
  - id: layer_name_count
    type: u4
    
  - id: layer_names
    type: str
    encoding: ascii
    terminator: 0
    repeat: expr
    repeat-expr: layer_name_count
    
  # Layer GUID
  - id: layer_guid_count
    type: u4
    doc: uses area_count instead
    
  - id: layer_guid
    type: guid
    repeat: expr
    repeat-expr: layer_guid_count
    
  # Layer Name Offset
  - id: area_layer_name_offset_count
    type: u4
    doc: Always equal to area_count

  - id: area_layer_name_offset
    type: u4
    repeat: expr
    repeat-expr: area_count
    
types:
  asset_id:
    seq:
      - id: value
        type: u8
        
  guid:
    seq:
      - id: value
        size: 16
        
  mlvl_area:
    seq:
      - id: area_name_id
        type: asset_id
        doc: STRG
        
      - id: area_transform
        type: f4
        repeat: expr
        repeat-expr: 12
        
      - id: area_bounding_box
        type: f4
        repeat: expr
        repeat-expr: 6
        
      - id: area_mrea_id
        type: asset_id
        doc: MREA
        
      - id: internal_area_id
        type: asset_id
        
      - id: attached_area_index_count
        type: u4
        
      - id: attached_area_index
        type: u2
        repeat: expr
        repeat-expr: attached_area_index_count
        
      - id: docks_count
        type: u4
        
      - id: docks
        type: mlvl_dock
        repeat: expr
        repeat-expr: docks_count
        
      - id: internal_area_name
        type: str
        encoding: ascii
        terminator: 0
        
  mlvl_dock:
    seq:
      - id: connecting_dock_count
        type: u4
        
      - id: connecting_dock
        type: mlvl_connecting_dock
        repeat: expr
        repeat-expr: connecting_dock_count
        
      - id: dock_coordinates_count
        type: u4
      - id: dock_coordinates
        type: vector3
        repeat: expr
        repeat-expr: dock_coordinates_count
       
  mlvl_connecting_dock:
    seq:
      - id: area_index
        type: u4
      - id: dock_index
        type: u4

  mlvl_area_layer_flags:
    seq:
      - id: layer_count
        type: u4
      - id: layer_flags
        type: u8
        
  vector3:
    seq:
      - id: value
        type: f4
        repeat: expr
        repeat-expr: 3
