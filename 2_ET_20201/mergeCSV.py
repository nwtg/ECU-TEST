import os
import pandas

def func(reportFolder, csvName):

    folders = os.listdir(reportFolder)
    i = 0
    for folder in folders:
        csvFile = os.path.join(reportFolder, folder, csvName)
        if os.path.exists(csvFile):
            if i == 0:
                df = pandas.read_csv(csvFile)
                df.index = [folder] * len(df)
                df.to_csv(reportFolder+'\\test.csv', index=True)
            else:
                df = pandas.read_csv(csvFile)
                df.index = [folder] * len(df)
                df.to_csv(reportFolder+'\\test.csv', index=True, header=False, mode='a+')
            i += 1
