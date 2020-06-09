%% startup script template to be used by ECU-TEST
% ==== HELP TEXT START ==== help block can be removed
% (1) general init code comes first, see below
%
% (2) model-specific PRE-open_system code can be inserted by callback function 
% that can optionally be handed to ecuTest.api.EcuTestController.getMatlabStartupScript
% or use a template file with the name: preLoadModelStartupFile.m
%
% (3)open_system-command will be inserted after general init and PRE-open callback
%
% (4) model-specific POST-open_system code can be inserted by callback function 
% that can optionally be handed to ecuTest.api.EcuTestController.getMatlabStartupScript
% or use a template file with the name: postLoadModelStartupFile.m
%
% ==== HELP TEXT END ====

%% (1) ==== general init code may go here, e.g.: ====
% run('initfile.m');
% load('initvalues.mat');
ecuTestExampleDummyVariable0 = 0;


%% (2) ==== PRE-LOAD Commands ====
% Used callback function: preLoadModelStartupFile
% Pre-load commands for \\mac\home\Desktop\OneDrive\3_ET_Workspaces\9_2020test_ET2020_1\Models\multiply.slx
% Insterted by using the function: \\mac\home\Desktop\OneDrive\3_ET_Workspaces\9_2020test_ET2020_1\Templates\MatlabUserTemplates\userGeneratorFunctions\preLoadModelStartupFile
ecuTestExampleDummyVariable1 = 1;

%% (3) ==== LOAD SYSTEM ====
relPath = '\\mac\home\Desktop\OneDrive\3_ET_Workspaces\9_2020test_ET2020_1\Models'; % try to get relative path 
if exist(relPath, 'dir')
    addpath(relPath); % add model path 
else
    addpath('\\mac\home\Desktop\OneDrive\3_ET_Workspaces\9_2020test_ET2020_1\Models'); % alternatively, use absolute model path 
end
open_system('multiply.slx'); % open system to test 

%% (4) ==== POST-LOAD Commands ====
% Used callback function: postLoadModelStartupFile
% Post-load commands for \\mac\home\Desktop\OneDrive\3_ET_Workspaces\9_2020test_ET2020_1\Models\multiply.slx
% Insterted by using the function: \\mac\home\Desktop\OneDrive\3_ET_Workspaces\9_2020test_ET2020_1\Templates\MatlabUserTemplates\userGeneratorFunctions\postLoadModelStartupFile
ecuTestExampleDummyVariable2 = 2;
