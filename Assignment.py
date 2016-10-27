from graph import Queue, bfs, getPath
import sys

Graph = {}
array = []



#                                 ***************************************************************************

                               #A function which is comparing words entered by user to compare character by character


def WordGraph(file):                                         
    w = {}
    f = open("dictionary.txt")                                     #opening the dictionary file
    dicwords = f.read().split('\n')                          #reading the words from dictionary and then spliting them

    for word in dicwords:                                    #Traversing through all words of the dictionary

        for i in range(len(word)):                           #counting the length of each word
            wordhidden = word[:i] + '#' + word[i + 1:]       #adding hashes on each word     
            if wordhidden in w:
                w[wordhidden].append(word)                   #appending the word to use for comparison later
            else:
                w[wordhidden] = [word]

    for key in w:
        wordlist = w[key]
        for fw in wordlist:
            for sw in wordlist:
                if fw != sw:
                    WordInput(fw, sw)                        #loops are working to compare every word by comparing them character by character





#                              ***************************************************************************


                          #A function which is making chains of all words with all possible options


def Executioner(file):                                         
    w = {}
    f = open("dictionary.txt")                                     #opening the dictionary file
    dicwords = f.read().split('\n')                          #reading the words from dictionary and then spliting them

    for eachword in dicwords:
        for word in dicwords:
            if eachword in Graph:
                start = Graph[eachword];
                if word in Graph: 
                  if(eachword != word):
                   finish = Graph[word]
                  
                   predecessors = bfs(start, finish, Graph) 
                   if(predecessors != ''):
                    path = getPath(start, finish, predecessors) ;
                    str = '';
                    array.append(path);
                    for p in path: 
                     str += p + ' -> ';
                    print (str[:-3])  
           




#                                 ***************************************************************************

                    #A class which is giving name to the words which has no chain or extending the neighbours if chain is possible

class Root:

    def __init__(self, name):
        self.name = name
        self.neighbours = []

    __slots__ = ('name', 'neighbours')

    def __str__(self):
        result = self.name + ' : '
        for n in self.neighbours:
            result += n.name + ', '
        return result[:-1]









#                                 ***************************************************************************

                  #A function which is checking if the word which has no chain or extending the neighbours if chain is possible using class Root






def WordInput(fword, sword):                                #WordInput function taking two words as input

    if fword not in Graph:
        node = Root(fword)
        node.neighbours.append(Root(sword))
        Graph[fword] = node
    else:

        neighbours = Graph[fword].neighbours

        if fword not in [x.name for x in neighbours]:
            neighbours.append(Root(sword))

    if sword not in Graph:
        node = Root(sword)
        node.neighbours.append(Root(fword))
        Graph[sword] = node
    else:

        neighbours = Graph[sword].neighbours

        if fword not in [x.name for x in neighbours]:
            neighbours.append(Root(fword))








#                                 ***************************************************************************
                                                                #Main function
                  



if __name__ == '__main__':                                      

    Graph = {}

    
    file="dictionary.txt"

    WordGraph(file) 

                                                                # Taking input from Users for two words to make a word ladder
    fword = raw_input('Enter the first word :')
    sword = raw_input('Enter the second word :')

     
    if len(sys.argv) > 1:


        fword=sys.argv[1]
        sword=sys.argv[2]

    if fword in Graph:

        start = Graph[fword]
        
        if sword in Graph:
            finish=Graph[sword]
            predecessors = bfs(start, finish, Graph)            #calling bfs function from graph.py
            path = getPath(start, finish, predecessors)         #calling getpath function from graph.py
            str = ''

            for p in path:

                str += p + ' -> '                               #printing the chain by replacing letters from first word to second

            print (str[:-3]) 
	    
    	
        else:
             print("Second Word is not found in Graph") 

	
    else:
        print("First Word is not found in Graph")

    Executioner(file)


			

			
			
