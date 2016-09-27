

p = [0.2,0.2,0.2,0.2,0.2]

world = ['green','red','red','green','green']
measurements = ['red','red']
motion = [1,1]
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1


def sense(p,Z):
    qVector = []
    sum = 0
    for i in range(len(p)):
        hit = (Z==world[i])
        if (Z == world[i]):
            q = p[i]*pHit
        else:
            q = p[i]*pMiss
            
        sum += q
        qVector.append(q)
        
        
    for i in range(len(p)):
        qVector[i] = qVector[i]/sum
        
    return qVector

def move(p,U):
    q = []
    
    
    for i in range (len(p)): 
        s =  (pExact * p[(i-U) % len(p)] ) + \
                ( pOvershoot * p[(i-U - 1) % len(p)] ) + \
                ( pUndershoot *  p[(i-U + 1) % len(p)] )
        q.append(s)

    
    return q
     
#for j in range(len(measurements)):
#    p = sense(p,measurements[j])

for i in range(len(motion)):
    p = sense(p, measurements[i])
    p = move(p,motion[i])
    
print p