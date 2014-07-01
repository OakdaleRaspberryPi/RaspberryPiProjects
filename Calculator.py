#!/usr/bin/env python
2.
3.import random 
4.import cPickle 
5.
6.class Hangman(object):
7.    '''A simple hangman game that tries to improve your vocabulary a bit '''
8.    def __init__(self):
9.        # the variables used, this is not necessary
10.        self.dumpfile = ''       #the dictionary file
11.        self.dictionary = {}     #the pickled dict
12.        self.words = []          #list of words used
13.        self.secret_word = ''    #the 'key'
14.        self.length = 0          #length of the 'key'
15.        self.keys = []           #inputs that match the 'key'
16.        self.used_keys = []      #keys that are already used
17.        self.guess = ''          #player's guess
18.        self.mistakes = 0        #number of incorrect inputs
19.        
20.        return self.load_dict()
21.        
22.    #insert some random hints for the player
23.    def insert_random(self, length):
24.        randint = random.randint
25.        
26.        # 3 hints
27.        if length >= 7: hint = 3
28.        else: hint = 1
29.        for x in xrange(hint):
30.                a = randint(1, length - 1)
31.                self.keys[a-1] = self.secret_word[a-1]
32.
33.    def test_input(self):
34.        #if the guessed letter matches
35.        if self.guess in self.secret_word:
36.            indexes = [i for i, item in enumerate(self.secret_word) if item == self.guess]
37.            for index in indexes:
38.                self.keys[index] = self.guess
39.                self.used_keys.append(self.guess)
40.                print "used letters ",set(self.used_keys),'\n'
41.       
42.        #if the guessed letter didn't match
43.        else:
44.            self.used_keys.append(self.guess)
45.            self.mistakes += 1
46.            print "used letters ",set(self.used_keys),'\n'
47.    
48.
49.    # load the pickled word dictionary and unpickle them    
50.    def load_dict(self):
51.        try :
52.            self.dumpfile = open("~/python/hangman/wordsdict.pkl", "r")
53.        except IOError:
54.            print "Couldn't find the file 'wordsdict.pkl'"
55.            quit()
56.        self.dictionary = cPickle.load(self.dumpfile)
57.        self.words = self.dictionary.keys()
58.        self.dumpfile.close()
59.        return self.prepare_word()
60.    
61.    #randomly choose a word for the challenge
62.    def prepare_word(self):
63.        
64.        self.secret_word = random.choice(self.words)
65.        #don't count trailing spaces
66.        self.length = len(self.secret_word.rstrip())
67.        self.keys = ['_' for x in xrange(self.length)]
68.        self.insert_random(self.length)
69.        return self.ask()
70.
71.    #display the challenge
72.    def ask(self):
73.        print ' '.join(self.keys), ":", self.dictionary[self.secret_word] 
74.        print 
75.        return self.input_loop()
76.
77.    #take input from the player
78.    def input_loop(self):
79.        #four self.mistakes are allowed
80.        chances = len(set(self.secret_word)) + 4          
81.        while chances != 0 and self.mistakes < 5:
82.            try:
83.                self.guess = raw_input("> ")
84.                
85.            except EOFError:
86.                exit(1)
87.            self.test_input()
88.            print ' '.join(self.keys)
89.            if '_' not in self.keys:
90.                print 'well done!'
91.                break
92.            chances -= 1
93.       
94.        if self.mistakes > 4: print 'the word was', ''.join(self.secret_word).upper()
95.        return self.quit_message()
96.    
97.    def quit_message(self):
98.        print "\n"
99.        print "Press 'c' to continue, or any other key to quit the game. "
100.        print "You can always quit the game by pressing 'Ctrl+D'"
101.        try:
102.            command = raw_input('> ')
103.            if command == 'c': return self.__init__() #loopback
104.            else : exit(0)
105.        except EOFError: exit(1)
106.            
107.        
108.        
109.        
110.
111.
112.if __name__ == '__main__':
113.    game = Hangman()
114.    game.__init__()
