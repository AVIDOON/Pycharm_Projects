

def priceCheck(products, productPrices, productSold, soldPrice):
    dict = {}
    count = 0
    for i in range(len(products)):
        product1 = products[i]
        productprice = productPrices[i]
        dict[product1] = productprice

    for i in range(len(productSold)):
        if productSold[i] in dict:
            if soldPrice[i] == dict[products[i]]:
                count += 0
                print("matched")
            else:
                count += 1
                print("not matched")
    return count

unmatched = priceCheck(products=['egg','orange','papaya','apple'],
                       productPrices=[0.32,0.42,1.21,9.2],
                       productSold=['egg','egg','orange','apple'],
                       soldPrice=[0.36,0.32,3.21,9.2])
print(unmatched)