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
''' Implementation of 3 input NAND gate using The Neurons
    x1 x2 x3  Y
    0  0  0   1
    0  0  1   1 
    0  1  0   1
    0  1  1   1
    1  0  0   1
    1  0  1   1
    1  1  0   1
    1  1  1   0
    
    bias=b
    if b+w1*x1+w2*x2+w2*x2>0 output=1
       b+w1*x1+w2*x2+w3*x3<=0 output=0
       
       *for inputs (0,0,0) output will be 1
        b+0+0+0>0
        therfore consider b>0 let's consider b=1
        and further consider w1=w2=w3=1       
       *for inputs (0,0,1) output will be 1
        1+0+0+1>0
        hence the weight and bias satisfy the equation 
       *Likewise,w1=1,w2=1,w3=1,b=1 satisfy the inputs (0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0) 
       
       *When the inputs equal (1,1,1):-
                1+1*1+1*1+1*1=4>0
                but it must be <0 as the output is 0
                w1=1,w2=1,w3=1,b=1 doesn't satisfy the three input NAND gate.
        * Let's put w1=-1,w2=-1,w3=-1,b=3
            it will satisfy the truth table for all inputs.
         
Hence, weights and bias values for 3 input NAND gate will be
w1=-1,w2=-1,w3=-1,bias=3'''
    
    
