#(Lambda functions or Annonymous
# Not declared in the standard manner by using def keyword
# Use to create small anonymous functions
# lambda [arg1 [,arg2,....argn]]:expression)

#sum variable contains this lambda function. so use sum to call the function.
sum = lambda num1, num2 : num1 + num2
#calling the lambda function
print("sum of two numbers",sum(2,3))