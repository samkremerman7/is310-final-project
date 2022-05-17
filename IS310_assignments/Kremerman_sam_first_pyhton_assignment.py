tools = {
    "Python": {
        "2015": 9,
        "2016": 22,
        "2017": 27,
        "2018": 32,
        "2019": 35,
    },
    "JavaScript": {
        "2015": 8,
        "2016": 18,
        "2017": 12,
        "2018": 6,
        "2019": 15,
    },
    "Twitter": {
        "2015": 10,
        "2016": 18,
        "2017": 26,
        "2018": 16,
        "2019": 12,
    },
    "GitHub": {
        "2015": 2,
        "2016": 6,
        "2017": 17,
        "2018": 5,
        "2019": 10,
    },
    "Gephi": {
        "2015": 11,
        "2016": 16,
        "2017": 14,
        "2018": 10,
        "2019": 9,
    },
    "GeoNames": {
        "2015": 2,
        "2016": 4,
        "2017": 3,
        "2018": 1,
        "2019": 8,
    },
    "Transkribus": {
        "2015": 0,
        "2016": 1,
        "2017": 2,
        "2018": 1,
        "2019": 8,
    },
    "Excel": {
        "2015": 5,
        "2016": 9,
        "2017": 3,
        "2018": 6,
        "2019": 7,
    },
    "MySQL": {
        "2015": 0,
        "2016": 6,
        "2017": 9,
        "2018": 5,
        "2019": 7,
    },
}
tools["Python"]["Overall"] = tools["Python"]["2015"] + tools["Python"]["2016"] + tools["Python"]["2017"] + tools["Python"]["2018"] + tools["Python"]["2019"]
tools["JavaScript"]["Overall"] = tools["JavaScript"]["2015"] + tools["JavaScript"]["2016"] + tools["JavaScript"]["2017"] + tools["JavaScript"]["2018"] + tools["JavaScript"]["2019"]
tools["Twitter"]["Overall"] = tools["Twitter"]["2015"] + tools["Twitter"]["2016"] + tools["Twitter"]["2017"] + tools["Twitter"]["2018"] + tools["Twitter"]["2019"]
tools["GitHub"]["Overall"] = tools["GitHub"]["2015"] + tools["GitHub"]["2016"] + tools["GitHub"]["2017"] + tools["GitHub"]["2018"] + tools["GitHub"]["2019"]
tools["Gephi"]["Overall"] = tools["Gephi"]["2015"] + tools["Gephi"]["2016"] + tools["Gephi"]["2017"] + tools["Gephi"]["2018"] + tools["Gephi"]["2019"]
tools["GeoNames"]["Overall"] = tools["GeoNames"]["2015"] + tools["GeoNames"]["2016"] + tools["GeoNames"]["2017"] + tools["GeoNames"]["2018"] + tools["GeoNames"]["2019"]
tools["Transkribus"]["Overall"] = tools["Transkribus"]["2015"] + tools["Transkribus"]["2016"] + tools["Transkribus"]["2017"] + tools["Transkribus"]["2018"] + tools["Transkribus"]["2019"]
tools["Excel"]["Overall"] = tools["Excel"]["2015"] + tools["Excel"]["2016"] + tools["Excel"]["2017"] + tools["Excel"]["2018"] + tools["Excel"]["2019"]
tools["MySQL"]["Overall"] = tools["MySQL"]["2015"] + tools["MySQL"]["2016"] + tools["MySQL"]["2017"] + tools["MySQL"]["2018"] + tools["MySQL"]["2019"]
print("Python's 2015 popularity: " + str(tools["Python"]["2015"]))
print("Python's 2019 popularity: " + str(tools["Python"]["2019"]))
print("Python's Overall popularity: " + str(tools["Python"]["Overall"]))
print("JavaScript's 2015 popularity: " + str(tools["JavaScript"]["2015"]))
print("JavaScript's 2019 popularity: " + str(tools["JavaScript"]["2019"]))
print("JavaScript's Overall popularity: " + str(tools["JavaScript"]["Overall"]))
print("Twitter's 2015 popularity: " + str(tools["Twitter"]["2015"]))
print("Twitter's 2019 popularity: " + str(tools["Twitter"]["2019"]))
print("Twitter's Overall popularity: " + str(tools["Twitter"]["Overall"]))
print("GitHub's 2015 popularity: " + str(tools["GitHub"]["2015"]))
print("GitHub's 2019 popularity: " + str(tools["GitHub"]["2019"]))
print("GitHub's Overall popularity: " + str(tools["GitHub"]["Overall"]))
print("Gephi's 2015 popularity: " + str(tools["Gephi"]["2015"]))
print("Gephi's 2019 popularity: " + str(tools["Gephi"]["2019"]))
print("Gephi's Overall popularity: " + str(tools["Gephi"]["Overall"]))
print("GeoNames's 2015 popularity: " + str(tools["GeoNames"]["2015"]))
print("GeoNames's 2019 popularity: " + str(tools["GeoNames"]["2019"]))
print("GeoNames's Overall popularity: " + str(tools["GeoNames"]["Overall"]))
print("Transkribus's 2015 popularity: " + str(tools["Transkribus"]["2015"]))
print("Transkribus's 2019 popularity: " + str(tools["Transkribus"]["2019"]))
print("Transkribus's Overall popularity: " + str(tools["Transkribus"]["Overall"]))
print("Excel's 2015 popularity: " + str(tools["Excel"]["2015"]))
print("Excel's 2019 popularity: " + str(tools["Excel"]["2019"]))
print("Excel's Overall popularity: " + str(tools["Excel"]["Overall"]))
print("MySQL's 2015 popularity: " + str(tools["MySQL"]["2015"]))
print("MySQL's 2019 popularity: " + str(tools["MySQL"]["2019"]))
print("MySQL's Overall popularity: " + str(tools["MySQL"]["Overall"]))