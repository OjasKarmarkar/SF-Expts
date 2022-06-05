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

def binary_sub(q,m):
    converted=two_comp(m)
    #print(f'asas {b}')
    res=binary_add(q,converted)
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

def shift_right(aReg , qReg):
    new_bit=aReg[-1]
    aReg=[aReg[0]]+aReg
    aReg=aReg[:-1]

    q_pop=qReg[-1]
    qReg=[new_bit]+qReg
    qReg=qReg[:-1]

    return {
        "a":aReg,
        "q":qReg,
        "q0":q_pop
    }

print("Enter two numbers to multiply : ")
x,y=map(int , input(' ').split())
a , b = abs(x) , abs(y)
q_reg=DecimalToBinary(b)
m_reg=DecimalToBinary(a)
if y<0:
  q_reg=two_comp(q_reg)
if x<0:
  m_reg=two_comp(m_reg)

a_reg=[0]*len(q_reg)
a_steps=['0'*len(q_reg)]
q_steps=["".join(map(str,q_reg))]
q1_steps=['0']


def calc(a_reg , q_reg):
    mx=m_reg
    count=len(q_reg)+1
    global qLast
    qLast=0
    while(count>1):
    #compare Q and Q0:
        if q_reg[-1]==1 and qLast==0:
            
            a_reg= binary_sub(a_reg , mx)
           
        elif q_reg[-1]==0 and qLast==1:

           # print(f'{a_reg} add {m_reg}')
            a_reg= binary_add(a_reg , mx)
        shiftR=shift_right(a_reg , q_reg)
        qLast=shiftR['q0']
        a_reg=shiftR['a']
        q_reg=shiftR['q']
        count-=1
        a_steps.append("".join(map(str,a_reg)))
        q_steps.append("".join(map(str,q_reg)))
        q1_steps.append(q_reg[-1])
        #print(f'A - {a_reg} Q - {q_reg} , Q Comp - {q_reg[-1]}{qLast}')
    if (x<0 and y>0) or (x>0 and y<0):
      return -abs(int("".join(map(str,two_comp(a_reg+q_reg))) , 2))
    else:
      return int("".join(map(str,a_reg+q_reg)) , 2)

final_result=calc(a_reg , q_reg)

print ("{:<8} {:<15} {:<10}".format('A','Q','Q-1'))
for a,q,q0 in zip(a_steps,q_steps,q1_steps):
    print ("{:<8} {:<15} {:<10}".format( a, q, q0))
print(f"The result is : {final_result}")


        



    