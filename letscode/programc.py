class MPNeuron:
    def __init__(self):
        self.n = 3
        self.inputs=[1,1,1]
        self.weights=[1,1,1]
        self.threshold=2.5
    def MP_Neuron_Input(self):
        print("Enter the number of inputs")
        self.n=int(input())
        print("Enter the threshold value")
        self.threshold=input()
        print("Enter the inputs")
        for i in range(self.n):
            self.inputs[i]=int(input())
        print("Enter the weightage values")
        for i in range(int(self.n)):
            self.weights[i]=int(input())
    def MP_Neuron_Evaluate(self):
        summ=0
        for i in range(self.n):
            summ=summ+self.inputs[i]*self.weights[i]
        if(summ>float(self.threshold)):
            return 1
        else:
            return 0
