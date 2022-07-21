#GST CALCULATION
#INPUT AS PRICE AND RATE(in %)

#function to calculate gst
def calculateGst(price,rate):
    cgstPrice = price + (rate / 200)*price
    sgstPrice = price + (rate / 200)*price
    totalPrice = cgstPrice + sgstPrice
    print("Actual price of item: {}".format(price))
    print("Price after CGST: {}".format(cgstPrice))
    print("Price after SGST: {}".format(sgstPrice))
    print("Price after GST: {}".format(totalPrice))

#input values
price = int(input("Enter the price of the item: "))
rate = int(input("Enter the GST rate of the item: "))
#call function
calculateGst(price,rate)
