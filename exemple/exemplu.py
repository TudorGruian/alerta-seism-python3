import alertaseism


while True:
    print(alertaseism.mag())
    if alertaseism.mag() >= 1:
        print("UN CUTREMUR SE INTAMPLA. NU VA PANICATI")
    print("Status:" + alertaseism.heart())
    
