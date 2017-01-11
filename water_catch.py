from random import randint	

def retention(arg):
    l = len(arg)
    water_map = [0] * l
    water = 0
    for q in xrange(1, l):
        left = arg[0 : q ]
        right = arg[q : l]
        #print(q, left, right)
        water_map[q] = max(min(max(left), max(right)) - arg[q], 0)
        water += water_map[q]

    print "Water held:" 
    print water
    print "_______________________________"
    display_rain(arg, water_map)

	
def display_rain(arg, water_map):
    top = max(arg)
    for n in xrange(top):
        print(top - n)
        layer = " "
        j = 0
        for m in arg:
            layer += " "
            if (m >= top - n):
                layer += "x"
            elif (water_map[j] + m >= top - n ):
                layer += "-"
            else:
            	layer += " "
            j += 1
        print layer

    print("----------------------------")
	
input = []
for n in xrange(15):
    input.append(randint(0,8))
retention(input)