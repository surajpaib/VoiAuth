from scripts import ModuleML

model = ModuleML()
model.train_model('authentication/samples/gayathritrain1.wav')

model.GBM_run()

model.predict('authentication/samples/kanthitest1.wav', 1)
model.predict('authentication/samples/kanthitest1.wav', 2)
model.predict('authentication/samples/kanthitest1.wav', 3)
