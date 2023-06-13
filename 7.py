def main(x):
    b = str(bin(int(x, 16)))[2::].rjust(33, '0')
    ln = len(b)

    s1 = b[ln - 9:ln]
    s2 = b[ln - 14:ln - 9]
    s3 = b[ln - 21:ln - 14]
    s4 = b[ln - 24:ln - 21]
    s5 = b[0: ln - 24]
    bin_response = s4 + s5 + s3 + s1 + s2
    hex_response = hex(int(bin_response, 2))

    return str(hex_response)


print(main('0x114083513'))
