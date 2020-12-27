# Freshworks-Engineering
Solution of the Problem statement for Freshworks Hiring.\
These are the commands to use the code file.

#### Run the module of `.py` and import `assignment` as library, Here, we need to import the code file as a library, it can be the name of the main code file.

## Python commands to use to run the program.
`import assignment as agni`\
`agni.create("utkarsh",1)`\
`agni.create("assignment",23,3600)`\
`agni.read("utkarsh")`\
`agni.read("assignment")`\
`agni.create("sid",812)`\
`agni.modify("utkarsh",424)`\
`agni.delete("utkarsh")`


## Also supports multithreading, one can access the same like:
`t1=Thread(target=(create/read/delete),args=(key_name,value,runtime))`\
`t1.start()`\
`t1.sleep()`\
`t2=Thread(target=(create/read/delete),args=(key_name,value,runtime))`\
`t2.start()`\
`t2.sleep()`
