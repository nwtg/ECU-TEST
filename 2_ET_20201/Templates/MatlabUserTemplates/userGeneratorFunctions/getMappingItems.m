function [inputs, outputs, parameters, signals] = getMappingItems(modelName)
%getMappingItems  Returns all inport, outport and parameter mapping items 
%   [inputs, outputs, parameters, signals] = getMappingItems(modelName)
%   can be used to return individual list of mappings to be used for 
%   generate global mapping file
%
% Return format:
%   * Each return parameter will be a m-by-4 cell array. m is the number of
%     mappings which have been found. 
%   * column 1: targetPath – Name of measurement variable to be accessed
%   * column 2: dataType - data type of the variable (e.g. uint8, int16, double)
%   * column 3: referenceName – (if available) Name of the mapping item
%   * column 4: variableType – Type of variable to be mapped (VALUE, VECTOR, MATRIX)
%   * column 5: isSignal (logical) - Selects if the mapping item should point to a model signal instead of variable

% by default, use the built-in function that returns all top-level
% subsystem inputs and outputs and all workspace parameters and signals

[inputs, outputs, parameters, signals] = ecuTest.tools.GetMappingItems(modelName);
