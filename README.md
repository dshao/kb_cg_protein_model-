# kb_cg_protein_model-
Creates a Karanicolas and Brooks coarse-grained protein model from a protein data bank file and a control file

citation for kb_cg model: (1) O’Brien, E. P.; Ziv, G.; Haran, G.; Brooks, B. R.; Thirumalai, D. Effects of Denaturants and Osmolytes on Proteins Are Accurately Predicted by the Molecular Transfer Model. Proc. Natl. Acad. Sci. U. S. A. 2008. https://doi.org/10.1073/pnas.0802113105.

Monomer coarse-graining with the kb potential
---------------------------------------------
#### Preprocessing
1. The pdb use HSE instead of HIS for histidine residues
2. The pdb cannot be missing residues. If it is use:

`[path-to-charmm-exe] < rebuild_solv_ions_definitive_v1.2.inp pdbin=[path-to-pbd-file-to-rebuild] label=[label-for-output-files]`

3. The pdb must also have the following form:
``````
ATOM      1  N   MET A   1       1.325   0.000   0.000  1.00  0.00
ATOM      2  HT1 MET A   1       1.746   0.686   0.658  1.00  0.00
ATOM      3  HT2 MET A   1       1.356  -0.949   0.423  1.00  0.00
ATOM      4  HT3 MET A   1       0.337   0.263  -0.189  1.00  0.00
ATOM      5  CA  MET A   1       2.073   0.000  -1.245  1.00  0.00
ATOM      6  HA  MET A   1       1.985   1.012  -1.640  1.00  0.00
ATOM      7  CB  MET A   1       3.533  -0.363  -0.964  1.00  0.00
ATOM      8  HB1 MET A   1       3.676  -0.302   0.140  1.00  0.00
ATOM      9  HB2 MET A   1       3.719  -0.331   0.109  1.00  0.00
ATOM     10  CG  MET A   1       4.484   0.597  -1.681  1.00  0.00
ATOM     11  HG1 MET A   1       4.877   0.130  -2.608  1.00  0.00
ATOM     12  HG2 MET A   1       4.857   0.137  -2.596  1.00  0.00
ATOM     13  SD  MET A   1       5.850   1.016  -0.611  1.00  0.00
ATOM     14  CE  MET A   1       5.083   2.280   0.389  1.00  0.00
ATOM     15  HE1 MET A   1       5.586   2.335   1.354  1.00  0.00
ATOM     16  HE2 MET A   1       5.163   3.242  -0.118  1.00  0.00
ATOM     17  HE3 MET A   1       4.032   2.036   0.541  1.00  0.00
ATOM     18  C   MET A   1       1.481  -1.000  -2.241  1.00  0.00
ATOM     19  O   MET A   1       2.212  -1.766  -2.866  1.00  0.00
`````
If it does not you can use the following for conversion:

`convert_pdb_for_multimer_cg_v1.1.py [path-to-input-pdb] [path-to-output-pdb] [segid]`

NOTE: this conversion script is not perfect as there are many different forms a PDB can take depending on when and by what it was created. The script is simple enough that any beginner pythoner can modify it.

#### To create a kb_cg_model for a monomer 
use: 

`perl create_cg_protein_model_v37.1.pl [path-to-control-file]`

see monomer_test/nbd1/input/nbd1_n1.1725_go.cntrl for an example control file and output

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

#### Example cntrl file contents for a monomer:

`charmm = [path-to-charmm-exe]
pdb = [path-to-prepared-pdb]
nscal = 1.8
pot = bt
bondlength_go = 0
dihedral_go = 0 
casm = 0
charges = 1 
angle_dw = 1
fnn = 1
ca_name = A 
sc_name = none`

NOTE: this CG procedure requires the hacked version of charmm specific to our group.

Main outputs:
[pdb-file-name]_ca.cor
[pdb-file-name]_ca.psf
[pdb-file-name]_ca.top
[pdb-file-name]_[nscal]_[fnn]_go_[pot].prm
[pdb-file-name]_ca.seq
[pdb-file-name]_ca_mini.cor

NOTE: other other files are created during the CG procedure that are not necessary for running Molecular Dynamics

#### To convert your resulting .top and .prm into a single .xml file for OpenMM simulations use:

`python ../../../parse_cg_prm.py -p [path-to-parameter-file] -t [path-to-topology-file]`

Multimer coarse-graining with the kb potential is still under construction
--------------------------------------------------------------------------

#### Preprocessing
1. Each monomer of the n monomer multimer should have its own pdb
2. The pdb use HSE instead of HIS for histidine residues
3. The pdb cannot be missing residues. If it is use:

`[path-to-charmm-exe] < rebuild_solv_ions_definitive_v1.2.inp pdbin=[path-to-pbd-file-to-rebuild] label=[label-for-output-files]`

4. The pdb must also have the following form:
``````
ATOM      1  N   MET A   1       1.325   0.000   0.000  1.00  0.00
ATOM      2  HT1 MET A   1       1.746   0.686   0.658  1.00  0.00
ATOM      3  HT2 MET A   1       1.356  -0.949   0.423  1.00  0.00
ATOM      4  HT3 MET A   1       0.337   0.263  -0.189  1.00  0.00
ATOM      5  CA  MET A   1       2.073   0.000  -1.245  1.00  0.00
ATOM      6  HA  MET A   1       1.985   1.012  -1.640  1.00  0.00
ATOM      7  CB  MET A   1       3.533  -0.363  -0.964  1.00  0.00
ATOM      8  HB1 MET A   1       3.676  -0.302   0.140  1.00  0.00
ATOM      9  HB2 MET A   1       3.719  -0.331   0.109  1.00  0.00
ATOM     10  CG  MET A   1       4.484   0.597  -1.681  1.00  0.00
ATOM     11  HG1 MET A   1       4.877   0.130  -2.608  1.00  0.00
ATOM     12  HG2 MET A   1       4.857   0.137  -2.596  1.00  0.00
ATOM     13  SD  MET A   1       5.850   1.016  -0.611  1.00  0.00
ATOM     14  CE  MET A   1       5.083   2.280   0.389  1.00  0.00
ATOM     15  HE1 MET A   1       5.586   2.335   1.354  1.00  0.00
ATOM     16  HE2 MET A   1       5.163   3.242  -0.118  1.00  0.00
ATOM     17  HE3 MET A   1       4.032   2.036   0.541  1.00  0.00
ATOM     18  C   MET A   1       1.481  -1.000  -2.241  1.00  0.00
ATOM     19  O   MET A   1       2.212  -1.766  -2.866  1.00  0.00
``````
If it does not you can use the following for conversion:

`convert_pdb_for_multimer_cg_v1.1.py [path-to-input-pdb] [path-to-output-pdb] [segid]`

NOTE: this conversion script is not perfect as there are many different forms a PDB can take depending on when and by what it was created. The script is simple enough that any beginner pythoner can modify it.

#### To create a kb_cg_model for a monomer 
use: 

`perl create_cg_protein_model_v37.1.pl [path-to-control-file]`

see multimer_test/go_model.cntrl for an example control file and output

| cntrl file param | description                                                                                                    |
|------------------|----------------------------------------------------------------------------------------------------------------|
| charmm           | path to charmm executable hacked or modified with correct deby huckel electrostatics and double well angle pot |
| pdb              | space separatetd paths to input pdbs 1 to n                                                                    |
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

#### Example cntrl file contents for a multimer:

`charmm = [path-to-charmm-exe]
pdb = [path-to-prepared-pdb1] [path-to-prepared-pdb2] ... [path-to-prepared-pdbn]
nscal = 1.8
pot = bt bt bt bt bt bt bt
bondlength_go = 0 0 0 0 0 0 0
dihedral_go = 0 0 0 0 0 0 0
casm = 0
charges = 1 1 1 1 1 1 1
angle_dw = 1 1 1 1 1 1 1
fnn = 1
ca_name = A B C D E F G
sc_name = none none none none none none none`

NOTE: this CG procedure requires the hacked version of charmm specific to our group.

Main outputs for each of the n input pdbs:
[pdb-file-name]_ca.cor
[pdb-file-name]_ca.psf
[pdb-file-name]_ca.top
[pdb-file-name]_[nscal]_[fnn]_go_[pot].prm
[pdb-file-name]_ca.seq
[pdb-file-name]_ca_mini.cor

NOTE: other other files are created during the CG procedure that are not necessary for running Molecular Dynamics

#### To convert your resulting .top and .prm into a single .xml file for OpenMM simulations use:

`python ../../../parse_cg_prm.py -p [path-to-parameter-file] -t [path-to-topology-file]`


