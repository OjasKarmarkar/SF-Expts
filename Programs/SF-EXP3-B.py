def DecimalToBinary(num):
    results=list(map(int , bin(num)[2:]))
    if len(results)==4:
      results=[0]+results
    if len(results)==3:
      results=[0]+[0]+results
    elif len(results)==2:
        results=[0]+[0]+[0]+results

    return results

def binary_add(q,m):
  result=[]
  carry=0
 
  for a_item , b_item in zip(q[::-1],m[::-1]):
    addn=0
    if a_item+b_item+carry==3:
        addn=1
    elif a_item+b_item+carry==2:
        addn=0
    else:
        addn=a_item+b_item+carry

    carry=1 if a_item+b_item+carry>1 else 0
    result.append(addn)
  return result[::-1]

def binary_sub(a,m):
    converted=two_comp(m)
    #print(f'asas {b}')
    res=binary_add(a,converted)
    m=two_comp(m)
    return res

def two_comp(x):
  add_one=[0 for i in range(len(x))]
  add_one.append(1)
  for index , val in enumerate(x):
    if int(val)==0:
      x[index]=1
    else:
      x[index]=0
   
  r = binary_add(x,add_one)
  return r

print("Enter two numbers to divide  (A/B) : ")
x,y=map(int , input(' ').split())
a , b = abs(x) , abs(y)
q_reg=DecimalToBinary(a)
m_reg=DecimalToBinary(b)
if y<0:
  q_reg=two_comp(q_reg)
if x<0:
  m_reg=two_comp(m_reg)
 
m_reg=[0]+m_reg
a_reg=[0]*(len(q_reg)+1)
a_steps=['0'*(len(q_reg)+1)]
q_steps=["".join(map(str,q_reg))]


def shift_left(aReg , qReg):
   
    new_bit=qReg[0]
    qReg=qReg[1:]
   
    aReg=aReg[1:]
    aReg=aReg+[new_bit]



    return {
        "a":aReg,
        "q":qReg
    }



def calc(a_reg , q_reg):
    mx=m_reg
    count=len(q_reg)+1
    global qLast
    qLast=0
    while(count>1):

        shiftL=shift_left(a_reg , q_reg)
        a_reg=shiftL['a']
        q_reg=shiftL['q']
        if a_reg[0]==1:
          # A is negative
          a_reg=binary_add(a_reg , mx)
        
        else:
          # A is positive
          a_reg = binary_sub(a_reg , mx)

        if a_reg[0]==0:
            q_reg=q_reg+[1]
        else:
            q_reg=q_reg+[0]
    
        count-=1
        a_steps.append("".join(map(str,a_reg)))
        q_steps.append("".join(map(str,q_reg)))
    
    if a_reg[0]==1:
      a_reg = binary_add(a_reg , mx)

    rem= int("".join(map(str, a_reg)),2)
    quo= int("".join(map(str, q_reg)),2)
    return quo , rem
         
quo , rem = calc(a_reg , q_reg)
print ("{:<15} {:<10}".format('A','Q'))
for a,q in zip(a_steps,q_steps):
    print ("{:<15} {:<10}".format(a, q))
print(f"\nQuotient : {quo} , Remainder : {rem} ")