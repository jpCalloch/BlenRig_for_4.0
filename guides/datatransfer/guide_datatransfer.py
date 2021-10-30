from os.path import dirname, join
from .. datatransfer.guide_datatransfer_actions import *

images_dir = join(dirname(__file__), 'images')

GUIDE_STEPS_DATATRANSFER = (
    #Introduction
    {
        'imagen': 'DT_Intro.jpg',
        'titulo': {
            'EN': 'Introduction',
            'ES': 'Introducción'
            },
        'texto': {
            'EN': "In this Guide you will Transfer the Weights from the BlenRig pre-weighted Meshes to the meshes of your character. This will give you a first weighting iteration that will let you continue with the rigging process",
            'ES': 'En esta guía transferirás los pesos de las mallas pre-pesadas de BlenRig a las mallas de tu personaje. Esto le dará una primera iteración de pesos que le permitirá continuar con el proceso de rigging'
            },
        'accion': DT_Intro
    },
    #Edit Weith Transfer Model Head Shape
    {
        'imagen': ('DT_Weight_Mesh_Shapekey_Head_A.jpg', 'DT_Weight_Mesh_Shapekey_Head_B.jpg', 'DT_Weight_Mesh_Shapekey_Head_C.jpg', 'DT_Weight_Mesh_Shapekey_Head_D.jpg'),
        'titulo': {
            'EN': 'Edit Weight Transfer Model Head Shape',
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Edit the Head of the Head Weights Transfer Model to avoid overlapping geometry, specially in the mouth.",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': DT_Weight_Mesh_Shapekey_Head
    },
    #Select Character's Head
    {
        'imagen': ('DT_Select_Head_A.jpg', 'DT_Select_Head_B.jpg'),
        'titulo': {
            'EN': "Select Character's Head Object",
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Select the Head Object of the character and press the 'Define Selected as Head' Button",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': DT_Select_Head
    },
    #Edit Character's Head
    {
        'imagen': ('DT_Edit_Head_A.jpg', 'DT_Edit_Head_B.jpg', 'DT_Edit_Head_C.jpg', 'DT_Edit_Head_D.jpg'),
        'titulo': {
            'EN': "Edit Character's Head",
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Edit the Head of the character to get the mouth opened and match the shape of the Weight Transfer Model. You can also edit the Transfer Mesh further. Once you are done, press the Transfer Weights Button",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': DT_Edit_Head
    },
    #Test Character's Face
    {
        'imagen': ('DT_Test_Head_A.jpg', 'DT_Test_Head_B.jpg', 'DT_Test_Head_C.jpg'),
        'titulo': {
            'EN': "Test Character's Face",
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "With the Character's Head selected, press the 'Add Head Modifiers' Button. Then press the 'Test Deformation' Button. Keep in mind that this is just a first approximation, deformation should not be perfect. If you feel you need to refine the weights transfer, you can go back to the previous step.",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': DT_Test_Face
    },
    #Edit Weith Transfer Model Hands Shape
    {
        'imagen': ('DT_Weight_Mesh_Shapekey_Hands_A.jpg', 'DT_Weight_Mesh_Shapekey_Hands_B.jpg'),
        'titulo': {
            'EN': 'Edit Weith Transfer Model Hands Shape',
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Check the Fingers of the Weight Transfer Model to avoid overlapping geometry.",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': DT_Weight_Mesh_Shapekey_Hands
    },
    #Select Character's Hands
    {
        'imagen': ('DT_Select_Hands_A.jpg', 'DT_Select_Hands_B.jpg'),
        'titulo': {
            'EN': "Select Character's Hands Object",
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Select the Hands Object of the character and and press the 'Define Selected as Hands' Button.",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': DT_Select_Hands
    },
    #Edit Character's Hands
    {
        'imagen': ('DT_Edit_Hands_A.jpg', 'DT_Edit_Hands_B.jpg', 'DT_Edit_Hands_C.jpg'),
        'titulo': {
            'EN': "Edit Character's Hands",
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Edit the Hands to match the shape of the Hands Weight Transfer Model. You can also edit the Transfer Mesh further. Once you are done, press the Transfer Weights Button",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': DT_Edit_Hands
    },
    #Test Character's Hands
    {
        'imagen': ('DT_Test_Hands_A.jpg', 'DT_Test_Hands_B.jpg', 'DT_Test_Hands_C.jpg'),
        'titulo': {
            'EN': "Test Character's Hands",
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "With the Character's Hands selected, press the 'Add Hands Modifiers' Button. Then press the 'Test Deformation' Button. Keep in mind that this is just a first approximation, deformation should not be perfect. If you feel you need to refine the weights transfer, you can go back to the previous step.",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': DT_Test_Hands
    },
    #Eyes Setup
    {
        'imagen': ('DT_Eyes_A.jpg', 'DT_Eyes_B.jpg'),
        'titulo': {
            'EN': "Eyes Setup",
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Select the Left Eye and press the 'Add Left Eye Modifiers' Button. Same for the Right Eye. If both Eyes belong to a single object, go into Edit Mode, select the geometry of each Eye and press the corresponding button.",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': DT_Eyes
    },
    #Inner Mouth Setup
    {
        'imagen': ('DT_Inner_Mouth_A.jpg', 'DT_Inner_Mouth_B.jpg'),
        'titulo': {
            'EN': "Inner Mouth Setup",
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Select all the loose objects that conform the inner mouth. Press the 'Add Inner Mouth Modifiers' Button.",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': DT_Inner_Mouth
    },
    #Clean Symmetry
    {
        'imagen': 'DT_Clean_Symmetry.jpg',
        'titulo': {
            'EN': "Clean Vgroups Symmetry",
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Select the head of the character and press the 'Mirror all Vertex Groups' button to clean the Symmetry of the Vgroups. Do the same with the Hands object. This operation might take a bit.",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': DT_Clean_Symmetry
    },
    #Weights Transfer Finish
    {
        'imagen': 'DT_Finish.jpg',
        'titulo': {
            'EN': "Weights Transfer Finish",
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Great! You can move on to the Mesh Deform Guide",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': DT_Finish
    },
)


