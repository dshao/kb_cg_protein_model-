# kb_cg_protein_model-
Creates a Karanicolas and Brooks coarse-grained protein model from a protein data bank file and a control file

citation for kb_cg model: (1) O’Brien, E. P.; Ziv, G.; Haran, G.; Brooks, B. R.; Thirumalai, D. Effects of Denaturants and Osmolytes on Proteins Are Accurately Predicted by the Molecular Transfer Model. Proc. Natl. Acad. Sci. U. S. A. 2008. https://doi.org/10.1073/pnas.0802113105.

Monomer coarse-graining with the kb potential
---------------------------------------------
To create a kb_cg_model for a monomer use: 

`perl create_cg_protein_model_v36.2.pl [path-to-control-file]`

see nbd1_monomer_test for an example control file and output

| cntrl file param | description                                                                                                    |
|------------------|----------------------------------------------------------------------------------------------------------------|
| charmm           | path to charmm executable hacked or modified with correct deby huckel electrostatics and double well angle pot |
| pdb              | path to input pdb                                                                                              |
| nscal            | scaling factor for the sidechain sidechain nonbonded interaction                                               |
| pot              | type of generic potential to use: bt, mj, kgs                                                                  |
| bondlength_go    | use a go model bondlength 0:no 1:yes                                                                           |
| dihedral_go      | use a go model dihedral potential 0:no 1:yes                                                                   |
| casm             | alpha-carbon side-chain model 0:no 1:yes                                                                       |
| charges          | include electrostatics  0:no 1:yes                                                                             |
| angle_dw         | include double well angle pot 0:no 1:yes                                                                       |
| fnn              | a multiplicative value which modifies the radius of the hard spheres used in the coarse-grain model            |
| ca_name          | name of model segments for alpha-carbon only CG model                                                          |
| sc_name          | name of side-chains for alpha-carbon side-chain CG model                                                       |

NOTE: this CG procedure requires the hacked version of charmm specific to our group.

Main outputs:
[pdb-file-name]_ca.cor
[pdb-file-name]_ca.psf
[pdb-file-name]_ca.top
[pdb-file-name]_[nscal]_[fnn]_go_[pot].prm
[pdb-file-name]_ca.seq
[pdb-file-name]_ca_mini.cor

NOTE: other other files are created during the CG procedure that are not necessary for running Molecular Dynamics

### To convert your resulting .top and .prm into a single .xml file for OpenMM simulations use:

`python ../../../parse_cg_prm.py -p [path-to-parameter-file] -t [path-to-topology-file]`

Multimer coarse-graining with the kb potential is still under construction
--------------------------------------------------------------------------
To create a kb_cg_model for a multimer use create_cg_protein_model_v34_modified_V2.3.2.pl [path-to-control-file]
see multimer_test for an example control file and output

