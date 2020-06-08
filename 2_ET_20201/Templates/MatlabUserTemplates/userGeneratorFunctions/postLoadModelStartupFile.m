function postLoadModelStartupFile(fid, modelName)
% Function that will be called to insert matlab commands into the 
% startup file used by ECU-TEST during configuration start.
% This function may be modified to generate code that will be executed
% AFTER the model is opened.
fprintf(fid, '%% Post-load commands for %s\n', modelName);
fprintf(fid, '%% Insterted by using the function: %s\n', mfilename('fullpath'));
fprintf(fid, 'ecuTestExampleDummyVariable2 = %d;\n', 2);
end