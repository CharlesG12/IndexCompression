import Encoding

gaps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

encoder = Encoding.Encoding()

en_gamma_gaps = encoder.run(gaps, "g")
en_delta_gaps = encoder.run(gaps, "d")

print("gap    gamma encode    delta encode")
for i in gaps:
    print(str(i) + "  " + str(encoder.gamma_encoding(i)) + "  " + str(encoder.delta_encoding(i)), end="")
    print()







