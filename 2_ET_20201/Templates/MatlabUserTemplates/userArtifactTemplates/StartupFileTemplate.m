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

