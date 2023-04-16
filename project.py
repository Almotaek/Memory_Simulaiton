#Author: Khalid Almotaery
#Date: 4/16/2023

from optparse import OptionParser
import random
import math


######

#The simulation code starts in line 289

######

# Page Class
class Page:
    def __init__(self,index):
        self.index = index
        self.hexValue = 0x0 #page value in hex
        self.hexString = "" #page value as a string
        shifts = (options.pagesize)*2

        #Create random string of hex values sized according to the page size
        for i in range(0,shifts):
            self.hexValue = self.hexValue << 4
            randHex = int(hex(random.randrange(0,16)),16)
            self.hexValue = self.hexValue | randHex
        
        self.hexString = hex(self.hexValue)

#Virtual Address
class VirtualAdress:  
    def __init__(self,numBits):
        self.VA = ""
        #create random virtual address
        for i in range(0,numBits):
            self.VA = self.VA + str(random.randrange(0,2))

#Virtual Address Organiztion Procedure
def VASimualtion():
    print('Virtual Address Organiztion Simulation')
    print('')

    virtualSizeBytes = options.virsize

    virtualPages = math.floor(virtualSizeBytes/options.pagesize) #find the number of virtual pages
    
    #create random virtual address space
    VAPages = [] # each entry in the array is virtual page.
    for i in range(0,virtualPages):
        page = Page(i)
        VAPages.append(page)

    #print pages 
    i = 0
    for page in VAPages:
        print("Page #"+str(i)+": "+page.hexString)
        i = i + 1
        
    print('')

    #Pick  Virtual Addresses for the question
    VAs = [] 
    #VA number of bits 
    numVABits = int(math.log(len(VAPages)*options.pagesize,2))
    for i in range(0,10):
        va = VirtualAdress(numVABits)  
        VAs.append(va) 

    if options.solve == False:
        #ask the user to find the byte given the VA 
        i = 0
        for v in VAs:
            print("Virtual Address #"+str(i)+": "+v.VA+" find the refrenced word value -------------> ?")
            i = i + 1
        print('')

    #solve it
    if options.solve:
        #Find the number of bits needed for VPN and OFFSET 
        numOffsetBits = int(math.log(options.pagesize,2))
        numVPNBits = int(math.log(len(VAPages),2))

        VPNMASK = ""
        OFFSETMASK = ""

        #VPN mask
        for i in range(0,numVABits):
            if i < numVPNBits:
                VPNMASK = VPNMASK + "1"
            else:
                VPNMASK = VPNMASK + "0"
        
        VPNMASK = int(VPNMASK,2)

        #offset mask
        for i in range(0,numVABits):
            if i < numVPNBits:
                OFFSETMASK = OFFSETMASK + "0"
            else:
                OFFSETMASK = OFFSETMASK + "1"
        
        OFFSETMASK = int(OFFSETMASK,2)

        i = 0
        #For each VA, find the corresponding word
        for v in VAs:
            testVA = v
            testVA = int(testVA.VA,2)
            #Getting offset value
            OFFSET = testVA & OFFSETMASK

            #Getting VPN value
            VPN = testVA & VPNMASK

            VPN = VPN >> numOffsetBits

            #find the page vpn points to
            refPage = VAPages[VPN]
            pageContents = refPage.hexString
            pageContents = str(pageContents).split("0x")[1]

            #Find answer based on word size
            loop = int(math.floor(options.wordsize/8))
            if loop <= 1:
                loop = 1
            byte = "0x"
            for y in range(0,loop * 2):
                byte = byte + pageContents[(OFFSET*2)+y]
            print("Virtual Address #"+str(i)+": "+v.VA+" refrenced word value -------------> "+byte)
            i = i + 1
        print('')
    
    
#Page Table Size Procedure
def PTSSimualtion():
    print('Page Table Size Simulation')
    print('')
    for q in range(0,6):
        print('Question #'+str(q+1))
        print('')

        #give random phy mem, virt mem, and cntrl bits, ask for page table size and a drawing
        #pick random page size
        pagesize = 1 << random.randrange(2,4)
        #pick random virtual address space (multipule of 2) in bytes
        virtualAddressSpace = 1 << random.randrange(math.log(pagesize,2)+1,5)
        #pick random phy address space in bytes
        phyAddressSize = 1 << random.randrange(math.log(pagesize,2)+1,9)
        #pick random cntrl bits
        cntrlBits = random.randrange(0,10)

        print('')
        print("Page Size: "+str(pagesize)+" bytes")
        print(str(virtualAddressSpace)+"-bit Virtual Addressing")
        print("Physical Memeory: "+str(phyAddressSize)+" bytes")
        print("Control Bits : "+str(cntrlBits)+" bits")
        print('')

        if options.solve:
            #Given virtual addressing and page size, find the number of virtual pages.
            numVirtPages = math.ceil((2**virtualAddressSpace)/(pagesize))

            #Find the number of physical pages given physical memory size and page size 
            numPhyPages = math.ceil(phyAddressSize/pagesize)  
            
            #Find the number of bits needed to represent the physcial frames so that we know the page table width
            phyAddressSpace = math.ceil(math.log(numPhyPages,2))

            #Page table width
            pageTableWidth = phyAddressSpace + cntrlBits
            
            #Padding
            while(pageTableWidth%8 != 0):
                pageTableWidth = pageTableWidth + 1

            pageTableHeight = numVirtPages

            #Padding
            while(pageTableHeight%8 != 0):
                pageTableHeight = pageTableHeight + 1

            pageTableSize = pageTableHeight * pageTableWidth

            #Outline the steps of solving it here.
            print('Solution Steps: ')
            print('')
            print('Find the number of physical pages')
            print('     Number of Physical Pages = Physical Size/Page Size')
            print('     Number of Physical Pages = '+str(phyAddressSize)+' bytes/'+str(pagesize)+" bytes")
            print('     Number of Physical Pages = '+str(numPhyPages))
            print('Find the number of virtual pages')
            print('     n-bit virtual addressing contins 2^n bytes')
            print('     '+str(virtualAddressSpace)+'-bit virtual addressing contins 2^'+str(virtualAddressSpace)+' bytes')
            print('     # of vitual pages = 2^'+str(virtualAddressSpace))
            print('Find the number of bits needed to address the physical memory')
            print('     n-bit physical addressing contins 2^n bytes')
            print('     # of bits needed to address phy mem = log(number of physical pages)')
            print('     # of bits needed to address phy mem = log('+str(numPhyPages)+')')
            print('Find page table width')
            print('     Page Table Width = # of bits needed to address phy mem + control bits')
            print('     Page Table Width = '+str(phyAddressSpace)+' bits + '+str(cntrlBits)+" bitss")    
            print('     Page Table Width (padded to the nearst byte)= '+str(pageTableWidth)+" bytes")    
            print('Find page table height')
            print('     Page Table Height = number of virtual pages')
            print('     Page Table Height (padded to the nearst byte)='+str(pageTableHeight)+" byte")
            print('Find page table size')
            print('     Page Table Size = Page Table Height x Page Table Width')
            print('     Page Table Size = '+str(pageTableHeight)+' X '+str(pageTableWidth)+" bytes")
            print('')
            print("     Page Table Size = "+str(pageTableSize)+" bytes")
            print('')
        else:
            print("Page Table Size = ?")
            print('')
            print("Given the previous specifications, find the Page Table Size padded to the neareast byte")
            print('')




#Page Table Entry Organization Procedure
def PTESimualtion():
    print('Page Table Entry Organization Simulation')
    print('')
    #Given the following physical, virtual memory and control bits, draw the page table

    #make virtual mem
    virtualSizeBytes = options.virsize

    virtualPages = math.floor(virtualSizeBytes/options.pagesize)

    VAPages = []
    for i in range(0,virtualPages):
        page = Page(i)
        VAPages.append(page)

    #Create random phyical memory that can have invalid pages
    print('Physical Memory')
    print('')
    phySizeBytes = options.physize

    numPhyPages = math.floor(phySizeBytes/options.pagesize)

    phyPages = []
    
    for i in range(0,numPhyPages):
        valid = random.randrange(0,2) # randomly make an invalid page
        page = Page(i)
        if valid == 0:
            page.hexString = "0x0"
            page.hexValue = 0x0
        phyPages.append(page)
            
    #Print physcial pages 
    i = 0
    for page in phyPages:
        print("Physical Frame #"+str(i)+": "+page.hexString)
        i = i + 1
    print('')

    #Find # of VPN bits
    numVPNBits = int(math.log(len(VAPages),2))
    #Find # of PPN bits
    numPPNBits = int(math.log(len(phyPages),2))

    print('Page Table')
    print('')

    i = 0
    for page in VAPages:
        bit = "0" #Valid bit
        ran = random.randrange(0,len(phyPages)) #pick a randiom physical page frame that would be tranlated to the current virtual page
        if phyPages[ran].hexString != "0x0":
            bit = "1" #Valid 
        if options.solve == False:
            #Print Page Table Entry and ask question
            print(format(i,'0'+str(numVPNBits)+'b')+'|'+format(ran,'0'+str(numPPNBits)+'b')+bit+" --------> Physical Frame Contents in hex ?")
        else:
            #Find the corresponding frame
            answer = ""
            if bit == "0":
                answer = "Not Valid"
            else:
                answer = phyPages[ran].hexString
            #Print Page Table Entry and answer
            print(format(i,'0'+str(numVPNBits)+'b')+'|'+format(ran,'0'+str(numPPNBits)+'b')+bit+" --------> "+answer)
        i = i + 1
    if options.solve == False: 
        print('')
        print('Given the previous physical memory and the page table, find the contents of the physical frame. Note: there is a valid bit in each page table entry.')
        print('')



#Start


#Options parser
parser = OptionParser()

#defining options
parser.add_option('-t', '--type',default="VA",help='type of simulator. For Virtual Address Organiztion, enter VA. For Page Table Size, enter PTS. For Page Table Entry Organization, enter PTE.', action='store', type='string', dest='type')
parser.add_option('-s', '--seed',   default=0,     help='the random seed',  action='store', type='int', dest='seed')
parser.add_option('-c',  help='compute answers for me', action='store_true', default=False, dest='solve')
parser.add_option('-p', '--physical',default=512,help='physical memory size ', action='store', type='int', dest='physize')
parser.add_option('-v', '--virtual',default=512,help='virtual memory size ', action='store', type='int', dest='virsize')
parser.add_option('-f', '--frame',default=64,help='frame/page size ', action='store', type='int', dest='pagesize')
parser.add_option('-w', '--word',default=8,help='machine word', action='store', type='int', dest='wordsize')

#options object
(options, args) = parser.parse_args()


#Picking seed
random.seed(options.seed)


#options message
if options.type != "PTS":
    print('')
    print('type is: ',               options.type)
    print('seed is: ',               options.seed )
    print('virtual mem size is: ', str(options.virsize) + " bytes")
    print('phys mem size is: ',      str(options.physize)+ " bytes")
    print('page size is: ',          str(options.pagesize) + " bytes")
    print('word size is: ',          str(options.wordsize) + " bits")
    print('')


#Virtual Page Organization Simulation
if options.type == "VA":
    VASimualtion()
if options.type == "PTS":
    PTSSimualtion()
if options.type == "PTE":
    PTESimualtion()





exit(0)
