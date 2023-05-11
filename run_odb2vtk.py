from odb2vtk import *
#ConvertOdb2Vtk('odb2vtk.txt')

path = 'E:\\Simulations\\DIDEAROT\\Micro_RVE_Elastic_Compare_BSC\\Generic_PBC_Long_Tension\\NLGEOM_YES'

ConvertOdb2VtkP( Odbpath = path, Odbname = 'Test-RVE-Generic_PBC', vtkpath = path, Piecenum = 1, BeginFrame = 0, EndFrame = 1, Steps = '0', Instances = '13')