class Encoding:
    def __init__(self):
        self.codes = []

    def run(self, gaps, encode_type):
        self.codes = []
        for i in range(len(gaps)):
            gap = gaps[i]
            if encode_type == "g":
                encode = self.gamma_encoding(gap)
                self.codes.append(encode)
            elif encode_type == "d":
                encode = self.delta_encoding(gap)
                self.codes.append(encode)
        return self.codes

    def gamma_encoding(self, gap):
        b_code = format(gap, "b")
        offset = b_code[1:]
        len_offset = len(offset)
        unary_len = self.unary(len_offset)

        # print("gap " + str(gap) + " binary: " + str(b_code) + " offset " + str(offset) + " len(" + str(offset) + ") "
        #       + " unary(" + str(len_offset) + ") " + str(unary_len) + " Gamma " +  str(unary_len) + str(offset))
        return str(unary_len) + str(offset)

    def delta_encoding(self, gap):
        b_code = format(gap, "b")
        len_b = len(b_code)
        gamma_len = self.gamma_encoding(len_b)
        return str(gamma_len) + str(b_code[1:])

    @staticmethod
    def unary(num):
        ans = ""
        for j in range(num):
            ans += "1"

        return ans + "0"

