"""
Write a function named print_box that accepts two parameters: a string holding a file name, and an integer for a width.
Your function should open that file and reads its contents as a sequence of lines, and display the lines to the console with a 'box' border of # characters around them on all four sides. 
The second parameter to your function indicates the total width of the box including its border. 
You must also convert each line to "title case" by capitalizing the first letter of the line and lowercasing all subsequent letters. For example, suppose the file poem.txt contains the following text:

roses ARE red
VIOLETS Are bl_u_e

All my BASE
ARE belong To YOU
"""
def print_box(filename,width):

        file=open(filename)
        print(width*"#")
        lines = file.readlines()
        lines =[ i.strip() for i in lines]
        lines =[ i.replace("_","") for i in lines]
            
        lines = [ i.capitalize() for i in lines]

        lines[:] = (elem[:width-2] for elem in lines)
    

        for i in range(len(lines)):
            length=int(len(lines[i]))
            if len(lines[i])==0:
                print("#"+(width-2)*' '+"#")
            else:
             
                print("#"+lines[i]+(width-length-2)*" "+"#")
       
        print(width*"#")
