"""
Day 16: Packet Decoder
"""
from functools import reduce
import operator


def parse_literal(b):
    i = 6
    nibs = []
    while True:
        print("--", b[i:(i+5)])
        last = (b[i] == "0")
        i += 1
        nibs.append(b[i:(i+4)])
        i += 4
        if last: break
    return int("".join(nibs), base=2), i


def parse_packet(b):
    if all(bd=="0" for bd in b):
        return None, len(b)
    print(f"parse packet: {b}")
    pver = int(b[0:3], base=2)
    ptype = int(b[3:6], base=2)
    print(f"{pver=}, {ptype=}")
    if ptype==4:
        literal, i = parse_literal(b)
        return (pver, ptype, literal), i
    len_type_id = b[6]
    sub_packets = []
    if len_type_id == "0":
        sub_packet_len = int(b[7:22], base=2)
        offset = 22
        i = offset
        j = i + sub_packet_len
        while i < j:
            print(f"{i=}, {j=}, {sub_packet_len=}")
            packet, spi = parse_packet(b[i:j])
            if packet:
                sub_packets.append(packet)
            i += spi
    elif len_type_id == "1":
        n_sub_packets = int(b[7:18], base=2)
        n = 0
        offset = 18
        i = offset
        while n < n_sub_packets:
            print(f"{n=}, {i=}")
            packet, spi = parse_packet(b[i:])
            if packet:
                sub_packets.append(packet)
            i += spi
            n += 1
    else:
        SyntaxError(f"Bad length type id {len_type_id}.")
    return (pver, ptype, sub_packets), i


def version_sum(t):
    pver, ptype, contents = t
    if ptype==4: return pver
    return pver + sum(version_sum(tsp) for tsp in contents)


def prod(factors):
    """
    return the product of a sequence of factors
    """
    return reduce(operator.mul, factors, 1)

def evaluate(t):
    pver, ptype, contents = t    
    # sum
    if ptype==0:
        return sum(evaluate(st) for st in contents)
    #product
    if ptype==1:
        return prod(evaluate(st) for st in contents)
    #min
    if ptype==2:
        return min(evaluate(st) for st in contents)
    #max
    if ptype==3:
        return max(evaluate(st) for st in contents)
    #literal
    if ptype==4:
        return contents
    #gt
    if ptype==5:
        assert len(contents)==2
        st1, st2 = contents
        return 1 if evaluate(st1) > evaluate(st2) else 0
    #lt
    if ptype==6:
        assert len(contents)==2
        st1, st2 = contents
        return 1 if evaluate(st1) < evaluate(st2) else 0
    #eq
    if ptype==7:
        assert len(contents)==2
        st1, st2 = contents
        return 1 if evaluate(st1) == evaluate(st2) else 0


def to_binary(h):
    return "".join(f"{int(hd, base=16):04b}" for hd in h)

def parse_hex(h):
    return parse_packet(to_binary(h))

def print_stuff(h):
    t, i = parse_hex(h)
    print('-'*80)
    print(h), print(t), print(version_sum(t)), print(evaluate(t))

print_stuff("D2FE28")
print_stuff("38006F45291200")
print_stuff("EE00D40C823060")
print_stuff("8A004A801A8002F478")
print_stuff("620080001611562C8802118E34")
print_stuff("C0015000016115A2E0802F182340")
print_stuff("A0016C880162017C3686B18A3D4780")

print_stuff("C200B40A82")
print_stuff("04005AC33890")
print_stuff("880086C3E88112")
print_stuff("CE00C43D881120")
print_stuff("D8005AC2A8F0")
print_stuff("F600BC2D8F")
print_stuff("9C005AC2F8F0")
print_stuff("9C0141080250320F1802104A08")

print_stuff("6053231004C12DC26D00526BEE728D2C013AC7795ACA756F93B524D8000AAC8FF80B3A7A4016F6802D35C7C94C8AC97AD81D30024C00D1003C80AD050029C00E20240580853401E98C00D50038400D401518C00C7003880376300290023000060D800D09B9D03E7F546930052C016000422234208CC000854778CF0EA7C9C802ACE005FE4EBE1B99EA4C8A2A804D26730E25AA8B23CBDE7C855808057C9C87718DFEED9A008880391520BC280004260C44C8E460086802600087C548430A4401B8C91AE3749CF9CEFF0A8C0041498F180532A9728813A012261367931FF43E9040191F002A539D7A9CEBFCF7B3DE36CA56BC506005EE6393A0ACAA990030B3E29348734BC200D980390960BC723007614C618DC600D4268AD168C0268ED2CB72E09341040181D802B285937A739ACCEFFE9F4B6D30802DC94803D80292B5389DFEB2A440081CE0FCE951005AD800D04BF26B32FC9AFCF8D280592D65B9CE67DCEF20C530E13B7F67F8FB140D200E6673BA45C0086262FBB084F5BF381918017221E402474EF86280333100622FC37844200DC6A8950650005C8273133A300465A7AEC08B00103925392575007E63310592EA747830052801C99C9CB215397F3ACF97CFE41C802DBD004244C67B189E3BC4584E2013C1F91B0BCD60AA1690060360094F6A70B7FC7D34A52CBAE011CB6A17509F8DF61F3B4ED46A683E6BD258100667EA4B1A6211006AD367D600ACBD61FD10CBD61FD129003D9600B4608C931D54700AA6E2932D3CBB45399A49E66E641274AE4040039B8BD2C933137F95A4A76CFBAE122704026E700662200D4358530D4401F8AD0722DCEC3124E92B639CC5AF413300700010D8F30FE1B80021506A33C3F1007A314348DC0002EC4D9CF36280213938F648925BDE134803CB9BD6BF3BFD83C0149E859EA6614A8C")
