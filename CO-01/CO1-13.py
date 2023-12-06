x=input("Enter the list of colors separated by commas:")
colors=x.split(",")
if len(colors)>=2:
    first_color=colors[0]
    last_color=colors[-1]
    print (first_color,f"first color")
    print (last_color,f"last color")
else:
    print ("Enter minimum 2 colors")
    
