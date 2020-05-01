import numpy as np 
import matplotlib.pyplot as plt 
import sys   
import math 
import argparse  

# PDF is not your protected document file 
# It is probability distribution function 
class PDF: 
    
    def __init__(self,fileName): 
        self.file=fileName
        self.colID=0     
        self.nbins=50   
        self.normalize=False 
        self.outFile='out_pdf.dat' 
        self.normType='sum' 
        self.outFile='out.dat' 
        self.writeStatus=False 
    
    def exe(self): 
        self.readFile() 
        self.getPDF() 
        self.plot() 
        
        if self.writeStatus: 
            self.write() 
    
    def setWriteStatus(self):
        self.writeStatus=True 

    def setNormType(self,normType): 
        self.normType=normType 

    def setColID(self,colID): 
        self.colID=colID 

    def setNormalize(self,boolOpt): 
        self.normalize=boolOpt 

    def setBins(self,nbins):
        self.nbins=nbins 

    def setOutFile(self,outFile): 
        self.outFile=outFile 


    def plot(self): 
        plt.scatter(self.binValues,self.pdf,color='red',s=20)
        plt.xlabel(r'$x$')	
        plt.ylabel(r'$\rho(x)$') 
        plt.show() 

    def readFile(self): 
        fileHandler=open(self.file,'r') 
        lines=fileHandler.readlines() 

        self.data=[] 
        for line in lines: 

            if line.startswith('#'): 
                continue 
            if line.startswith('@'): 
                continue 
            elif not  line.strip(): 
                continue 
            keys=line.split() 
            idata=float(keys[self.colID])
            self.data.append(idata)

        fileHandler.close() 
    
    def getPDF(self): 

        maxVal=max(self.data) 
        minVal=min(self.data) 
        offset=(maxVal-minVal)*0.001  # 0.1% offset for span of data
        start=minVal-offset 
        end=maxVal+offset 
        
        binWidth=(end-start)/float(self.nbins) 

        self.pdf=list(np.zeros(self.nbins))
        
        self.binValues=list(np.zeros(self.nbins))  


        for i in range(self.nbins):  
            self.binValues[i]=start+(i+0.5)*binWidth 

        for i in range(len(self.data)):
            idx=math.floor((self.data[i]-start)/binWidth) 
            self.pdf[idx]+=1 

        if(self.normalize): 
            # Normalize such that sum(binWidth*height[i])=1
            if self.normType=='sum': 
                for i in range(self.nbins):
                    self.pdf[i]=self.pdf[i]/(float(len(self.data)))  
            elif self.normType=='integral': 
                for i in range(self.nbins):
                    self.pdf[i]=self.pdf[i]/(binWidth*float(len(self.data)))  
    def write(self): 
        fileHandler=open(self.outFile,'w') 

        for i in range(self.nbins): 
            fileHandler.write('%16.8f%16.8f\n'%(self.binValues[i],self.pdf[i]))




    


def main(): 
    
    parser=argparse.ArgumentParser(
        description='Quickly plot probability distribution from CLI'
    ) 
    
    parser.add_argument('file',
        type=str,
        help='Name of the input file'
    )
    
    parser.add_argument('-nbins',
        type=int,metavar='',
        help='set number of bins, default is 50'
    ) 
    parser.add_argument('-o','--out-file',
        metavar='',type=str,
        help='output file to write pdf'
    )  
    
    parser.add_argument('-c','--column',
        metavar='',type=int,
        help='Column ID of data for analysis, default is 0'
    ) 

    # parser.add_argument('-bw','--bin-width',
    #     metavar='',type=float,
    #     help="set the width of bin. Don't specifiy both -nbins and -bw together"
    # )
    
    parser.add_argument('-n','--normalize',
        action='store_true',
        help='Set normalize true, default false'
    )
    
    parser.add_argument('-nt','--norm-type',
        metavar='',
        help="1) sum: sum of all bin heights is 1" + 
        "2) integral: sum of (binwidth X bin height) is 1," + 
        "default is sum "
        ) 
    
    parser.add_argument('-w','--write',
        action='store_true',
        help='Flag for writing results into a file,'+
        'default is not set'
    )


    args=parser.parse_args() 

    fileName=args.file 
    myPDF=PDF(fileName) 

    if args.column: 
        myPDF.setColID(args.column)

    if args.nbins: 
        myPDF.setBins(args.nbins) 

    if args.normalize: 
        myPDF.setNormalize(True) 
        if args.norm_type: 
            myPDF.setNormType(args.norm_type)
   
    if args.write: 
        myPDF.setWriteStatus() 
        if args.out_file: 
            myPDF.setOutFile(args.out_file) 

    myPDF.exe()  

if __name__=='__main__': 
    main() 	
 

 
