#!/usr/bin/env python
# coding: utf-8

# In[3]:


from textgenrnn import textgenrnn
from termcolor import colored
import sys

textgen_demo = textgenrnn(weights_path='demo_model_weights.hdf5',
                       vocab_path='demo_model_vocab.json',
                       config_path='demo_model_config.json')


# In[13]:

print("  \
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\
██╗███╗   ██╗ ██████╗ ██████╗ ███████╗\n\
██║████╗  ██║██╔═══██╗██╔══██╗██╔════╝\n\
██║██╔██╗ ██║██║   ██║██║  ██║█████╗  \n\
██║██║╚██╗██║██║   ██║██║  ██║██╔══╝  \n\
██║██║ ╚████║╚██████╔╝██████╔╝███████╗\n\
╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ ╚══════╝\n\
\n\
")

print(colored('Query Autocompletion Demo using ', 'cyan'), end="") 
print(colored('bi-LSTMs', 'yellow'))


def static():
    flag=True
    while flag==True:
        print(colored("Start typing your query and press ENTER at any time for suggestions:\n\n\n\n\n ", 'green'))
        input1 = input() 
        print(colored(" \nSuggestions:", 'cyan'))
        print(textgen_demo.generate(n=3, prefix=input1, temperature=0.2, progress= False))
        print("===")
        print(colored("Continue? Y/N", 'green'))
        input2 = input()
        if input2 == 'N' or input2 =='No' or input2 == 'no' or input2 == 'n':
            flag = False
            print(colored('===Terminating...====', 'green'))
        elif input2 == 'Yes' or input2 == 'Y' or input2 == 'yes' or input2 == 'y':
            flag = True
            print(colored('===Next query====', 'cyan'))
        else: 
            flag = False
            print(colored('=== Invalid answer, terminating...====', 'red'))



def interactive():
    flag=True
    while flag==True:
        print(colored("Start typing your query and press ENTER at any time for suggestions:\n\n\n\n\n ", 'green'))
        input1 = input() 
        print(colored(" \nSuggestions:", 'cyan'))
        print(textgen_demo.generate(interactive=True, prefix=input1, max_gen_length=300,progress=False, temperature=0.2))
        print("===")
        print(colored("Continue? Y/N", 'green'))
        input2 = input()
        if input2 == 'N' or input2 =='No' or input2 == 'no' or input2 == 'n':
            flag = False
            print(colored('===Terminating...====', 'green'))
        elif input2 == 'Yes' or input2 == 'Y' or input2 == 'yes' or input2 == 'y':
            flag = True
            print(colored('===Next query====', 'green'))
        else: 
            flag = False
            print(colored('=== Invalid answer, terminating...====', 'red'))


if __name__ == '__main__':
    globals()[sys.argv[1]]()
        


# 
