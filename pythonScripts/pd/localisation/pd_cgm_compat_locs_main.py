#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys,glob,io
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(1, '..\..')
from locList import LocList
locList=LocList(2)
for fileName in glob.glob('locs/*.py'):
	with io.open(fileName,'r', encoding='utf-8') as file:
		 exec(file.read())
locList.addEntry("locale_key","@locale_key")
locList.addEntry("pc_large_asteroid_moon","@pc_large_asteroid_moon")
locList.addEntry("pc_large_asteroid_moon_desc","@pc_large_asteroid_moon_desc")
locList.addEntry("pc_small_asteroid_moon","@pc_small_asteroid_moon")
locList.addEntry("pc_small_asteroid_moon_desc","@pc_small_asteroid_moon_desc")
locList.addEntry("pc_retinal","@pc_retinal")
locList.addEntry("pc_retinal_desc","@pc_retinal_desc")
locList.addEntry("pc_retinal_habitability","@pc_retinal_habitability")
locList.addEntry("pc_retinal_tile","@pc_retinal_tile")
locList.addEntry("pc_retinal_tile_desc","@pc_retinal_tile_desc")
locList.addEntry("trait_pc_retinal_preference","@trait_pc_retinal_preference")
locList.addEntry("trait_pc_retinal_preference_desc","$trait_pc_arctic_preference_desc$")
locList.addEntry("pc_greenhouse_hot","@pc_greenhouse_hot")
locList.addEntry("pc_greenhouse_hot_desc","@pc_greenhouse_hot_desc")
locList.addEntry("pc_greenhouse_cold","@pc_greenhouse_cold")
locList.addEntry("pc_greenhouse_cold_desc","@pc_greenhouse_cold_desc")
locList.addEntry("pc_irradiated_terrestrial","@pc_irradiated_terrestrial")
locList.addEntry("pc_irradiated_terrestrial_desc","@pc_irradiated_terrestrial_desc")
locList.addEntry("pc_irradiated_terrestrial_habitability","@pc_irradiated_terrestrial_habitability")
locList.addEntry("pc_irradiated_terrestrial_tile","@pc_irradiated_terrestrial_tile")
locList.addEntry("pc_irradiated_terrestrial_tile_desc","@pc_irradiated_terrestrial_tile_desc")
locList.addEntry("trait_pc_irradiated_terrestrial_preference","@trait_pc_irradiated_terrestrial_preference")
locList.addEntry("trait_pc_irradiated_terrestrial_preference_desc","$trait_pc_arctic_preference_desc$")
locList.addEntry("pc_lush","@pc_lush")
locList.addEntry("pc_lush_desc","@pc_lush_desc")
locList.addEntry("pc_lush_habitability","@pc_lush_habitability")
locList.addEntry("pc_lush_tile","@pc_lush_tile")
locList.addEntry("pc_lush_tile_desc","@pc_lush_tile_desc")
locList.addEntry("trait_pc_lush_preference","@trait_pc_lush_preference")
locList.addEntry("trait_pc_lush_preference_desc","$trait_pc_arctic_preference_desc$")
locList.addEntry("pc_geoplastic","@pc_geoplastic")
locList.addEntry("pc_geoplastic_desc","@pc_geoplastic_desc")
locList.addEntry("pc_geometallic","@pc_geometallic")
locList.addEntry("pc_geometallic_desc","@pc_geometallic_desc")
locList.addEntry("pc_geocrystalline","@pc_geocrystalline")
locList.addEntry("pc_geocrystalline_desc","@pc_geocrystalline_desc")
locList.addEntry("pc_geocrystalline_habitability","@pc_geocrystalline_habitability")
locList.addEntry("pc_geocrystalline_tile","@pc_geocrystalline_tile")
locList.addEntry("pc_geocrystalline_tile_desc","@pc_geocrystalline_tile_desc")
locList.addEntry("trait_pc_geocrystalline_preference","@trait_pc_geocrystalline_preference")
locList.addEntry("trait_pc_geocrystalline_preference_desc","$trait_pc_arctic_preference_desc$")
locList.addEntry("pc_geomorteus","@pc_geomorteus")
locList.addEntry("pc_geomorteus_desc","@pc_geomorteus_desc")
locList.addEntry("pc_dwarf_planet_asteroid","@pc_dwarf_planet_asteroid")
locList.addEntry("pc_dwarf_planet_asteroid_desc","@pc_dwarf_planet_asteroid_desc")
locList.addEntry("pc_gas_giant_hot","@pc_gas_giant_hot")
locList.addEntry("pc_gas_giant_hot_desc","@pc_gas_giant_hot_desc")
locList.addEntry("pc_ice_giant","@pc_ice_giant")
locList.addEntry("pc_ice_giant_desc","@pc_ice_giant_desc")
locList.addEntry("pc_marginal","@pc_marginal")
locList.addEntry("pc_marginal_desc","@pc_marginal_desc")
locList.addEntry("pc_marginal_habitability","@pc_marginal_habitability")
locList.addEntry("pc_marginal_tile","@pc_marginal_tile")
locList.addEntry("pc_marginal_tile_desc","@pc_marginal_tile_desc")
locList.addEntry("trait_pc_marginal_preference","@trait_pc_marginal_preference")
locList.addEntry("trait_pc_marginal_preference_desc","$trait_pc_arctic_preference_desc$")
locList.addEntry("pc_irradiated_marginal","@pc_irradiated_marginal")
locList.addEntry("pc_irradiated_marginal_desc","@pc_irradiated_marginal_desc")
locList.addEntry("pc_irradiated_marginal_habitability","@pc_irradiated_marginal_habitability")
locList.addEntry("pc_irradiated_marginal_tile","@pc_irradiated_marginal_tile")
locList.addEntry("pc_irradiated_marginal_tile_desc","@pc_irradiated_marginal_tile_desc")
locList.addEntry("trait_pc_irradiated_marginal_preference","@trait_pc_irradiated_marginal_preference")
locList.addEntry("trait_pc_irradiated_marginal_preference_desc","$trait_pc_arctic_preference_desc$")
locList.addEntry("pc_marginal_cold","@pc_marginal_cold")
locList.addEntry("pc_marginal_cold_desc","@pc_marginal_cold_desc")
locList.addEntry("pc_marginal_cold_habitability","@pc_marginal_cold_habitability")
locList.addEntry("pc_marginal_cold_tile","@pc_marginal_cold_tile")
locList.addEntry("pc_marginal_cold_tile_desc","@pc_marginal_cold_tile_desc")
locList.addEntry("trait_pc_marginal_cold_preference","@trait_pc_marginal_cold_preference")
locList.addEntry("trait_pc_marginal_cold_preference_desc","$trait_pc_arctic_preference_desc$")
for language in locList.languages:
	outFolderLoc=language
	if not os.path.exists(outFolderLoc):
		os.makedirs(outFolderLoc)
	locList.write(outFolderLoc+"/pd_cgm_compat_locs_l_"+language+".yml",language)