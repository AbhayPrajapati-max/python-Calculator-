def show_history():
 with open(r'c:\Users\91930\Desktop\Start Web\Python Projects\History.txt','r') as f:
    
     lines=f.readlines()
     if len(lines)==0:
        print('there no History')
     else:
        f.seek(0)
        print(f.read())

def clear_history():
   with open(r'c:\Users\91930\Desktop\Start Web\Python Projects\History.txt','w') as f:
    print('History cleared ')
def save_to_history(equa,result):
    with open(r'c:\Users\91930\Desktop\Start Web\Python Projects\History.txt','a') as f:
         f.write(equa+'='+str(result)+'\n')
def calculate(user_input):
     parts=user_input.split()
     print(len(parts))
     if len(parts)!=3:
        print('Invalid input give e.f(number Operator number)')
        return
     num1=float(parts[0])
     op=parts[1]
     num2=float(parts[2])
     if op=='+':
        result=num1+num2
     elif op=='-':
        result=num1-num2
     elif op=='*':
        result=num1*num2
     elif op=='/':
        if num2==0:
           print('cannot divide by Zero')
           return
        result=num1/num2
        
     else:
        print('Invalid input use + - * /')
     if int(result)==result:
        result=int(result)
     print('Result:',result)              
     save_to_history(user_input,result)
def main():
   print('  This Is Calculator (type history,Clear,Exit)')     
   while True:
      user_in=input('Enter calculation (+ - * /) or command history, clear, exit ').lower()
      if user_in=='exit':
         print('goobye')
         break
      elif user_in=='clear':
         clear_history()
         print('Data has been cleared')
      elif user_in=='history':
         print('This is History ')
         show_history()  
      else:
           calculate(user_in)
main()   
      