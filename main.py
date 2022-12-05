#Q18 WAP to create a calculator.
a,b,c=float(input("Enter the first number: ")),input("operator:"),float(input("Enter the second number: "))
if b=='+':
    print(a,"+",c,"=",a+c)
if b=='-':
    print(a,"-",c,"=",a-c)
if b=='*':
    print(a,"*",c,"=",a*c)
if b=='%':
    print(a,"%",c,"=",a%c)
if b=='/':
    print(a,"/",c,"=",a/c)
if b=='**':
    print(a,"**",c,"=",a**c)
if b=='//':
    print(a,"//",c,"=",a//c)
