# {value:flags} # Format a value based on what FLAGS are Inserted

price1 = 12.233
price2 = 12343.234543
price3 = 34543

print(f"The price 1:{price1:.2f}")
print(f"The price 1:{price2:.3f}")
print(f"The price 1:{price3:.2f}")
print(f"The price 1:{price1:.<10}")
print(f"The price 1:{price1:>10}")
print(f"The price 1:{price1:^10}")
print(f"The price 1:{price3:+}")
print(f"The price 1:{price3:-}")
print(f"The price 1:{price3:,}")
print(f"The price 1:{price3:+,.2f}")