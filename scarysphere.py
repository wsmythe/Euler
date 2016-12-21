
#r is the radius of the sphere
r = 2047
total = 0
triples = []
for i in xrange(r+1):
    for j in  xrange(r+1):
        if (r*r-i*i-j*j >= 0 ):
            k = (r*r-i*i-j*j)**0.5
            if (k - int(k) == 0.0 ):

                triples.append([i,j,int(k)])

                if (i*j*k != 0 ):
                    transform = 8
                elif (( ( i or j ) == 0 ) or ( (j or k) ==0) or ((i or k) ==0)):
                    transform = 2
                else:
                    transform = 4
                total = total + ( i + j + int(k) ) * transform
                print [ i, j, int(k), transform ]

print(total)
