# -*- coding: utf-8 -*-
# #START_LICENSE###########################################################
#
#
# This file is part of the Environment for Tree Exploration program
# (ETE).  http://ete.cgenomics.org
#  
# ETE is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#  
# ETE is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public
# License for more details.
#  
# You should have received a copy of the GNU General Public License
# along with ETE.  If not, see <http://www.gnu.org/licenses/>.
#
# 
#                     ABOUT THE ETE PACKAGE
#                     =====================
# 
# ETE is distributed under the GPL copyleft license (2008-2011).  
#
# If you make use of ETE in published work, please cite:
#
# Jaime Huerta-Cepas, Joaquin Dopazo and Toni Gabaldon.
# ETE: a python Environment for Tree Exploration. Jaime BMC
# Bioinformatics 2010,:24doi:10.1186/1471-2105-11-24
#
# Note that extra references to the specific methods implemented in 
# the toolkit are available in the documentation. 
# 
# More info at http://ete.cgenomics.org
#
# 
# #END_LICENSE#############################################################
__VERSION__="ete2-2.2.1072" 
from ete2 import PhyloTree, PhyloNode, ClusterTree, ClusterNode, EvolTree, EvolNode
import layouts 

def apply_template(tree_style, template):
    for k, v in template.iteritems(): 
        setattr(tree_style, k, v)

phylogeny = {
    "layout_fn": layouts.phylogeny, 
     "show_leaf_name":False, 
     "draw_guiding_lines":False
    }

evol = {
    "layout_fn": layouts.evol_layout, 
     "show_leaf_name":True, 
     "draw_guiding_lines":False
    }

clustering = {
    "layout_fn": layouts.large, 
    "show_leaf_name":False
    }

_DEFAULT_STYLE={
    PhyloTree: phylogeny,
    PhyloNode: phylogeny,
    EvolTree: evol,
    EvolNode: evol,
    ClusterTree: clustering,
    ClusterNode: clustering, 
    }
