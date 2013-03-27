import pickle
from Exceptions import *
# TODO, abstract model, editmodelname, testcode, abstract open+close methods
#DBFILENAME = ".pickleDB.dat"


class PickleMonger(object):

    #The constructor creates a database file and an object map
    def __init__(self, DBFILENAME, objectMap={}):
        self.DBFILENAME = DBFILENAME
        dbFile = open(self.DBFILENAME, 'a+b')
        self.objectMap = objectMap
        pickle.dump(self.objectMap, dbFile)
        dbFile.close()

    #This method is used for adding new models to the database
    def create(self, modelname):
        dbFile = open(self.DBFILENAME, 'r+b')
        currentObjectMap = pickle.load(dbFile)
        if modelname in currentObjectMap.keys():
            return
        self.objectMap[modelname] = []
        dbFile = open(self.DBFILENAME, 'w+b')
        pickle.dump(self.objectMap, dbFile)
        dbFile.close()

    #This method returns the objects stored in a model
    def read_allInstances(self, modelName):
        dbFile = open(self.DBFILENAME, 'r+b')
        self.objectMap = pickle.load(dbFile)
        dbFile.close()
        return self.objectMap[modelName]

    def read_oneInstances(self, modelName, instanceName):
        dbFile = open(self.DBFILENAME, 'r+b')
        self.objectMap = pickle.load(dbFile)
        for instance in self.objectMap:
            if instance.instanceName == instanceName:
                return instance
        dbFile.close()
        raise NoInstanceException

    #This method is used to add objects to a model
    def addObject(self, model):
        modelName = model.modelName
        dbFile = open(self.DBFILENAME, 'r+b')
        self.objectMap = pickle.load(dbFile)

        for instances in self.objectMap[model.modelName]:
            if instances.instanceName == model.instanceName:
                raise MultipleInstanceException()
        self.objectMap[modelName].append(model)
        dbFile = open(self.DBFILENAME, 'w+b')
        pickle.dump(self.objectMap, dbFile)
        dbFile.close()

    def updateObject(self, model):
        modelName = model.modelName
        dbFile = open(self.DBFILENAME, 'r+b')
        self.objectMap = pickle.load(dbFile)

        self.objectMap[modelName] = model
        dbFile = open(self.DBFILENAME, 'w+b')
        pickle.dump(self.objectMap, dbFile)
        dbFile.close()

    #This method destroys a model
    def destroyModel(self, modelName):
        dbFile = open(self.DBFILENAME, 'r+b')
        self.objectMap = pickle.load(dbFile)
        for k, v in self.objectMap:
            if k == modelName:
                self.objectMap.pop(modelName)
        dbFile.close()
        raise NoInstanceException

    #This method destroys an object in a model
    def destroyObjectInstance(self, modelName, instanceName):
        dbFile = open(self.DBFILENAME, 'r+b')
        self.objectMap = pickle.load(dbFile)
        for modelObject in self.objectMap[modelName]:
            if modelObject.instanceName == instanceName:
                self.objectMap[modelName].remove(modelObject)
        dbFile.close()

    def editInstance(self, modelName, instanceName, newInstance):
        dbFile = open(self.DBFILENAME, 'r+b')
        self.objectMap = pickle.load(dbFile)
        for instance in self.objectMap[modelName]:
            if instance.instanceName == instanceName:
                self.objectMap[modelName][self.objectMap[modelName].index(instance)] = newInstance

        dbFile = open(self.DBFILENAME, 'w+b')
        pickle.dump(self.objectMap, dbFile)
        dbFile.close()



    def editModelName(self, modelName, newModelName):
        dbFile = open(self.DBFILENAME, 'r+b')
        self.objectMap = pickle.load(dbFile)
        self.objectMap[newModelName] = self.objectMap[modelName]
        del self.objectMap[modelName]
        dbFile = open(self.DBFILENAME, 'w+b')
        pickle.dump(self.objectMap, dbFile)
        dbFile.close()





###BASIC TEST CLASS AND MAIN FOR PICKLEMONGER###
#class Model():
    #def __init__(self,username,instanceName,pw):
        #self.modelName=username
        #self.instanceName=instanceName
        #self.pw=pw



#if __name__=="__main__":
    #PM = PickleMonger('PICKLE3.db')
    #t = Model('nathan','n1','12345')
    #t2 = Model('nathan','n2','2343')
    #t3 = Model('nathan','n3','ppp')
    #PM.create('nathan')
    #PM.addObject(t)
    #PM.addObject(t2)
    #PM.destroyObjectInstance('nathan','n1')

