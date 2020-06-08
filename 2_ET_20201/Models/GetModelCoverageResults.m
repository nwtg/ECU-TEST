function covDataStruct = GetModelCoverageResults(covDataWorkspaceVariable, modelName, subsysPath)
modelPath = strcat(modelName, '/',subsysPath);

if ~exist('modelPath', 'var')
    modelPath = bdroot;
elseif strcmp(modelPath, '/')
    modelPath = bdroot;
end

%% Get coverage results from workspace
coverage = conditioninfo(covDataWorkspaceVariable, modelPath);
if isempty(coverage)
    c1_result = 0;
    c1_objectives = 0;
else
    c1_result = round(100 * coverage(1) / coverage(2));
    c1_objectives = coverage(2);
end

coverage = decisioninfo(covDataWorkspaceVariable, modelPath);
if isempty(coverage)
    d1_result = 0;
    d1_objectives = 0;
else
    d1_result = round(100 * coverage(1) / coverage(2));
    d1_objectives = coverage(2);
end

coverage = mcdcinfo(covDataWorkspaceVariable, modelPath);
if isempty(coverage)
    mcdc_result = 0;
    mcdc_objectives = 0;
else
    mcdc_result = round(100 * coverage(1) / coverage(2));
    mcdc_objectives = coverage(2);
end

complexity = complexityinfo(covDataWorkspaceVariable, modelPath);
complexity = complexity(1);

covDataStruct.complexity = complexity;
covDataStruct.mcdc = mcdc_result;
covDataStruct.mcdc_objectives = mcdc_objectives;
covDataStruct.d1 = d1_result;
covDataStruct.d1_objectives = d1_objectives;
covDataStruct.c1 = c1_result;
covDataStruct.c1_objectives = c1_objectives;
end